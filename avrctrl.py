#!/usr/bin/env python

import serial
import argparse
import time

# parse arguments
parser = argparse.ArgumentParser()
parser.add_argument('-d', dest='device', default='/dev/ttyUSB0')
parser.add_argument('-c', dest='all_off', default=False, action='store_true')
parser.add_argument('-o', dest='all_on',  default=False, action='store_true')
args = parser.parse_args()

ser = serial.Serial(args.device, baudrate=9600,
                    bytesize=8, parity='N', stopbits=1, timeout=None)

if args.all_off:
    ser.write('c')

time.sleep(1.0)

if args.all_on:
    ser.write('o')
