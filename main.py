import os
import firebase_admin
from firebase_admin import credentials, auth, firestore
from flask import render_template, Flask, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'super_secret_key' # Required for flash messages

# Initialize Firebase Admin SDK
try:
    # Try to load credentials from a file if it exists
    cred = credentials.Certificate("serviceAccountKey.json")
    firebase_admin.initialize_app(cred)
except Exception as e:
    try:
        # Fallback to default credentials (e.g. env vars or GCP environment)
        firebase_admin.initialize_app()
    except Exception as e2:
        print("Warning: Firebase could not be initialized.", e2)

@app.route("/")
def index():
    nome = 'icoma.com.br'
    return render_template('index.html', site = nome)

@app.route("/login")
def login():
    return render_template('login/login.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')
        confirma_senha = request.form.get('confirma_senha')

        if senha != confirma_senha:
            flash('As senhas não coincidem.', 'error')
            return render_template('login/register.html', site='icoma.com.br')
        
        try:
            # 1. Create user in Firebase Authentication
            user = auth.create_user(
                email=email,
                password=senha,
                display_name=nome
            )
            
            # 2. Add user data to Firestore 'users' collection
            db = firestore.client()
            db.collection('users').document(user.uid).set({
                'nome': nome,
                'email': email,
                'created_at': firestore.SERVER_TIMESTAMP
            })
            
            flash('Conta criada com sucesso! Faça login para continuar.', 'success')
            return redirect(url_for('login'))
            
        except Exception as e:
            # Handle specific Firebase errors or general exceptions
            flash(f'Erro ao criar conta: {str(e)}', 'error')
            return render_template('login/register.html', site='icoma.com.br')

    return render_template('login/register.html', site='icoma.com.br')

def main():
    app.run(host="0.0.0.0", port = int(os.environ.get("PORT", 10000)))

if __name__ == "__main__":
    main()