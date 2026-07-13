# import math


# def encrypt(message, key):

#     message = message.replace(" ", "_")

#     columns = key
#     rows = math.ceil(len(message) / columns)

#     matrix = []

#     index = 0

#     for i in range(rows):

#         row = []

#         for j in range(columns):

#             if index < len(message):
#                 row.append(message[index])

#             else:
#                 row.append("X")

#             index += 1

#         matrix.append(row)

#     cipher = ""

#     for j in range(columns):
#         for i in range(rows):
#             cipher += matrix[i][j]

#     return cipher


# def decrypt(cipher, key):

#     columns = key
#     rows = math.ceil(len(cipher) / columns)

#     matrix = [['' for _ in range(columns)] for _ in range(rows)]

#     index = 0

#     for j in range(columns):
#         for i in range(rows):

#             if index < len(cipher):
#                 matrix[i][j] = cipher[index]
#                 index += 1

#     message = ""

#     for i in range(rows):
#         for j in range(columns):
#             message += matrix[i][j]

#     return message.replace("X", "").replace("_", " ")


# def main():

#     while True:

#         print("\n===== Transposition Cipher =====")
#         print("1. Encrypt")
#         print("2. Decrypt")
#         print("3. Exit")

#         choice = input("Enter choice: ")

#         if choice == "1":

#             text = input("Enter Message: ")
#             key = int(input("Enter Key (Columns): "))

#             print("\nEncrypted:")
#             print(encrypt(text, key))

#         elif choice == "2":

#             text = input("Enter Cipher Text: ")
#             key = int(input("Enter Key (Columns): "))

#             print("\nDecrypted:")
#             print(decrypt(text, key))

#         elif choice == "3":
#             break

#         else:
#             print("Invalid Choice")


# if __name__ == "__main__":
#     main()



import tkinter as tk
import math


def encrypt(message, key):

    message = message.replace(" ", "_")

    rows = math.ceil(len(message) / key)

    matrix = []

    index = 0

    for i in range(rows):

        row = []

        for j in range(key):

            if index < len(message):
                row.append(message[index])

            else:
                row.append("X")

            index += 1

        matrix.append(row)

    cipher = ""

    for j in range(key):
        for i in range(rows):
            cipher += matrix[i][j]

    return cipher


def decrypt(cipher, key):

    rows = math.ceil(len(cipher) / key)

    matrix = [['' for _ in range(key)] for _ in range(rows)]

    index = 0

    for j in range(key):
        for i in range(rows):
            if index < len(cipher):
                matrix[i][j] = cipher[index]
                index += 1

    text = ""

    for i in range(rows):
        for j in range(key):
            text += matrix[i][j]

    return text.replace("X", "").replace("_", " ")


def encrypt_click():

    text = message.get()
    key = int(column.get())

    output.delete(0, tk.END)
    output.insert(0, encrypt(text, key))


def decrypt_click():

    text = message.get()
    key = int(column.get())

    output.delete(0, tk.END)
    output.insert(0, decrypt(text, key))


root = tk.Tk()
root.title("Transposition Cipher")

tk.Label(root, text="Message").pack()

message = tk.Entry(root, width=40)
message.pack()

tk.Label(root, text="Key (Columns)").pack()

column = tk.Entry(root)
column.pack()

tk.Button(root, text="Encrypt", command=encrypt_click).pack()

tk.Button(root, text="Decrypt", command=decrypt_click).pack()

output = tk.Entry(root, width=40)
output.pack(pady=10)

root.mainloop()