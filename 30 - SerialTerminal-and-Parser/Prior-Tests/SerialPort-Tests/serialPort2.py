import serial
def main():
    ser = serial.Serial(
        port='COM11',
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS)
    ser.timeout=5
    ser.write("OUTP? 1 \r\n".encode()) #Asks the Lock-in for x-value
    ser.write("++read\r\n".encode())

    while True:
        buffer = ""
        print("send another massege\n")
        while True:
            oneByte = ser.read(1)
            if oneByte == b"\r":    #method should returns bytes
                print (buffer)
                ser.write("Received\r\n".encode())
                break
            else:
                buffer += oneByte.decode()
if __name__ == '__main__': main()