# Author:   Raymond Harrison
#
# Purpose:  Create basic HTML file
#
# Tested:   ver 3.11.7 tested on Windows 11
#
#

import tkinter as tk
from tkinter import *
import webbrowser

# Making class for GUI
class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")
        # Create button for Default HTML page
        self.btn = Button(self.master, text="Default HTML Page", width = 30, height = 2, command=self.defaultHTML)
        self.btn.grid(row=3, column=1, padx=(10,10), pady=(10,10))

        # Create button for Custom Text to HTML page
        self.btn = Button(self.master, text="Submit Custom Text", width = 30, height = 2, command=self.customHTML)
        self.btn.grid(row=3, column=2, padx=(10,10), pady=(10,10))

        # Create input and Label text
        self.lbl_customText = tk.Label(self.master, text="Enter custom text or click the Default HTML page button.")
        self.lbl_customText.grid(row=0, column=0, padx=(30,10), pady=(10,10))
        self.customText = Entry(width = 130)
        self.customText.grid(row=1, column=0, columnspan=4)

    # Creating function to make HTML
    def defaultHTML(self):        
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html","w")
        htmlContect = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContect)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")


    # Creating function to make custom text HTML
    def customHTML(self):
        custom_HtmlText = self.customText.get()
        htmlFile = open("index.html","w")
        htmlCustom = "<html>\n<body>\n<h1>" + custom_HtmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlCustom)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")







if __name__ == '__main__':
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
