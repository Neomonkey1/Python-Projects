#!/usr/bin/python
#-*- coding: utf-8 -*-
#
# Python Ver: 3.11.7
#
# Author: Raymond Harrison
#
# Purpose:  Phonebook Demo. Demonstrating OOP, Tkinter GUI module,
#           using Tkinter Parent and Child relationships.
#
# Tested OS: This code was written and tested to work with Windows 11.

import os
from tkinter import *
import tkinter as tk
import sqlite3

# Be sure to import our other modules
# so we can have access to them
import Phonebook_main
import Phonebook_gui


def center_window(self, w, h): # pass in the tkinter frame (master) reference and
    # the w and h get user's screen width and height
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    # calculate x and y coordinates to paint the app centered on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo

# catch if the user's clicks on the windows upper-right 'X' to ensure they want to close
def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        #This closes app
        self.master.destroy()
        os._exit(0)

#===========================================================================

def create_db(self):
    conn = sqlite3.connect('db_phonebook.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not exists tbl_phonebook( \
            ID INTERGER PRIMARY KEY AUTOINCREMENT, \
            col_fname TEXT, \
            col_lname TEXT, \
            col_fullname TEXT, \
            col_phone TEXT, \
            col_email TEXT \
            );")
        # You must commit() to save changes & close the database connection
        conn.commit()
    conn.close()
    first_run(self)

def first_run(self):
    conn = sqlite3.connect('db_phonebook.db')
    with conn:
        cur = conn.cursor()
        cur,count = count_records(cur)
        if count < 1:
            cur.execute("""INSERT INTO tbl_phonebook (col_fname,col_lname,col_fullname,col_phone,col_email) VALUES (?,?,?,?,?)""", ('John','Doe','John Doe','111-111-1111','jdoe@email.com'))
            conn.commit()
    conn.close()










if __name__ == '__main__':
    pass
