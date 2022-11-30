from cryptography.fernet import Fernet
import  os

user = os.getlogin()

def generate_key():

    key = Fernet.generate_key()
    with open(f"C:\\Users\\{user}\\Desktop\\secret.key", "wb") as key_file:
        key_file.write(key)
def load_key():

    return open(f"C:\\Users\\{user}\\Desktop\\secret.key", "rb").read()

def encryptSifre(sifre):

    key = load_key()
    encodedSifre = sifre.encode()
    f = Fernet(key)
    encrypted_sifre = f.encrypt(encodedSifre)

    return encrypted_sifre

def decryptSifre(sifre):

    key = load_key()
    f = Fernet(key)
    decrypted_sifre = f.decrypt(sifre)

    return decrypted_sifre


