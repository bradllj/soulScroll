import sys
import os

proc= os.popen('/usr/bin/zbarcam --prescale=300x300 -Sqrcode.enable', 'r')

def start_scan():
    global proc
    while True:
        print('Scanning')
        data = proc.readline()
        qrcode = str(data)[8:]
        if (qrcode):
            print(qrcode)

try:
    start_scan()
except KeyboardInterrupt:
    print('Stop')
finally:
    proc.close()
