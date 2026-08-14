import os
from app import create_app

app = create_app()

def main():
    app.run(host="0.0.0.0", port = int(os.environ.get("PORT", 10000)))

if __name__ == "__main__":
    main()