# from serial import LineReader
# from serial import ReaderThread
import serial
'''
En vez de instanciar directamente el objeto, llamo a una funcion que gestione los parametros del objeto desde un archivo de configuración
'''
ser = serial.Serial()
ser.baudrate = 9600
ser.port = 'COM11'
print(ser)
ser.open()
ser.write(b'Hello from python\n!')
# print(serial.tools.list_ports)


# class PrintLines(LineReader):
#     def connection_made(self, transport):
#         super(PrintLines, self).connection_made(transport)
#         sys.stdout.write('port opened\n')
#         self.write_line('hello world')

#     def handle_line(self, data):
#         sys.stdout.write('line received: {}\n'.format(repr(data)))

#     def connection_lost(self, exc):
#         if exc:
#             traceback.print_exc(exc)
#         sys.stdout.write('port closed\n')

# ser = serial.serial_for_url('loop://', baudrate=9600, timeout=1)
# with ReaderThread(ser, PrintLines) as protocol:
#     protocol.write_line('Hola')
#     time.sleep(2)
#     # protocol.write_line('hello')