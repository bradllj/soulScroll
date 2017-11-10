#!/usr/bin/python 

import os
import cups

conn = cups.Connection()
printers = conn.getPrinters()
for printer in printers:
	print printer
#conn.printFile("soul_print", "/home/chip/prayerTest.txt", "test", {})
conn.printFiles("soul_print", ["/home/chip/H1Qrcode.jpg", "/home/chip/deathQr.png"], "image", {})
