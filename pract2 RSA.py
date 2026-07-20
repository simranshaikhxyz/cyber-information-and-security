# from math import gcd

# # Function to find modular inverse
# def mod_inverse(e, phi):
#     for d in range(2, phi):
#         if (e * d) % phi == 1:
#             return d
#     return None

# # Input prime numbers
# p = int(input("Enter prime number p: "))
# q = int(input("Enter prime number q: "))

# # Calculate n and phi
# n = p * q
# phi = (p - 1) * (q - 1)

# print("\nValue of n =", n)
# print("Value of phi =", phi)

# # Input public key
# while True:
#     e = int(input("\nEnter public key (e): "))
#     if gcd(e, phi) == 1:
#         break
#     print("e must be coprime with phi. Try again.")

# # Calculate private key
# d = mod_inverse(e, phi)

# print("\nPublic Key :", (e, n))
# print("Private Key:", (d, n))

# # Input message
# message = int(input("\nEnter numeric message (< n): "))

# # Encryption
# cipher = pow(message, e, n)
# print("Encrypted Message:", cipher)

# # Decryption
# plain = pow(cipher, d, n)
# print("Decrypted Message:", plain)

# # Verify
# if message == plain:
#     print("\nRSA Encryption and Decryption Successful!")
# else:
#     print("\nDecryption Failed!")


from tkinter import *
from tkinter import messagebox
from math import gcd

# Function to find modular inverse
def mod_inverse(e, phi):
    for d in range(2, phi):
        if (e * d) % phi == 1:
            return d
    return None

# Encrypt Function
def encrypt():
    try:
        p = int(entry_p.get())
        q = int(entry_q.get())
        e = int(entry_e.get())
        message = int(entry_msg.get())

        n = p * q
        phi = (p - 1) * (q - 1)

        if gcd(e, phi) != 1:
            messagebox.showerror("Error", "e must be coprime with phi")
            return

        if message >= n:
            messagebox.showerror("Error", "Message must be less than n")
            return

        d = mod_inverse(e, phi)

        cipher = pow(message, e, n)
        plain = pow(cipher, d, n)

        lbl_public.config(text=f"Public Key : ({e}, {n})")
        lbl_private.config(text=f"Private Key : ({d}, {n})")
        lbl_encrypt.config(text=f"Encrypted Message : {cipher}")
        lbl_decrypt.config(text=f"Decrypted Message : {plain}")

    except:
        messagebox.showerror("Error", "Please enter valid numbers")


# GUI Window
root = Tk()
root.title("RSA Encryption & Decryption")
root.geometry("450x450")

Label(root, text="RSA Algorithm", font=("Arial", 16, "bold")).pack(pady=10)

Label(root, text="Prime Number (p)").pack()
entry_p = Entry(root)
entry_p.pack()

Label(root, text="Prime Number (q)").pack()
entry_q = Entry(root)
entry_q.pack()

Label(root, text="Public Key (e)").pack()
entry_e = Entry(root)
entry_e.pack()

Label(root, text="Numeric Message (< n)").pack()
entry_msg = Entry(root)
entry_msg.pack(pady=5)

Button(root, text="Encrypt & Decrypt", command=encrypt, bg="lightblue").pack(pady=10)

lbl_public = Label(root, text="")
lbl_public.pack()

lbl_private = Label(root, text="")
lbl_private.pack()

lbl_encrypt = Label(root, text="")
lbl_encrypt.pack()

lbl_decrypt = Label(root, text="")
lbl_decrypt.pack()

root.mainloop()