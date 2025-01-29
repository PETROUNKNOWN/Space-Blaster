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
        self.canvas_size = 800
        # self.iconpath = ImageTk.PhotoImage(file=os.path.join("/assets/logo.png"))
        # self.root.wm_iconbitmap()
        # self.root.iconphoto(False, self.iconpath)
        # myCanvas=ctk.CTkCanvas(self,height=50,width=50,bd=50,background=)
        # myCanvas.grid(row=0,column=0)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.canvasWidget = ctk.CTkCanvas(self, width=self.canvas_size, height=self.canvas_size, bg="white")
        self.canvasWidget.grid(row=0,column=0)

        self.canvasWidget.bind("<Button-1>", self.on_click)
        self.canvasWidget.bind('<Right>',self.flyRight)
        self.canvasWidget.bind('<Left>',self.flyLeft)
        # self.canvasWidget.bind('<Right>',lambda event: self.moveJet(event,"right"))
        # self.canvasWidget.bind('<Left>',lambda event: self.moveJet(event,"left"))
        self.canvasWidget.bind('<Up>',lambda event: self.moveJet(event,"up"))
        self.canvasWidget.bind('<Down>',lambda event: self.moveJet(event,"down"))
        self.canvasWidget.focus_set()
        # self.canvas.create_arc(0, 0, 300, 300,width=1,start=0, extent=-180)
        jetSize=100
        flat_coordinates = [
            0.5*jetSize,0.05*jetSize,
            0.54*jetSize,0.17*jetSize,
            0.565*jetSize,0.35*jetSize,
            0.59*jetSize,0.44*jetSize,
            0.59*jetSize,0.49*jetSize,
            0.775*jetSize,0.615*jetSize,
            0.775*jetSize,0.56*jetSize,
            0.78*jetSize,0.55*jetSize,
            0.785*jetSize,0.56*jetSize,
            0.785*jetSize,0.75*jetSize,
            0.775*jetSize,0.75*jetSize,
            0.775*jetSize,0.715*jetSize,
            0.56*jetSize,0.715*jetSize,
            0.56*jetSize,0.81*jetSize,
            0.67*jetSize,0.895*jetSize,
            0.67*jetSize,0.955*jetSize,
            0.57*jetSize,0.955*jetSize,
            0.57*jetSize,0.94*jetSize,
            0.56*jetSize,0.94*jetSize,
            0.56*jetSize,0.88*jetSize,
            0.54*jetSize,0.965*jetSize,

            0.46*jetSize,0.965*jetSize,
            0.44*jetSize,0.88*jetSize,
            0.44*jetSize,0.94*jetSize,
            0.43*jetSize,0.94*jetSize,
            0.43*jetSize,0.955*jetSize,
            0.33*jetSize,0.955*jetSize,
            0.33*jetSize,0.895*jetSize,
            0.44*jetSize,0.81*jetSize,
            0.44*jetSize,0.715*jetSize,
            0.225*jetSize,0.715*jetSize,
            0.225*jetSize,0.75*jetSize,
            0.215*jetSize,0.75*jetSize,
            0.215*jetSize,0.56*jetSize,
            0.22*jetSize,0.55*jetSize,
            0.225*jetSize,0.56*jetSize,
            0.225*jetSize,0.615*jetSize,
            0.41*jetSize,0.49*jetSize,
            0.41*jetSize,0.44*jetSize,
            0.435*jetSize,0.35*jetSize,
            0.46*jetSize,0.17*jetSize,
            0.5*jetSize,0.05*jetSize

        ]
        
        self.jet=self.canvasWidget.create_polygon(flat_coordinates, fill="gray", outline="black")

    def moveJet(self,event,direction):
        if direction == "right":
            self.canvasWidget.move(self.jet, 30, 0)
        elif direction == "left":
            self.canvasWidget.move(self.jet, -30, 0)
        elif direction == "up":
            self.canvasWidget.move(self.jet, 0, -30)
        elif direction == "down":
            self.canvasWidget.move(self.jet, 0, 30)
        else:
            print("Wrong Direction")

    def flyRight(self,event):
        self.canvasWidget.move(self.jet, 30, 0)
    def flyLeft(self,event):
        self.canvasWidget.move(self.jet, -30, 0)
        
    
    def on_click(self, event):
        x = event.x
        y = event.y

        custom_x = x - 150 
        custom_y = 300 - y  
        print(f"Click: ({custom_x}, {custom_y})")


if __name__ == "__main__":
    app = App()
    app.mainloop()