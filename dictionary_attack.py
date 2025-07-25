# File: password-cracking-and-hashing/dictionary_attack.py

target_password = "secure123"

# Simulated wordlist
wordlist = ["admin", "password", "123456", "secure123", "letmein"]

found = False
for word in wordlist:
    if word == target_password:
        print(f"[Dictionary Attack] Password found: {word}")
        found = True
        break

if not found:
    print("[Dictionary Attack] Password not found in wordlist.")
