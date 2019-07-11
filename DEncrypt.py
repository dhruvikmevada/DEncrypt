"""
Date Created: 10-07-2018

Developed By: Mevada Dhruvik

E-mail: dhruvikhm98@gmail.com

Description: This encryption and decryption program is based on concept of stream cipher algorithm. Both character and numeric input is valid.

"""


# Section A: Encryption Process

# Global declaration
my_list = []
plain_text = []
original_text_list = []


def encryption():
    text = str(input("Enter Text here : "))[::-1]  # reverses the string
    key = int(input("Enter the Key Value : "))
    i = 0
    for i in text:
        cipher = ord(i) + key  # converts it into numeric value and add key value to every bit
        my_list.append(cipher)  # appends the encrypted bit value to list variable
        # print(cipher)
    enc_msg = ''.join(map(str, my_list))  # joins the list elements and stores it in string form
    print(enc_msg)


# Section B: Decryption Process
# In this section all operations will be performed in reverse
def decryption():

    s_key = int(input("Enter Key to Decrypt : "))
    i = 0
    for j in my_list:
        plain = my_list[i] - s_key
        plain_text.append(plain)
        i = i+1

    i = 0
    for k in plain_text:
        original_text = chr(plain_text[i])
        original_text_list.append(original_text)
        i = i+1

    original_msg = ''.join(map(str, original_text_list))
    print(original_msg[::-1])


print("\nThis is a program to encrypt the entered text.. \n")

encryption()
ask = input("Do you want to Decrypt? (Y/N): ")
if ask == 'y' or ask == 'Y':
    decryption()
else:
    exit()
