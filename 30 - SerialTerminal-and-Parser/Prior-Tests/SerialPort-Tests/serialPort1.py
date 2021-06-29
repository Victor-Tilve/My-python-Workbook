import serial



serial_port = serial.Serial(baudrate = 9600,port = 'COM11')
serial_port.write(b'Hello from python!\r\n')

buffer = serial_port.read_until(expected='\n', size=None)


#TODO: implemnt read_until if I want to idntify the carry return (LF)
#TODO: Implement and axception when the port is already taken
