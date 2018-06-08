from crc import CRC32
from uart import UART
from time import sleep

PACKET_SIZE_MIN = 8
PACKET_SIZE_MAX = 512
PACKET_SIZE_HEAD = 3
PACKET_SIZE_CRC = 4
PACKET_SIZE_INFO = PACKET_SIZE_HEAD + PACKET_SIZE_CRC


class Packet(object):
    def __init__(self, ser: UART, crc: CRC32, address: int = 0):
        self.crc = crc
        self.ser = ser
        self._address = address
        self._data = []
        self._stream = []

    def set_address(self, address: int):
        self._address = address

    def get_address(self) -> int:
        return self._address

    def set_data(self, data: list):
        self._data = data

    def get_data(self) -> list:
        return self._data

    def set_stream(self, stream: list):
        self._stream = stream

    def get_stream(self) -> list:
        return self._stream

    def create(self, data: list = []) -> list:
        if len(data) > 0:
            self._data = data

        self._stream = []
        self._stream.append(self._address)

        size = len(self._data) + PACKET_SIZE_INFO
        self._stream.append((size >> 8) & 0xFF)
        self._stream.append((size >> 0) & 0xFF)

        self._stream += self._data

        crc = self.crc.calculate(self._stream)
        self._stream.append((crc >> 24) & 0xFF)
        self._stream.append((crc >> 16) & 0xFF)
        self._stream.append((crc >> 8) & 0xFF)
        self._stream.append((crc >> 0) & 0xFF)

        return self._stream

    def tx(self):
        for i in self._stream:
            self.ser.send_byte(i)
        sleep(0.005)
