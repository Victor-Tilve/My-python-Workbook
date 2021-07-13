# from processor import Processor
from serialProcessor import SerialPort,Processor
from modemTeledyme import ModemTeledyne
import sys
import time

import threading

status_configuration : bool = True

''' 
trying to calculate time for waiting xsegs for the answer
'''
from datetime import datetime

# print(str(threading.current_thread()))

# serialPort.Send('Hola, Terminal' + '\r\n')


#TODO: develope a status machine for waiting for the modem response. wait maximun 10 secs. 
#simulate "..." for giving a loading perspective
while True:
    start_time = datetime.now()
    # print('<test><While>:dentro del bucle')
    # print(f'<test><While>:processor._state = {processor._state}')
    # print(str(threading.current_thread()))
    try:
        if status_configuration:
            serialPort = SerialPort()
            port = "COM7"
            baud = 9600
            # Opening port
            serialPort.Open(port,baud)
            #intaciated processor
            processor = Processor()
            #Attaaching observer
            serialPort.attach(processor)
            #intaciated modem
            modem_teledyne = ModemTeledyne()
            #COnfigure modem
            modem_teledyne.configure_modem(serialPort=serialPort,procesor=processor)
            status_configuration = False
        elif not status_configuration:
            # print(f'<test><While>:lapse = {datetime.now() - start_time}')
            
            if processor.get_status_command_clam():#TODO: Implement time for waiting
                print('<test><While>:dentro del condicional \"get_status_command_clamget_status_command_clam\"')
                processor.set_status_command_clam(False)
            time.sleep(2)
    except KeyboardInterrupt:
        print("<test><while>: ", sys.exc_info()[0])
        serialPort.Close()
        serialPort.exit_thread()
        sys.exit(1)
    except: #COMEBACK: doi have to do this to differentiate keboard interupt from another error?
        print("<test><while>: ", sys.exc_info()[0])
        serialPort.Close()
        serialPort.exit_thread()
        sys.exit(1)
