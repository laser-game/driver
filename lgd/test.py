from uart import Uart

dev = Uart()
dev.send_cmd('Hello word!')
