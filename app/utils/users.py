import bcrypt
from cryptography.fernet import Fernet

# Генерация ключа (это нужно делать один раз и сохранять ключ)
key = Fernet.generate_key()

# Инициализация шифратора
cipher = Fernet(key)

def hash_password(password: str) -> str:
    # Генерация соль и хэширование пароля
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password.decode()


def encrypt_phone(phone: str) -> str:
    encrypted_phone = cipher.encrypt(phone.encode())
    return encrypted_phone.decode()

def decrypt_phone(encrypted_phone: str) -> str:
    decrypted_phone = cipher.decrypt(encrypted_phone.encode())
    return decrypted_phone.decode()