import itertools
import string
import time

# Target password to crack (you can change this!)
target_password = "a3"

# Character set: digits + lowercase letters
charset = string.digits + string.ascii_lowercase  # 0-9 + a-z

max_length = 3  # Set based on complexity you want to test

attempts = 0
start_time = time.time()

print("Brute Force Attack Started...\n")
found = False

for length in range(1, max_length + 1):
    for guess_tuple in itertools.product(charset, repeat=length):
        guess = ''.join(guess_tuple)
        attempts += 1
        print(f"Trying: {guess}")
        if guess == target_password:
            end_time = time.time()
            print("\n✅ Password Found!")
            print(f"Password: {guess}")
            print(f"Attempts: {attempts}")
            print(f"Time Taken: {end_time - start_time:.4f} seconds")
            found = True
            break
    if found:
        break

if not found:
    print("\n❌ Password not found within given charset/length.")






# Sample Output (when target_password = "a3"):

# Brute Force Attack Started...

# Trying: 0
# Trying: 1
# Trying: 2
# ...
# Trying: a2
# Trying: a3

# ✅ Password Found!
# Password: a3
# Attempts: 74
# Time Taken: 0.0923 seconds
