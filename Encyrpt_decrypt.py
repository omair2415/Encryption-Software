def encrypt(plain_text, shift):
    """
    Encrypts the given plain text using the Caesar Cipher encryption algorithm.
    """
    cipher_text = ""
    for char in plain_text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97  # ASCII offset based on uppercase or lowercase character
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)  # Apply the shift
            cipher_text += encrypted_char
        else:
            cipher_text += char  # Keep non-alphabetic characters unchanged
    return cipher_text


def decrypt(cipher_text, shift):
    """
    Decrypts the given cipher text using the Caesar Cipher encryption algorithm.
    """
    plain_text = ""
    for char in cipher_text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97  # ASCII offset based on uppercase or lowercase character
            decrypted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)  # Apply the reverse shift
            plain_text += decrypted_char
        else:
            plain_text += char  # Keep non-alphabetic characters unchanged
    return plain_text


def main():
    while True:
        print("\n----- Encryption Software -----")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            plain_text = input("Enter the plain text: ")
            shift = int(input("Enter the shift value: "))
            cipher_text = encrypt(plain_text, shift)
            print("Encrypted text:", cipher_text)
        elif choice == "2":
            cipher_text = input("Enter the cipher text: ")
            shift = int(input("Enter the shift value: "))
            plain_text = decrypt(cipher_text, shift)
            print("Decrypted text:", plain_text)
        elif choice == "3":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
