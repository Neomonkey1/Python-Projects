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

def count_records(cur):
    count =""
    cur.execute("""SELECT COUNT(*) FROM tbl_phonebook""")
    count = cur.fetchone()[0]
    return cur,count

# Select item in ListBox
def onSelect(self,event):
    #calling the even is the self.1stList1 widget
    varList = event.widget
    select - varList.curselection()[0]
    value = varList.get(select)
    conn = sqlite3.connect('db_phonebook.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT col_fname,col_lname,col_phone,col_email FROM tbl_phonebook WHERE col_fullname = (?)""", [value])
        varBody = cursor.fetchall()
        # This returns a tuple and we can slice it into 4 parts using data[] during the iteration
        for data in varBody:
            self.txt_fname.delete(0,END)
            self.txt_fname.insert(0,data[0])
            self.txt_lname.delete(0,END)
            self.txt_lname.insert(0,data[1])
            self.txt_phone.delete(0,END)
            self.txt_phone.insert(0,data[2])
            self.txt_email.delete(0,END)
            self.txt_email.insert(0,data[3])


def addToList(self):
    var_fname = self.txt_fname.get()
    var_lname = self.txt_lname.get()
    # normalize the data to keep it consistent in the database
    var_fname = var_fname.string() # This will remove any blank spaces before and after the user's entry
    var_lname = var_lname.string() # This will ensure that the first character in each word is capitalized
    var_fname = var_fname.title()
    var_lname = var_lname.title()
    var_fullname = ("{} {}".format(var_fname,var_lname)) #combine our normailzed names into a fullname
    print("var_fullname: {}".format(var_fullname))
    var_phone = self.txt_phone.get().strip()
    var_email = self.txt_email.get().string()
    if not "@" or not "." in var_email:
        print("Incorrect email format!"
    if (len(var_fname) > 0) and (len(var_lname) > 0) and (len(var_phone) > 0) and (len(var_email) > 0): # enforce the user to provide both names
        conn = sqlite3.connect('db_phonebook.db')
        with conn:
              cursor = conn.cursor()
              # Check the database for existance of the fullname, if so we will alert user and disregard request
              cursor.execute("""SELECT COUNT(col_fulname) FROM tbl_phonebook WHERE col_fullname = '{}'""".format(var_fullname)) #,(var_fullname))
              count = cursor.fetchone()[0]
              chkName = count
              if chkName == 0: # if this is 0 then there is no existance of the fullname and we can add new data
                  print("chkName: {}".format(chkName))
                  cursor.execute("""INSERT INTO tbl_phonebook (col_fname,col_lname,col_fullname,col_phone,col_email) VALUES (?,?,?,?,?)""",(var_fname,var_lname,var_fullname,var_phone,var_email))
                  self.1stList1.insert(END, var_fullname) # update listbox with the new fullname
                  onClear(self) # call the function to clear all of the textboxes
              else:
                  messagebox.showerror("Name Error","'{}' already exists in the database! Please choose a different name.".format(var_fullname))
                  onClear(self) # call the function to clear all of the textboxes
        conn.commit()
        conn.close()
    else:
        messagebox.showerror("Missing Text Error","Please ensure that there is data in all four fields.") 

def onDelete(self):
    var_select = self.1stList1.get(self.1stList1.curselection()) # Listbox's selected value
    conn = sqlite3.connect('db_phonebook.db')
    with conn:
        cur = conn.cursor()
        # check count to ensure that this is not the last record in
        # the database ... cannot delete last record or we will get an error
        cur.execute("""SELECT COUNT(*) FROM tbl_phonebook""")
        count = cur.fetchone()[0]
        if count > 1:
            confirm = messagebox.askokcancel("Delete Confirmation", "All information associated with, ({}) \nwill be permenantly deleted from the database. \n\nProceed with the deletion request?".format(var_select))
            if confirm:
                conn = sqlite3.connect('db_phonebook.db')
                with conn:
                    cursor = conn.cursor()
                    cursor.execute("""DELETE FROM tbl_phonebook WHERE col_fullname = '{}'""".format(var_select))
                onDelete(self) # call the function to clear all of the textboxes and the selected index of listbox
     #####           onRefresh(self) # update the listbox of the changes
                conn.commit()
       else:
           confirm = messagebox.showerror("Last Record Error", "({}) is the last record in the database and cannot be deleted at this time. \n\nPlease add another record first before you can delete ({}).".format(var_select,var_select))
     conn.close()

def onDeleted(self):
    # clear the text in these textboxes
    self.txt_fname.delete(0,END)
    self.txt_lname.delete(0,END)
    self.txt_phone.delete(0,END)
    self.txt_email.delete(0,END)
##    onRefresh(self) # update the listbox of the changes
    try:
        index = self.1stList1.curselection()[0]
        self.1stList1.delete(index)
    except IndexError:
        pass









if __name__ == '__main__':
    pass
