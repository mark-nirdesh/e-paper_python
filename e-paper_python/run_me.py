# !/usr/bin/python
# !/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import sys
import tkinter.messagebox
from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk
from tkinter.messagebox import showinfo

picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from lib.waveshare_epd import epd5in65f
from PIL import Image

logging.basicConfig(level=logging.DEBUG)

file_title = ''

root = Tk()
root.title("Integrating with e-paper")
root.resizable(True, True)
root.geometry('400x150')

text = ''
def select_file(file_types=(
        ('bmp files', '.bmp'),
        ('All files', '*.*')
)):
    filename = fd.askopenfilename(
        title='Select a BMP image',
        initialdir='//home//pi//Desktop//sfsdf//pic',
        filetypes=file_types)

   # showinfo(

       # title='Image is selcted to write on e-paper',
    tkinter.messagebox.showinfo("Progression pop-up", "Click OK and wait till image is uploaded on e-paper")
        
   # )
    print('inside upload fn', filename, type(filename))
    file_title = filename
    return file_title


def upload_bmp():
    file_title = select_file()
    
    if file_title is not None:

        print('b4 try', file_title)

        try:
            print('in try', file_title)

            logging.info("epd5in65f Demo")

            epd = epd5in65f.EPD()
            logging.info("init and Clear")
            epd.init()
            epd.Clear()

            
            print(epd)
            logging.info("3.read bmp file")
            # Himage <PIL.BmpImagePlugin.BmpImageFile image mode=RGB size=600x448 at 0x7F8D1543A0>

            Himage = Image.open(file_title)
            print('himage', Himage)
            epd.display(epd.getbuffer(Himage))

            logging.info("Goto Sleep...")
            epd.sleep()
            tkinter.messagebox.showinfo("Progression pop-up", "Your image is uploaded.")
 
        except IOError as e:
            logging.info(e)

        except KeyboardInterrupt:
             logging.info("ctrl + c:")
             epd5in65f.epdconfig.module_exit()
             exit()





        

    else:
        tkinter.messagebox.showinfo("last else.", "if file_name is null")



# 1 open button
# open_button = ttk.Button(
#   root,
#  text='Select the BMP image',
#   command=
# )

# open_button.pack(expand=True)

# 2. upload button
print('b4 button', file_title)
upload_button = ttk.Button(
    root,
    text='Upload the BMP image to e-paper',
    command=upload_bmp
)

upload_button.pack(expand=True)

root.mainloop()




