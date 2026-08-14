from dataclasses import dataclass

@dataclass
class User:
    uid: str
    nome: str
    email: str
    created_at: str = None
