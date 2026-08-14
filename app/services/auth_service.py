from app.repositories.user_repository import UserRepository

class AuthService:
    def __init__(self):
        self.user_repo = UserRepository()

    def register_user(self, nome: str, email: str, senha: str, confirma_senha: str):
        """
        Business logic for registering a user.
        Validates the input and calls the repository.
        """
        if not nome or not email or not senha:
            raise ValueError("Todos os campos são obrigatórios.")

        if senha != confirma_senha:
            raise ValueError("As senhas não coincidem.")
        
        if len(senha) < 6:
            raise ValueError("A senha deve ter pelo menos 6 caracteres.")

        try:
            # 1. Create the user in Auth
            uid = self.user_repo.create_user_auth(email, senha, nome)
            
            # 2. Save additional data in Firestore
            self.user_repo.save_user_data(uid, nome, email)
            
            return True, "Conta criada com sucesso! Faça login para continuar."
        except Exception as e:
            # Re-raise the exception to be handled by the controller
            raise Exception(f"Erro ao criar conta: {str(e)}")
