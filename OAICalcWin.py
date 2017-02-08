#! /usr/bin/python

# OAI Port Calculator by Drew Dickenson 12-20-2016
#
# Useful for applications that need to know the OAI port number for
# integration with a Spectralink "Link 3000" series cabinet.
#
# Usage:  Enter Shelf, Slot, Port (1.3.1) each on its own line as prompted
# Ex: Please enter the shelf number: 1 <CR>
#     Please enter the slot  number: 3 <CR>
#     Please enter the port  number: 1 <CR>
	  

from Tkinter import *
import ttk
import os

shelf = 0
slot = 0
port = 0
OAI = 0

shelfval = 0
slotval = 0
portval = 0

def interface(text):
	print "\n"
	print "\n"
	print "     |------------------------------------------------------------------|"
	print "     |                                                                  |"
	print "     |                    OAI Port Number Calculator                    |"
	print "     |                                                                  |"
	print "%s" % (text)
	print "     |                                                                  |"
	print "     |------------------------------------------------------------------|"
	print "                                                                 DD-2016 "


os.system('cls')

interface("     |  1/3             Please enter the shelf number:                  |" )
shelf = int(raw_input())
os.system('cls')

interface ("     |  2/3             Please enter the slot  number:                  |")
slot = int(raw_input())
os.system('cls')

interface ("     |  3/3             Please enter the port  number:                  |")
port = int(raw_input())
os.system('cls')


if shelf == 1:
    shelfval = 0
elif shelf == 2:
    shelfval = 160
elif shelf == 3:
    shelfval = 320
elif shelf == 4:
    shelfval = 480
elif shelf == 5:
    shelfval = 640
elif shelf == 6:
    shelfval = 800
elif shelf == 7:
    shelfval = 960
elif shelf == 8:
    shelfval = 1120
elif shelf == 9:
    shelfval = 1280
elif shelf == 10:
    shelfval = 1440
elif shelf == 11:
    shelfval = 1600
elif shelf == 12:
    shelfval = 1760
elif shelf == 13:
    shelfval = 1920
elif shelf == 14:
    shelfval = 2080
elif shelf == 15:
    shelfval = 2240
elif shelf == 16:
    shelfval = 2400
elif shelf == 17:
    shelfval = 2560
elif shelf == 18:
    shelfval = 2720
elif shelf == 19:
    shelfval = 2880
elif shelf == 20:
    shelfval = 3040

    

if slot == 3:
    slotval = 0
elif slot == 4:
    slotval = 16
elif slot == 5:
    slotval = 32
elif slot == 6:
    slotval = 48
elif slot == 7:
    slotval = 64
elif slot == 8:
    slotval = 80
elif slot == 9:
    slotval = 96
elif slot == 10:
    slotval = 112
elif slot == 11:
    slotval = 128
elif slot == 12:
    slotval = 144

if port == 1:
    portval = 0
elif port == 2:
    portval = 1
elif port == 3:
    portval = 2
elif port == 4:
    portval = 3
elif port == 5:
    portval = 4
elif port == 6:
    portval = 5
elif port == 7:
    portval = 6
elif port == 8:
    portval = 7
elif port == 9:
    portval = 8
elif port == 10:
    portval = 9
elif port == 11:
    portval = 10
elif port == 12:
    portval = 11
elif port == 13:
    portval = 12
elif port == 14:
    portval = 13
elif port == 15:
    portval = 14
elif port == 16:
    portval = 15




OAI = shelfval + slotval + portval
interface ('     |                %d.%d.%d has an OAI port number of %d               |' % (shelf, slot, port, OAI) )
print "\n"
os.system ('pause')
