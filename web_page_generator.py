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
        # Creates button for Default HTML page
        self.btn = Button(self.master, text="Default HTML Page", width = 30, height = 2, command=self.defaultHTML)
        self.btn.grid(row=3, column=3, padx=(10,10), pady=(10,10))

        # Creates button for Custom Text to HTML page
        self.btn = Button(self.master, text="Submit Custom Text", width = 30, height = 2)
        self.btn.grid(row=3, column=4, padx=(10,10), pady=(10,10))

    # Creating function to make HTML
    def defaultHTML(self):        
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html","w")
        htmlContect = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContect)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")









if __name__ == '__main__':
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
