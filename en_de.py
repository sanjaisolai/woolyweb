from cryptography.fernet import Fernet
key = Fernet.generate_key()
cipher_suite = Fernet(key)
def encrypt(text_to_encrypt):
    print(key)
    encrypted_text = cipher_suite.encrypt(text_to_encrypt.encode())
    encrypted_text=encrypted_text.hex()
    return encrypted_text
def decrypt(en_text):
    en_text=bytes.fromhex(en_text)
    decrypted_text = cipher_suite.decrypt(en_text).decode()
    return decrypted_text



 
