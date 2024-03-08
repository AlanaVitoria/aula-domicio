import os 
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


class ImageBrowserApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Navegar de Imagens")
        
        self.image_paths = []
        self.current_image_index = 0
        
        self.image_label = tk.Label(root)
        self.image_label.pack(padx=10, pady=10)
        
        browse_button = tk.Button(root, text="Selecionar Diretório", command=self.browse_directory)
        browse_button.pack(padx=10, pady=5)
        
        self.prev_button = tk.Button(root, text="Anterior", state=tk.DISABLED, command=self.show_previous_image)
        self.prev_button.pack(side=tk.LEFT, padx=10, pady=5)
        
        self.next_button = tk.Button(root, text="Próxima", state=tk.DISABLED, command=self.show_next_image)
        self.next_button.pack(side=tk.RIGHT, padx=10, pady=5)
        
    def browse_directory(self):
        directory_path = filedialog.askdirectory()
        if directory_path:
            self.image_paths = [
                 os.path.join(directory_path, file)
                for file in os.listdir(directory_path)
                if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))
            ]
            if self.image_paths:
                self.current_image_index = 0
                self.show_image(self.current_image_index)
                self.prev_button.config(state=tk.NORMAL)
