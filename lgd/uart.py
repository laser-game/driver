import serial
from serial.tools import list_ports

import time
import os
import log

class Uart(object):
    def __init__(self):
        """ initialization """
        self.name = 'CP2102'
        self.ser = serial.Serial()
        self.port = self.find_device()
        self.open_connection()

    def __del__(self):
        """ destructor """
        self.close_connection()

    def find_device(self):
        """ find port when is connected device """
        for dev in list_ports.comports():
            print(dev.description)
            if self.name in dev.description:
                return dev.device

        log.err(self.name + ' is not connected')
        exit(1)

    def open_connection(self):
        """ open connection """
        self.ser.port = self.port
        self.ser.baudrate = 115200
        self.ser.stopbits = serial.STOPBITS_ONE
        self.ser.parity = serial.PARITY_NONE
        self.ser.bytesize = serial.EIGHTBITS

        self.ser.timeout = 1.5 # in seconds
        try:
            self.ser.open()
            log.ok('port {} is open'.format(self.port))
        except serial.SerialException:
            log.err('port {} opening is fail'.format(self.port))
            exit(1)

    def close_connection(self):
        """ end connection """
        self.ser.close()
        log.ok('port is close')

    def read_byte(self):
        """ read one byte """
        tmp = self.ser.read(1)
        if tmp == b'':
            return None
        return int.from_bytes(tmp, byteorder='little', signed=False)

    def send_byte(self, byte):
        """ write one byte """
        self.ser.write(bytes((byte,)))
        time.sleep(0.01)

    def send_cmd(self, cmd):
        """ send command """
        if type(cmd) == str:
            for c in cmd:
                self.send_byte(ord(c))
            self.send_byte(ord('\n'))
            log.stdo('CMD: ' + log.colors.reset + cmd)

    # TODO add proces for read
