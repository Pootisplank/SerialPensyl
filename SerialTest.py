#!/usr/bin/env python3
import time
import serial

print("running")
s = serial.Serial('/dev/serial0', 9600)

# Write newline character (ascii 10) to the serial port
s.write(str.encode('\n'))


# Write carriage return (ascii 13) to the serial port
s.write(str.encode('\r'))


# Write ints to serial
s.write(49)


