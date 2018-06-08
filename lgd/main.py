#!/usr/bin/env python

import threading
from uart import UART
from crc import CRC32
from packet import Packet
from time import sleep


def read():
    print('reading thread run')

    while True:
        rx_byte = ser.read_byte()
        if type(rx_byte) is int:
            uart_rx_callback(rx_byte)


def uart_rx_callback(rx_byte):
    print(chr(rx_byte), end='')


if __name__ == '__main__':
    ser = UART(port='/dev/ttyUSB0')
    crc = CRC32()
    packet = Packet(ser, crc, address=2)

    thread = threading.Thread(target=read)
    thread.start()

    while True:
        packet.create([0, 0, 0])
        packet.tx()
        packet.create([50, 0, 0])
        packet.tx()
        packet.create([100, 0, 0])
        packet.tx()
        packet.create([150, 0, 0])
        packet.tx()
        packet.create([200, 0, 0])
        packet.tx()
        packet.create([250, 0, 0])
        packet.tx()
        packet.create([200, 0, 0])
        packet.tx()
        packet.create([150, 0, 0])
        packet.tx()
        packet.create([100, 0, 0])
        packet.tx()
        packet.create([50, 0, 0])
        packet.tx()
        packet.create([0, 0, 0])
        packet.tx()

        packet.create([0, 0, 0])
        packet.tx()
        packet.create([0, 50, 0])
        packet.tx()
        packet.create([0, 100, 0])
        packet.tx()
        packet.create([0, 150, 0])
        packet.tx()
        packet.create([0, 200, 0])
        packet.tx()
        packet.create([0, 250, 0])
        packet.tx()
        packet.create([0, 200, 0])
        packet.tx()
        packet.create([0, 150, 0])
        packet.tx()
        packet.create([0, 100, 0])
        packet.tx()
        packet.create([0, 50, 0])
        packet.tx()
        packet.create([0, 0, 0])
        packet.tx()

        packet.create([0, 0, 0])
        packet.tx()
        packet.create([0, 0, 50])
        packet.tx()
        packet.create([0, 0, 100])
        packet.tx()
        packet.create([0, 0, 150])
        packet.tx()
        packet.create([0, 0, 200])
        packet.tx()
        packet.create([0, 0, 250])
        packet.tx()
        packet.create([0, 0, 200])
        packet.tx()
        packet.create([0, 0, 150])
        packet.tx()
        packet.create([0, 0, 100])
        packet.tx()
        packet.create([0, 0, 50])
        packet.tx()
        packet.create([0, 0, 0])
        packet.tx()
