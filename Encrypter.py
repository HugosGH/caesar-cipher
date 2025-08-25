def encrypt_a_message():
    inp_message = str(input("Input Message to be Encrypted: "))
    message = inp_message
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypted_message = ""
    offset = int(input("Input designated Offset: "))
    shift = offset


    def encrypt(message, offset):
        encrypted_message = ""
        for char in message.lower():
            if char in alphabet:
                index = alphabet.index(char)
                new_index = (index + offset) % len(alphabet)
                encrypted_message += alphabet[new_index]
            else:
                encrypted_message += char

        return encrypted_message

    encrypted = encrypt(message, shift)
    print("Encrypted Message: ", encrypted)

def decrypt_a_message():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    message = str(input("Input Message to be Decrypted: "))

    def decrypt_all(message):
        for offset in range(26):
            decrypted_message = ""
            for char in message.lower():
                if char in alphabet:
                    index = alphabet.index(char)
                    new_index = (index - offset) % len(alphabet)
                    decrypted_message += alphabet[new_index]
                else:
                    decrypted_message += char

            print(f"Offset {offset}: {decrypted_message}")
            
    decrypt_all(message)

print("Encrypt or Decrypt a message")
operation = input("What do you wanna do?: ")

if operation.lower() == "encrypt":
    encrypt_a_message()
elif operation.lower() == "decrypt":
    decrypt_a_message()