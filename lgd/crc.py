import numpy as np


class CRC32(object):
    def __init__(self,
                 gp: list = [32, 26, 23, 22, 16, 12, 11, 10, 8, 7, 5, 4, 2, 1]
                 ):
        self._generator_polynomial = sum(1 << i for i in gp) + 1
        self._table = tuple((self._calculate(i) for i in range(256)))

    def _calculate(self, byte: int) -> int:
        gp = np.uint64(self._generator_polynomial)

        MASK_MSB = np.uint64(0x8000000000)
        MASK_CRC = np.uint64(0x00FFFFFFFF)
        MASK_DATA = np.uint64(0xFF00000000)
        ONE = np.uint64(1)

        while not(gp & MASK_MSB):
            gp <<= ONE

        vector = np.uint64(byte) << np.uint64(32)
        mask_bit = MASK_MSB

        while (vector & MASK_DATA):
            if vector & mask_bit:
                vector ^= gp
            gp >>= ONE
            mask_bit >>= ONE

        return np.uint32(vector & MASK_CRC)

    def calculate(self, data) -> int:
        if type(data) is int:
            return int(self._table[data])

        elif type(data) is list or type(data) is tuple:
            CONST_0xFF = np.uint32(0xFF)
            CONST_0x08 = np.uint32(0x08)

            crc = np.uint32(~0)
            for i in data:
                crc = self._table[int((crc ^ np.uint32(i)) & CONST_0xFF)] ^ (
                    crc >> CONST_0x08)
            return int(~crc)

        return None


if __name__ == '__main__':
    crc = CRC32()
    print('{:08X}'.format(crc._generator_polynomial))
    print('{:08X}'.format(crc.calculate([7, 0, 10, 1, 2, 3])))
