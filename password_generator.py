import random  # Memasukan modul secara acak
import string  # Memasukkan modul string
import customtkinter
from tkinter import LEFT
import tkinter as tk

root = customtkinter.CTk()
entry1 = customtkinter.CTkEntry(root, placeholder_text="Test")

customtkinter.set_appearance_mode("dark")

root.iconbitmap("pw.ico")
root.title("Password Generator By Raja")
root.geometry("400x200")
label = customtkinter.CTkLabel(
    root, text="Password Generator", font=("Times New Roman", 20))
label.pack(pady=5, padx=10)
root.configure(fg_color=("black"))

frame = customtkinter.CTkFrame(root)
frame.configure(fg_color=("black"))
frame.pack(pady=5, padx=10)

entry1 = customtkinter.CTkEntry(
    frame, placeholder_text="Minimum Lenght")
entry1.pack(fill='x', expand=True, side=LEFT, pady=10, padx=5)
entry1.configure(fg_color=("white"), text_color="black")

dice_image = tk.PhotoImage(file="dadu.png")


# Variabel default nya
def generate_password(min_Length, numbers=False, special_chararters=False):
    letters = string.ascii_letters  # Menyimpan Semua Huruf
    digits = string.digits  # Menyimpan Angka
    special = string.punctuation  # Menyimpan Simbol

    # Generate Pw Nya
    characters = letters
    if numbers:
        characters += digits
        if special_chararters:
            characters += special
    elif special_chararters:  # Crucial Cuyyy!
        characters += special  # elseif..  kode ini akan menambahkan karakter spesial ke dalam kumpulan karakter yang valid, tanpa menambahkan angka !! :>

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_Length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_chararters:
            meets_criteria = meets_criteria and has_special

    return pwd


def enter_Length(event):
    try:
        min_Length = int(entry1.get())
        print(f"Minimum Lenght: {min_Length}")
    except ValueError:
        print("Invalid Input")


def button_event():
    print("Button Ter Pressed Di Terminal")

    has_special = special_check_var.get() == "on"
    has_number = number_check_var.get() == "on"

    try:
        min_Length = int(entry1.get())
    except ValueError:
        print("Invalid")

    pwd = generate_password(min_Length, has_number, has_special)

    entry2.delete(0, customtkinter.END)
    entry2.insert(0, pwd)

    print(pwd)


button = customtkinter.CTkButton(
    frame, image=dice_image, command=button_event)
button.configure(fg_color="transparent", text="", width=0)
button.pack(side=LEFT, pady=5, padx=5)


def checkbox_event1():
    print("Checkbox Sudah Di Tekan (cbox1):", special_check_var.get())


special_check_var = customtkinter.StringVar(value="on")
checkbox = customtkinter.CTkCheckBox(root, text="special_char", command=checkbox_event1,
                                     variable=special_check_var, onvalue="on", offvalue="off")
checkbox.pack(pady=9, padx=8)
checkbox.configure(fg_color="green")

# bug di checkbox_event2


def checkbox_event2():
    print("Checkbox Sudah Di Tekan (cbox2):", number_check_var.get())


number_check_var = customtkinter.StringVar(value="on")
checkbox_number = customtkinter.CTkCheckBox(root, text="has_number", command=checkbox_event2,
                                            variable=number_check_var, onvalue="on", offvalue="off")
checkbox_number.pack(pady=5, padx=8)
checkbox_number.configure(fg_color="green")

entry2 = customtkinter.CTkEntry(
    frame, placeholder_text="Password")
entry2.pack(fill='x', expand=True, side=LEFT, pady=10, padx=5)
entry2.configure(fg_color=("white"), text_color="black")


entry1.bind("<Return>", enter_Length)


root.mainloop()


def generate_password(min_Length, numbers=False, special_chararters=False):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
        if special_chararters:
            characters += special

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) > min_Length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_chararters:
            meets_criteria = meets_criteria and has_special

    return pwd


min_Length = int(input("Masukkan Minimal Input: "))
# (.lower) Untuk menghasilkan outpun berbais lowercase
has_number = input("Maukah menggunakan nomer (y/n)? ").lower() == "y"
has_special = input("Maukah menggunakan huruf spesial (y/n)? ").lower() == "y"
pwd = generate_password(min_Length, has_number, has_special)
print("Generated Password: ", pwd)


pwd = generate_password(10)
print(pwd)
