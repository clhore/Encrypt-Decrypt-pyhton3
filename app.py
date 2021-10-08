# encoding: utf-8

# library
import tkinter as tk
from tkinter.filedialog import askopenfile
import os

# import custom module
from mymodule import EncryptDecrypt

root = tk.Tk()

canvas = tk.Canvas(root, width=100, height=100)
canvas.grid(columnspan=2, rowspan=2)

# global variable
key = open('key.key', 'rb').read()

def generateKey():
    key = EncryptDecrypt.EncryptDecrypt().generateKey()
    # print(key)


def encryptFile():
    browse_text.set("encrypting ...")
    file = tk.filedialog.askdirectory()
    if file:
        try:
            # extract files
            files = os.listdir('data')
            listFile = ['data' + '\\' + file for file in files]

            # load key in class
            file = EncryptDecrypt.EncryptDecrypt(key)
            # class mode
            file.encryptFile(listFile)  # encrypt

            page_content = 'ENCRYPT'

            # text box
            text_box = tk.Text(root, height=2, width=10, padx=10, pady=10)
            text_box.insert(1.0, page_content)
            text_box.tag_configure("center", justify="center")
            text_box.tag_add("center", 1.0, "end")
            text_box.grid(column=1, row=1)

            browse_text.set("ENCRYPT")
        except Exception as e:
            page_content = f'ERROR: {str(e)}'


def decryptFileFile():
    browse_ext.set("decrypting ...")
    file = tk.filedialog.askdirectory()
    if file:
        try:
            # extract files
            files = os.listdir('data')
            listFile = ['data' + '\\' + file for file in files]

            # load key in class
            file = EncryptDecrypt.EncryptDecrypt(key)
            # class mode
            file.decryptFile(listFile)  # encrypt

            page_content = 'DECRYPT'

            # text box
            text_box = tk.Text(root, height=2, width=10, padx=10, pady=10)
            text_box.insert(1.0, page_content)
            text_box.tag_configure("center", justify="center")
            text_box.tag_add("center", 1.0, "end")
            text_box.grid(column=1, row=1)

            browse_ext.set("DECRYPT")
        except Exception as e:
            page_content = f'ERROR: {str(e)}'


# browse button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, command=lambda: encryptFile(),
                       font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
browse_text.set("ENCRYPT")
browse_btn.grid(column=0, row=0)

browse_ext = tk.StringVar()
browse_bn = tk.Button(root, textvariable=browse_ext, command=lambda: decryptFileFile(),
                      font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
browse_ext.set("DECRYPT")
browse_bn.grid(column=1, row=0)

browse_et = tk.StringVar()
browse_n = tk.Button(root, textvariable=browse_et, command=lambda: generateKey(),
                      font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
browse_et.set("GENERATE kEY")
browse_n.grid(columnspan=1)

canvas = tk.Canvas(root, width=10, height=10)
canvas.grid(columnspan=2)

root.mainloop()
