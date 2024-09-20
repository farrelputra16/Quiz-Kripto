import tkinter as tk
from tkinter import filedialog, messagebox
from ciphers import vigenere_encrypt, vigenere_decrypt, playfair_encrypt, playfair_decrypt, hill_encrypt, hill_decrypt

class CipherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cipher Application")
        self.root.geometry("500x600")
        self.create_widgets()

    def create_widgets(self):
  
        self.cipher_label = tk.Label(self.root, text="Select Cipher:")
        self.cipher_label.pack(pady=5)

        self.cipher_type = tk.StringVar(value="vigenere")
        self.vigenere_radio = tk.Radiobutton(self.root, text="Vigenère Cipher", variable=self.cipher_type, value="vigenere")
        self.playfair_radio = tk.Radiobutton(self.root, text="Playfair Cipher", variable=self.cipher_type, value="playfair")
        self.hill_radio = tk.Radiobutton(self.root, text="Hill Cipher", variable=self.cipher_type, value="hill")
        
        self.vigenere_radio.pack()
        self.playfair_radio.pack()
        self.hill_radio.pack()

        
        self.key_label = tk.Label(self.root, text="Enter Encryption Key (min 12 characters):")
        self.key_label.pack(pady=5)
        self.key_entry = tk.Entry(self.root, width=40)
        self.key_entry.pack(pady=5)

       
        self.input_type_label = tk.Label(self.root, text="Select Input Method:")
        self.input_type_label.pack(pady=5)

        self.input_type = tk.StringVar(value="keyboard")
        self.keyboard_radio = tk.Radiobutton(self.root, text="Keyboard Input", variable=self.input_type, value="keyboard")
        self.file_radio = tk.Radiobutton(self.root, text="File Input", variable=self.input_type, value="file")
        self.keyboard_radio.pack()
        self.file_radio.pack()

       
        self.text_label = tk.Label(self.root, text="Enter your text (if keyboard input selected):")
        self.text_label.pack(pady=5)
        self.text_entry = tk.Text(self.root, height=5, width=40)
        self.text_entry.pack(pady=5)

        
        self.action_frame = tk.Frame(self.root)
        self.encrypt_button = tk.Button(self.action_frame, text="Encrypt", command=self.encrypt)
        self.decrypt_button = tk.Button(self.action_frame, text="Decrypt", command=self.decrypt)
        self.encrypt_button.pack(side="left", padx=10)
        self.decrypt_button.pack(side="right", padx=10)
        self.action_frame.pack(pady=10)

      
        self.output_label = tk.Label(self.root, text="Output:")
        self.output_label.pack(pady=5)
        self.output_text = tk.Text(self.root, height=5, width=40)
        self.output_text.pack(pady=5)

    def encrypt(self):
        key = self.key_entry.get()
        if len(key) < 12:
            messagebox.showerror("Error", "Key must be at least 12 characters long!")
            return

        text = self.get_input_text()
        if not text:
            return

        cipher_type = self.cipher_type.get()
        if cipher_type == "vigenere":
            result = vigenere_encrypt(text, key)
        elif cipher_type == "playfair":
            result = playfair_encrypt(text, key)
        else:
            result = hill_encrypt(text, key)

        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, result)

    def decrypt(self):
        key = self.key_entry.get()
        if len(key) < 12:
            messagebox.showerror("Error", "Key must be at least 12 characters long!")
            return

        text = self.get_input_text()
        if not text:
            return

        cipher_type = self.cipher_type.get()
        if cipher_type == "vigenere":
            result = vigenere_decrypt(text, key)
        elif cipher_type == "playfair":
            result = playfair_decrypt(text, key)
        else:
            result = hill_decrypt(text, key)

        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, result)

    def get_input_text(self):
        
        if self.input_type.get() == "keyboard":
            
            return self.text_entry.get("1.0", tk.END).strip()
        else:
           
            file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
            if not file_path:
                
                messagebox.showerror("Error", "No file selected!")
                return None
          
            with open(file_path, "r") as file:
                return file.read().strip()

if __name__ == "__main__":
    root = tk.Tk()
    app = CipherApp(root)
    root.mainloop()
