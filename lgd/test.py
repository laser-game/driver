from uart import Uart

dev = Uart()
dev.process_rx_start()
dev.write('Hello word!')
dev.process_rx_join()
