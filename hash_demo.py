# File: password-cracking-and-hashing/hash_demo.py

import hashlib
import bcrypt

# Example password
password = "mySecretPassword123"

# SHA-256 Hashing
sha256_hash = hashlib.sha256(password.encode()).hexdigest()
print("[SHA-256] Hashed Password:", sha256_hash)

# SHA-512 Hashing
sha512_hash = hashlib.sha512(password.encode()).hexdigest()
print("[SHA-512] Hashed Password:", sha512_hash)

# Bcrypt Hashing (auto-salts)
bcrypt_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
print("[Bcrypt] Hashed Password:", bcrypt_hash.decode())

# Verifying the password using bcrypt
check = bcrypt.checkpw(password.encode(), bcrypt_hash)
print("[Bcrypt] Password Match:", check)
