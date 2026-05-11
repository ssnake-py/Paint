import tkinter as tk
from tkinter import colorchooser, filedialog
from PIL import Image, ImageDraw, ImageTk
import random
import math

class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Paint - Python (Preview Fixed)")

        self.color = "black"
        self.brush_size = 5
        self.tool = "brush"  # brush | eraser | graffiti | line | rect | oval

        self.start_x = None
        self.start_y = None
        self.last_x = None
        self.last_y = None

        self.preview_id = None

        # TOP TOOLBAR
        self.toolbar = tk.Frame(root)
        self.toolbar.pack(fill=tk.X)

        tk.Button(self.toolbar, text="Brush", command=lambda: self.set_tool("brush")).pack(side=tk.LEFT)
        tk.Button(self.toolbar, text="Eraser", command=lambda: self.set_tool("eraser")).pack(side=tk.LEFT)
        tk.Button(self.toolbar, text="Graffiti", command=lambda: self.set_tool("graffiti")).pack(side=tk.LEFT)
        tk.Button(self.toolbar, text="Line", command=lambda: self.set_tool("line")).pack(side=tk.LEFT)
        tk.Button(self.toolbar, text="Rect", command=lambda: self.set_tool("rect")).pack(side=tk.LEFT)
        tk.Button(self.toolbar, text="Oval", command=lambda: self.set_tool("oval")).pack(side=tk.LEFT)

        tk.Button(self.toolbar, text="Color", command=self.choose_color).pack(side=tk.LEFT)
        tk.Button(self.toolbar, text="Clear", command=self.clear_canvas).pack(side=tk.LEFT)
        tk.Button(self.toolbar, text="Save", command=self.save_image).pack(side=tk.LEFT)
        tk.Button(self.toolbar, text="Import", command=self.import_image).pack(side=tk.LEFT)

        self.size_slider = tk.Scale(self.toolbar, from_=1, to=50, orient=tk.HORIZONTAL, label="Size")
        self.size_slider.set(self.brush_size)
        self.size_slider.pack(side=tk.LEFT)

        # CANVAS
        self.canvas = tk.Canvas(root, bg="white", width=900, height=600)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.canvas.bind("<ButtonPress-1>", self.start)
        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.release)

        # IMAGE BUFFER
        self.image = Image.new("RGB", (900, 600), "white")
        self.draw = ImageDraw.Draw(self.image)

        self.bg_tk_image = None

    def set_tool(self, tool):
        self.tool = tool

    def choose_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.color = color
            self.tool = "brush"

    def clear_canvas(self):
        self.canvas.delete("all")
        self.image = Image.new("RGB", (900, 600), "white")
        self.draw = ImageDraw.Draw(self.image)

    def save_image(self):
        file = filedialog.asksaveasfilename(defaultextension=".png")
        if file:
            self.image.save(file)

    def import_image(self):
        file = filedialog.askopenfilename(filetypes=[("Images", "*.png *.jpg *.jpeg *.bmp")])
        if not file:
            return

        img = Image.open(file).convert("RGB").resize((900, 600))
        self.image.paste(img)
        self.draw = ImageDraw.Draw(self.image)

        self.bg_tk_image = ImageTk.PhotoImage(img)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.bg_tk_image)

    # EVENTS
    def start(self, event):
        self.start_x = event.x
        self.start_y = event.y
        self.last_x = event.x
        self.last_y = event.y

    def paint(self, event):
        self.brush_size = self.size_slider.get()
        x, y = event.x, event.y

        if self.tool == "brush":
            self.draw_line(self.last_x, self.last_y, x, y, self.color)
            self.last_x, self.last_y = x, y

        elif self.tool == "eraser":
            self.draw_line(self.last_x, self.last_y, x, y, "white")
            self.last_x, self.last_y = x, y

        elif self.tool == "graffiti":
            self.draw_graffiti(x, y)

        elif self.tool in ("line", "rect", "oval"):
            self.draw_preview(x, y)

    def release(self, event):
        x, y = event.x, event.y

        if self.preview_id:
            self.canvas.delete(self.preview_id)
            self.preview_id = None

        if self.tool == "line":
            self.draw_line(self.start_x, self.start_y, x, y, self.color)
        elif self.tool == "rect":
            self.draw_rectangle(self.start_x, self.start_y, x, y)
        elif self.tool == "oval":
            self.draw_oval(self.start_x, self.start_y, x, y)

        self.last_x = None
        self.last_y = None

    # PREVIEW FIXED (VISIBLE ALWAYS)
    def draw_preview(self, x, y):
        if self.preview_id:
            self.canvas.delete(self.preview_id)

        preview_color = "#888888"  # zawsze widoczne

        if self.tool == "line":
            self.preview_id = self.canvas.create_line(
                self.start_x, self.start_y, x, y,
                fill=preview_color,
                width=self.brush_size,
                dash=(6, 3)
            )

        elif self.tool == "rect":
            self.preview_id = self.canvas.create_rectangle(
                self.start_x, self.start_y, x, y,
                outline=preview_color,
                width=self.brush_size,
                dash=(6, 3)
            )

        elif self.tool == "oval":
            self.preview_id = self.canvas.create_oval(
                self.start_x, self.start_y, x, y,
                outline=preview_color,
                width=self.brush_size,
                dash=(6, 3)
            )

    # DRAW HELPERS
    def draw_line(self, x1, y1, x2, y2, color):
        self.canvas.create_line(x1, y1, x2, y2, width=self.brush_size, fill=color, capstyle=tk.ROUND)
        self.draw.line([x1, y1, x2, y2], fill=color, width=self.brush_size)

    def draw_rectangle(self, x1, y1, x2, y2):
        self.canvas.create_rectangle(x1, y1, x2, y2, outline=self.color, width=self.brush_size)
        self.draw.rectangle([x1, y1, x2, y2], outline=self.color, width=self.brush_size)

    def draw_oval(self, x1, y1, x2, y2):
        self.canvas.create_oval(x1, y1, x2, y2, outline=self.color, width=self.brush_size)
        self.draw.ellipse([x1, y1, x2, y2], outline=self.color, width=self.brush_size)

    def draw_graffiti(self, x, y):
        radius = 20
        for _ in range(25):
            angle = random.uniform(0, 2 * math.pi)
            r = random.uniform(0, radius)
            px = int(x + math.cos(angle) * r)
            py = int(y + math.sin(angle) * r)

            self.canvas.create_oval(px, py, px+2, py+2, fill=self.color, outline=self.color)
            self.draw.point((px, py), fill=self.color)

if __name__ == "__main__":
    root = tk.Tk()
    app = PaintApp(root)
    root.mainloop()
