import customtkinter as ctk
from PIL import ImageTk
import os
import math

class App(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.title("Space Blaster")
        self.geometry("-5-0")
        self.resizable(0, True)
        self.canvas_size = 300
        # self.iconpath = ImageTk.PhotoImage(file=os.path.join("/assets/logo.png"))
        # self.root.wm_iconbitmap()
        # self.root.iconphoto(False, self.iconpath)
        # myCanvas=ctk.CTkCanvas(self,height=50,width=50,bd=50,background=)
        # myCanvas.grid(row=0,column=0)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.canvas = ctk.CTkCanvas(self, width=self.canvas_size, height=self.canvas_size, bg="white")
        self.canvas.grid(row=0,column=0)

        self.canvas.bind("<Button-1>", self.on_click)
        # self.canvas.create_arc(0, 0, 300, 300,width=1,start=0, extent=-180)
        flat_coordinates = [
            119.67,238.75,-32.83,28.70,2.78,13.64,33.87,0.06,4.71,-3.54,9.42,-3.54,152.64,-3.54,4.71,3.54,33.87,-0.06,2.78,-13.64,-32.82,-28.70,-32.82,-13.54,65.94,-13.54,65.94,-14.13,65.94,-9.93,-2.65,-5.89,-2.65,5.89,-2.65,1.44,-2.65,-1.44,-2.65,-5.89,-2.66,5.89,-2.66,9.93,-2.66,14.13,65.94,14.13,65.94,238.75,119.67,238.75

        ]
        
        self.canvas.create_polygon(flat_coordinates, fill="gray", outline="black")

    
    
    def on_click(self, event):
        x = event.x
        y = event.y

        custom_x = x - 150 
        custom_y = 300 - y  

        print(f"Click: ({custom_x}, {custom_y})")


if __name__ == "__main__":
    app = App()
    app.mainloop()