import customtkinter as ctk
from PIL import ImageTk
import os
import random

class App(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.title("Space Blaster")
        self.geometry("-5-0")
        self.resizable(0, True)
        self.canvas_size = 800
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # Proper way to define CTkCanvas
        self.canvasWidget = ctk.CTkCanvas(self, width=self.canvas_size, height=self.canvas_size, bg="white")
        self.canvasWidget.grid(row=0, column=0)

        # Key and Mouse Bindings
        self.canvasWidget.bind("<Button-1>", self.on_click)
        self.bind('<Right>', self.flyRight)
        self.bind('<Left>', self.flyLeft)
        self.bind('<Up>', lambda event: self.moveJet(event, "up"))
        self.bind('<Down>', lambda event: self.moveJet(event, "down"))

        self.canvasWidget.focus_set()

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

        # Jet Shape Placeholder
        # self.jet = self.canvasWidget.create_rectangle(375, 375, 425, 425, fill="gray", outline="black")

        self.varSpawn = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.counter = 1
        self.objects = []

    def dajfn(self):
        self.after(3000, self.dajfn)
        for item in self.objects:
            self.moveScene(item)
    
    def moveJet(self, event, direction):
        move_map = {"right": (30, 0), "left": (-30, 0), "up": (0, -30), "down": (0, 30)}
        if direction in move_map:
            self.canvasWidget.move(self.jet, *move_map[direction])

    def flyRight(self, event):
        self.moveJet(event, "right")

    def flyLeft(self, event):
        self.moveJet(event, "left")

    def makeScene(self):
        obj = self.canvasWidget.create_rectangle(2, 2, 5, 5, fill="black")
        self.objects.append(obj)

    def moveScene(self, item):
        self.canvasWidget.move(item, 0, 30)
        self.objects.__delitem__(item)

    def on_click(self, event):
        x, y = event.x, event.y
        print(f"Click: ({x - 150}, {300 - y})")

        if random.choice(self.varSpawn) == 1 or 2 or 3 or 4 or 5:
            self.makeScene()
            self.counter += 1
        self.dajfn()

if __name__ == "__main__":
    app = App()
    app.mainloop()
