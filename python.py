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
        canvas=100
        flat_coordinates = [
            0.5*canvas,0.05*canvas,
            0.54*canvas,0.17*canvas,
            0.565*canvas,0.35*canvas,
            0.59*canvas,0.44*canvas,
            0.59*canvas,0.49*canvas,
            0.775*canvas,0.615*canvas,
            0.775*canvas,0.56*canvas,
            0.78*canvas,0.55*canvas,
            0.785*canvas,0.56*canvas,
            0.785*canvas,0.75*canvas,
            0.775*canvas,0.75*canvas,
            0.775*canvas,0.715*canvas,
            0.56*canvas,0.715*canvas,
            0.56*canvas,0.81*canvas,
            0.67*canvas,0.895*canvas,
            0.67*canvas,0.955*canvas,
            0.57*canvas,0.955*canvas,
            0.57*canvas,0.94*canvas,
            0.56*canvas,0.94*canvas,
            0.56*canvas,0.88*canvas,
            0.54*canvas,0.965*canvas,

            0.46*canvas,0.965*canvas,
            0.44*canvas,0.88*canvas,
            0.44*canvas,0.94*canvas,
            0.43*canvas,0.94*canvas,
            0.43*canvas,0.955*canvas,
            0.33*canvas,0.955*canvas,
            0.33*canvas,0.895*canvas,
            0.44*canvas,0.81*canvas,
            0.44*canvas,0.715*canvas,
            0.225*canvas,0.715*canvas,
            0.225*canvas,0.75*canvas,
            0.215*canvas,0.75*canvas,
            0.215*canvas,0.56*canvas,
            0.22*canvas,0.55*canvas,
            0.225*canvas,0.56*canvas,
            0.225*canvas,0.615*canvas,
            0.41*canvas,0.49*canvas,
            0.41*canvas,0.44*canvas,
            0.435*canvas,0.35*canvas,
            0.46*canvas,0.17*canvas,
            0.5*canvas,0.05*canvas

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