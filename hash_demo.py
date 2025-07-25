import hashlib
import bcrypt
import time

def hash_with_md5(password):
    return hashlib.md5(password.encode()).hexdigest()

def hash_with_sha1(password):
    return hashlib.sha1(password.encode()).hexdigest()

def hash_with_sha256(password):
    return hashlib.sha256(password.encode()).hexdigest()

def hash_with_bcrypt(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed, salt

# Demo password
password = "CyberShield@123"

print("\n🔐 Hashing Password with Various Algorithms...\n")
start = time.time()

# MD5
md5_hash = hash_with_md5(password)
print(f"🔸 MD5:      {md5_hash}")

# SHA1
sha1_hash = hash_with_sha1(password)
print(f"🔸 SHA1:     {sha1_hash}")

# SHA256
sha256_hash = hash_with_sha256(password)
print(f"🔸 SHA256:   {sha256_hash}")

# bcrypt
bcrypt_hash, salt = hash_with_bcrypt(password)
print(f"🔸 bcrypt:   {bcrypt_hash.decode()} (with salt)")

end = time.time()
print(f"\n✅ All hashes generated in {end - start:.4f} seconds")

# Verification Demo
print("\n🧪 Verifying bcrypt password...")
if bcrypt.checkpw(password.encode(), bcrypt_hash):
    print("✅ bcrypt Verification: Success")
else:
    print("❌ bcrypt Verification: Failed")


# Sample Output:

# Hashing Password with Various Algorithms...

# 🔸 MD5:      03ff9bba2d24446a8c90e967de66eaa5
# 🔸 SHA1:     c3ce83e4b2b934c84e11c042160f67122e449508
# 🔸 SHA256:   d1db53c917f889ee2c3a0a28d23579d5770663b47a6d6aa0b93ecda0339ec76d
# 🔸 bcrypt:   $2b$12$TWZ2sTgIkkiIU8RRVq7pmeBTPZfQsbBumNCFGpgZrsuT/57T2cBpy (with salt)

# ✅ All hashes generated in 0.0243 seconds

# 🧪 Verifying bcrypt password...
# ✅ bcrypt Verification: Success
