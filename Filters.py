from tkinter import *
from tkinter.ttk import Separator
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
import cv2 as cv
import os


class Filters(Frame):
    #Constructor
    def __init__(self, master = None, image = None):
        super().__init__(master)
        self.master = master

        # Add buttons
        self.button_sharpen = None
        self.button_blur = None
        self.button_contours = None

        # input image
        self.processed = image

        self.create_window()

    # Define window geometry
    def create_window(self):
        self.master.geometry('600x500')
        self.master.title("Filters window")
        #self.master.attributes("-fullscreen", True)
        #w, h = self.master.winfo_screenwidth(), self.master.winfo_screenheight()
        #self.master.geometry("%dx%d+0+0" % (w, h))
        #self.master.state('zoomed')
        self.master.resizable(True, True)
        # Add Filter button
        self.button_sharpen = Button(self.master, text="Sharpen", height=3, width=15, bd = 4, command=self.donothing)
        self.button_sharpen.place(relx=0.5, rely=0.05, relwidth=0.1, relheight=0.1)
        # Add Crop button
        self.button_blur = Button(self.master, text="Blur", height=3, width=15, bd = 4, command=self.blur)
        self.button_blur.place(relx=0.5, rely=0.17, relwidth=0.1, relheight=0.1)
        # Add Draw button
        self.button_contours = Button(self.master, text="Contours", height=3, width=15, bd = 4, command=self.contours)
        self.button_contours.place(relx=0.5, rely=0.29, relwidth=0.1, relheight=0.1)

    # TODO function
    def donothing(self):
        filewin = Toplevel(self.master)
        button = Button(filewin, text="TODO")
        button.pack()

    # Sharpen the image
    #def sharpen(self):

    # Blur the image
    def blur(self):
        self.processed = cv.GaussianBlur(self.processed, (7,7), 0)
        self.quit()

    # Convert the image to gray and draw contours
    def contours(self):
        self.processed = cv.Canny(self.processed , 150, 175)
        self.quit()
