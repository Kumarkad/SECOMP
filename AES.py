from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64

def encrypt(plain_text, key):
    # Generate a random initialization vector
    iv = get_random_bytes(16)
    
    # Create an AES cipher object with the given key and AES.MODE_CBC mode
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # Pad the plain text and encrypt it
    cipher_text = cipher.encrypt(pad(plain_text.encode(), AES.block_size))
    
    # Concatenate the initialization vector and cipher text
    encrypted_text = iv + cipher_text
    
    # Encode the encrypted text in base64 for easy storage/transmission
    encoded_text = base64.b64encode(encrypted_text)
    
    return encoded_text


def decrypt(encoded_text, key):
    # Decode the base64 encoded text
    encrypted_text = base64.b64decode(encoded_text)
    
    # Extract the initialization vector from the encrypted text
    iv = encrypted_text[:16]
    
    # Create an AES cipher object with the given key, AES.MODE_CBC mode, and the initialization vector
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # Decrypt the cipher text and remove the padding
    decrypted_text = unpad(cipher.decrypt(encrypted_text[16:]), AES.block_size)
    
    return decrypted_text.decode()

# Example usage:
key = b'ThisIsASecretKey'
plain_text = 'Hello, World!'

# Encrypt the plain text
encrypted = encrypt(plain_text, key)
print("Encrypted Text:", encrypted)

# Decrypt the encrypted text
decrypted = decrypt(encrypted, key)
print("Decrypted Text:", decrypted)