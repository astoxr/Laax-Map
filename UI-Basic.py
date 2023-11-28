import tkinter as tk
from PIL import Image, ImageTk


root = tk.Tk()
root.title("Laax-Map")
root.geometry("800x500")

# Load the JPG image
image_path = "C:\Users\lukas\Documents\GitHub\Laax-Map"  # Replace with the path to your JPG file
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)

# Create a label to display the image
label = tk.Label(root, image=photo)
label.pack(padx=10, pady=10)

root.mainloop()
