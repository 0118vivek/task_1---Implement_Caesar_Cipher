# Implement caesar cipher ->>
# Create a Python program that can encrypt and decrypt text using the Caesar Cipher algorithm. Allow users to input a message and a shift value to perform encryption and decryption.

def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    
    if mode == 'decrypt':
        shift = -shift
    
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            new_char = chr(((ord(char.lower()) - ord('a') + shift_amount) % 26) + ord('a'))
            result += new_char.upper() if char.isupper() else new_char
        else:
            result += char
    
    return result

# Get user input
mode = input("Enter mode (encrypt/decrypt): ").strip().lower()
message = input("Enter the message: ")
shift = int(input("Enter shift value: "))

# Perform encryption or decryption
output = caesar_cipher(message, shift, mode)
print(f"Result: {output}")
