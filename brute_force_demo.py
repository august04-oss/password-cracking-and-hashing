# File: password-cracking-and-hashing/brute_force_demo.py

import itertools
import time

target_password = "42"
charset = "0123456789"
found = False

start_time = time.time()

for length in range(1, 5):
    for guess in itertools.product(charset, repeat=length):
        guess = ''.join(guess)
        if guess == target_password:
            print(f"[Brute Force] Password found: {guess}")
            found = True
            break
    if found:
        break

end_time = time.time()
print("Time taken: {:.4f} seconds".format(end_time - start_time))
