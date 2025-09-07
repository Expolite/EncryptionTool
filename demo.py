
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os

# --- Key setup ---
# AES-256 requires a 32-byte key
key = os.urandom(32)  # never hardcode in real apps
print(f"\033[30;43m[debug]\033[0m Key: {key}")

# --- Encrypt ---
aesgcm = AESGCM(key)

nonce = os.urandom(12)  # 96-bit nonce recommended
data = b"MySuperSecretPassword123"                      # plain text (my password)
aad = b"metadata"  # optional (for integrity check)

print(f"Original: {data}")

ciphertext = aesgcm.encrypt(nonce, data, aad)
print("Ciphertext:", ciphertext)

# --- Decrypt ---
print()
plaintext = aesgcm.decrypt(nonce, ciphertext, aad)
print("Decrypted:", plaintext.decode())

# Author: Ronnel Macompas
# Date: Sep 7, 2025
# Version: 001