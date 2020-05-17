#!/usr/bin/env python3
import time
import serial

print("running")
s = serial.Serial('/dev/serial0', 9600)

#Write all digits
s.write(str.encode('0123456789'))

# Write carriage return(13) and newline(10)
s.write(str.encode('\r\n'))


