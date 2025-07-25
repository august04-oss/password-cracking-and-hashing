import time

# Simulated target password (in a real case, it would be hashed)
target_password = "shadowhunter"

# Sample dictionary (you can also load from a file)
dictionary = [
    "123456", "password", "qwerty", "letmein", "dragon",
    "iloveyou", "shadow", "hunter", "shadowhunter", "admin"
]

found = False
attempts = 0
start_time = time.time()

print("\n🔍 Starting Dictionary Attack...\n")

for word in dictionary:
    attempts += 1
    print(f"Trying: {word}")
    time.sleep(0.1)  # Simulate realistic delay
    if word == target_password:
        found = True
        end_time = time.time()
        print("\n✅ Password Cracked!")
        print(f"Password: {word}")
        print(f"Attempts: {attempts}")
        print(f"Time Taken: {end_time - start_time:.4f} seconds")
        break

if not found:
    print("\n❌ Password not found in dictionary.")




# Sample Output (for target password "shadowhunter"):
# 🔍 Starting Dictionary Attack...

# Trying: 123456
# Trying: password
# Trying: qwerty
# Trying: letmein
# Trying: dragon
# Trying: iloveyou
# Trying: shadow
# Trying: hunter
# Trying: shadowhunter

# ✅ Password Cracked!
# Password: shadowhunter
# Attempts: 9
# Time Taken: 0.9103 seconds
