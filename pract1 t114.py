# def encrypt(text, shift):
#     result = ""

#     for char in text:
#         if char.isalpha():

#             if char.isupper():
#                 result += chr((ord(char) - 65 + shift) % 26 + 65)

#             else:
#                 result += chr((ord(char) - 97 + shift) % 26 + 97)

#         else:
#             result += char

#     return result


# def decrypt(text, shift):
#     return encrypt(text, -shift)


# def main():

#     while True:

#         print("\n===== Caesar Cipher =====")
#         print("1. Encrypt")
#         print("2. Decrypt")
#         print("3. Exit")

#         choice = input("Enter choice: ")

#         if choice == "1":

#             message = input("Enter message: ")
#             shift = int(input("Enter shift value: "))

#             encrypted = encrypt(message, shift)

#             print("\nEncrypted Message:")
#             print(encrypted)

#         elif choice == "2":

#             message = input("Enter encrypted message: ")
#             shift = int(input("Enter shift value: "))

#             decrypted = decrypt(message, shift)

#             print("\nDecrypted Message:")
#             print(decrypted)

#         elif choice == "3":
#             print("Thank You")
#             break

#         else:
#             print("Invalid Choice")


# if __name__ == "__main__":
#     main()

import tkinter as tk
from tkinter import messagebox


def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():

            base = 65 if char.isupper() else 97
            result += chr((ord(char) - base + shift) % 26 + base)

        else:
            result += char

    return result


def do_encrypt():
    text = entry_text.get()
    shift = int(entry_shift.get())

    result.delete(0, tk.END)
    result.insert(0, encrypt(text, shift))


def do_decrypt():
    text = entry_text.get()
    shift = int(entry_shift.get())

    result.delete(0, tk.END)
    result.insert(0, encrypt(text, -shift))


root = tk.Tk()
root.title("Caesar Cipher")

tk.Label(root, text="Message").pack()

entry_text = tk.Entry(root, width=40)
entry_text.pack()

tk.Label(root, text="Shift").pack()

entry_shift = tk.Entry(root)
entry_shift.pack()

tk.Button(root, text="Encrypt", command=do_encrypt).pack(pady=5)

tk.Button(root, text="Decrypt", command=do_decrypt).pack()

result = tk.Entry(root, width=40)
result.pack(pady=10)

root.mainloop()