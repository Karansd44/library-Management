from tkinter import *
from PIL import ImageTk, Image  # for image handling
import random  # for color randomization

class librarymanagementSystem:
  def __init__(self, root):
    self.root = root
    self.root.title("Library Management System")
    self.root.geometry("1024x768")  # Adjust window size as needed

    # Create a canvas for background image and UI elements
    self.canvas = Canvas(self.root, width=1024, height=768)
    self.canvas.pack(fill=BOTH, expand=True)

    # Load a background image (replace 'library.jpg' with your image path)
    self.bg_image = Image.open("library.jpg")
    self.bg_image = self.bg_image.resize((1024, 768), Image.ANTIALIAS)  # Resize image
    self.bg_photo = ImageTk.PhotoImage(self.bg_image)
    self.bg_label = Label(self.canvas, image=self.bg_photo)
    self.bg_label.place(relwidth=1, relheight=1)  # Stretch image to fill canvas

    # Generate a random color for the title text
    self.text_color = "#" + ''.join(random.choice('0123456789ABCDEF') for i in range(6))

    # Create a styled label for the title using Label
    self.lbltitle = Label(self.canvas, text="LIBRARY MANAGEMENT SYSTEM",
                             font=("Arial", 40, "bold"),
                             fg=self.text_color,  # Set dynamically generated color
                             justify=CENTER,  # Center align text
                             shadow=True, shadowthickness=2, shadowoffset=(2, 2))  # Add shadow effect
    self.lbltitle.place(relx=0.5, rely=0.1, anchor=CENTER)  # Position title in center

    # Add some space after the title (optional)
    Label(self.canvas, text="", font=("Arial", 12)).place(relx=0.5, rely=0.25, anchor=CENTER)

if __name__ == "__main__":
  root = Tk()
  obj = librarymanagementSystem(root)
  root.mainloop()
