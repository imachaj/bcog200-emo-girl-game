import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk
import pygame
from tkinter import filedialog
from PIL import ImageGrab

class Item:
    def __init__(self, image_path, item_type, x, y, width=100, height=100):
        
        self.x = x
        self.y = y
        self.type = item_type

        
        img = Image.open(image_path)

        #resize the image
        img = img.resize((width, height))

        
        self.image = ImageTk.PhotoImage(img)

class Girl:
    def __init__(self, canvas):
        #manipulate the images 
        self.canvas = canvas
        self.hair = None
        self.tops = None
        self.bottoms = None
        self.accessories = None

        # Use PIL to load base image
        img = Image.open("assets/base.png")
        resized_img = img.resize((280, 550), Image.Resampling.LANCZOS)

        self.base_image = ImageTk.PhotoImage(resized_img)
        self.base = self.canvas.create_image(300, 500, image=self.base_image)

    def set_item(self, item):
        #Change an item on the girl 
        if item.type == "hair":
            if self.hair:
                self.canvas.delete(self.hair)
            self.hair = self.canvas.create_image(item.x, item.y, image=item.image)
        elif item.type == "top":
            if self.tops:
                self.canvas.delete(self.tops)
            self.tops = self.canvas.create_image(item.x, item.y, image=item.image)
        elif item.type == "bottom":
            if self.bottoms:
                self.canvas.delete(self.bottoms)
            self.bottoms = self.canvas.create_image(item.x, item.y, image=item.image)
        elif item.type == "accessory":
            if self.accessories:
                self.canvas.delete(self.accessories)
            self.accessories = self.canvas.create_image(item.x, item.y, image=item.image)

class EmoGame:
    def __init__(self, root):
        #Main game class where we handle all buttons, image swaps
        self.root = root
        self.root.configure(bg="#d90166")
        self.root.title("Pocket Emo Girl")
        self.root.geometry("600x800")

        #Create canvas and add it to the grid
        self.canvas = tk.Canvas(root, width=600, height=800, bg="#d90166")
        self.canvas.grid(row=0, column=0, sticky="nsew") 
        bg_img = Image.open("assets/background.png")
        bg_img = bg_img.resize((600, 800))
        self.bg_image = ImageTk.PhotoImage(bg_img)
        self.canvas.create_image(0, 0, image=self.bg_image, anchor="nw") 

        self.girl = Girl(self.canvas)

        #Load options
        self.hair_options = [
            Item("assets/hair1.png", "hair", 300, 490, width= 290, height=510),
            Item("assets/hair2.png", "hair", 300, 490, width= 290, height=510),
        ]
        
        self.top_options = [
            Item("assets/top1.png", "top", 295, 480, width = 260, height= 410),  # Top 1
            Item("assets/top2.png", "top", 295, 480, width = 240, height= 405),  # Top 2
        ]

        self.bottom_options = [
            Item("assets/bottom1.png", "bottom", 300, 480, width = 230, height = 500),  # Bottom 1
            Item("assets/bottom2.png", "bottom", 300, 490, width = 240, height= 452),  # Bottom 2
        ]

        self.accessory_options = [
            Item("assets/accessory1.png", "accessory", 302, 490, width = 300, height = 300),
            Item("assets/accessory2.png", "accessory", 302, 400, width=300, height= 300),
            Item("assets/accessory3.png", "accessory", 302, 400, width=300, height=300),
        ]

        self.hair_index = 0
        self.top_index = 0
        self.bottom_index = 0
        self.accessory_index = 0

        pygame.mixer.init()

        #background music
        pygame.mixer.music.load("assets/background_music.mp3")
        pygame.mixer.music.play(-1, 0.0)

        #frame to hold buttons 
        self.button_frame = tk.Frame(root)
        self.button_frame.configure(bg="#d90166")
        self.button_frame.grid(row=1, column=0, sticky="ew") 

        #buttons 
        self.hair_button = tk.Button(
            self.button_frame,
            text="Change Hair",
            command=self.change_hair,
            bg="#ffc0cb",               # pastel pink
            fg="#000000",               # black text
            font=("Comic Sans MS", 10, "bold"),
            relief="groove",
            activebackground="#ff69b4", # hot pink
            activeforeground="#ffffff",
            borderwidth=3
        )
        self.hair_button.grid(row=0, column=0, padx=10, pady=10)

        self.top_button = tk.Button(
            self.button_frame,
            text="Change Top",
            command=self.change_top,
            bg="#ffc0cb",               # pastel pink
            fg="#000000",               # black text
            font=("Comic Sans MS", 10, "bold"),
            relief="groove",
            activebackground="#ff69b4", # hot pink
            activeforeground="#ffffff",
            borderwidth=3
        )

        self.top_button.grid(row=0, column=1, padx=10, pady=10)

        self.bottom_button = tk.Button(
            self.button_frame,
            text="Change Bottom",
            command=self.change_bottom,
            bg="#ffc0cb",               # pastel pink
            fg="#000000",               # black text
            font=("Comic Sans MS", 10, "bold"),
            relief="groove",
            activebackground="#ff69b4", # hot pink
            activeforeground="#ffffff",
            borderwidth=3
        )

        self.bottom_button.grid(row=0, column=2, padx=10, pady=10)

        self.accessory_button = tk.Button(
            self.button_frame,
            text="Change Accessory",
            command=self.change_accessory,
            bg="#ffc0cb",               # pastel pink
            fg="#000000",               # black text
            font=("Comic Sans MS", 10, "bold"),
            relief="groove",
            activebackground="#ff69b4", # hot pink
            activeforeground="#ffffff",
            borderwidth=3
        )

        self.accessory_button.grid(row=0, column=3, padx=10, pady=10)

        self.save_button = tk.Button(
            self.button_frame,
            text="Save Button:3",
            command=self.save_screenshot,
            bg="#ffc0cb",               # pastel pink
            fg="#000000",               # black text
            font=("Comic Sans MS", 10, "bold"),
            relief="groove",
            activebackground="#ff69b4", # hot pink
            activeforeground="#ffffff",
            borderwidth=3
        )

        self.save_button.grid(row=0, column=4, padx=10, pady=10)

        #
        self.button_frame.grid_columnconfigure(0, weight=1)
        self.button_frame.grid_columnconfigure(1, weight=1)
        self.button_frame.grid_columnconfigure(2, weight=1)
        self.button_frame.grid_columnconfigure(3, weight=1)
        self.button_frame.grid_columnconfigure(4, weight=1)

    #these change the images
    def change_hair(self):
        
        self.hair_index = (self.hair_index + 1) % len(self.hair_options)
        self.girl.set_item(self.hair_options[self.hair_index])

    def change_top(self):
        
        self.top_index = (self.top_index + 1) % len(self.top_options)
        self.girl.set_item(self.top_options[self.top_index])

    def change_bottom(self):
       
        self.bottom_index = (self.bottom_index + 1) % len(self.bottom_options)
        self.girl.set_item(self.bottom_options[self.bottom_index])

    def change_accessory(self):
        
        self.accessory_index = (self.accessory_index + 1) % len(self.accessory_options)
        self.girl.set_item(self.accessory_options[self.accessory_index])

    def save_screenshot(self):
    #ask the user where to save the image
        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png")],
            title="Save Screenshot As"
        )

        if file_path:  
            self.root.update()
            x = self.canvas.winfo_rootx()+75
            y = self.canvas.winfo_rooty()+300
            w = x + self.canvas.winfo_width()
            h = y + self.canvas.winfo_height()-200

            img = ImageGrab.grab(bbox=(x, y, w, h))
            img.save(file_path)
            print(f"Screenshot saved as {file_path}")



if __name__ == "__main__":
    root = tk.Tk()
    icon = tk.PhotoImage(file="assets/emo_icon.png")
    root.iconphoto(True, icon)
    game = EmoGame(root)
    root.mainloop()