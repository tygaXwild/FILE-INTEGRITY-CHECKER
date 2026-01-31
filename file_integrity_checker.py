import hashlib
import os

def calculate_hash(file_path):
    sha256 = hashlib.sha256()

    try:
        with open(file_path, "rb") as file:
            while True:
                data = file.read(4096)
                if not data:
                    break
                sha256.update(data)
        return sha256.hexdigest()

    except FileNotFoundError:
        print("File not found!")
        return None


def save_hash(file_path, hash_value):
    hash_file = file_path + ".hash"
    with open(hash_file, "w") as f:
        f.write(hash_value)
    print("Hash saved successfully.")


def load_hash(file_path):
    hash_file = file_path + ".hash"
    try:
        with open(hash_file, "r") as f:
            return f.read()
    except FileNotFoundError:
        print("Hash file not found!")
        return None


def check_integrity(file_path):
    old_hash = load_hash(file_path)
    if old_hash is None:
        return

    new_hash = calculate_hash(file_path)
    if new_hash is None:
        return

    if old_hash == new_hash:
        print("File integrity verified. No changes detected.")
    else:
        print("WARNING! File has been modified!")


# -------- MAIN --------
print("\n FILE INTEGRITY CHECKER")
print("1. Generate Hash")
print("2. Check Integrity")

choice = input("Enter your choice (1/2): ")
file_path = input("Enter file path: ")

if choice == "1":
    hash_value = calculate_hash(file_path)
    if hash_value:
        save_hash(file_path, hash_value)

elif choice == "2":
    check_integrity(file_path)

else:
    print("Invalid choice!")
