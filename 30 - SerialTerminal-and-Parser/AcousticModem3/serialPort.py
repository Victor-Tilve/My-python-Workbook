#!/usr/bin/python3

import serial, time, sys, threading
from tkinter import ttk
import tkinter as tk

class SerialPort():
  def __init__(self, port:'str'= None, baud:'int'= 9600) -> None:
      # lock to serialize console output
      self.lock = threading.Lock()
      self.port = port
      self.baud = baud

      self.portconfig()

  def portconfig(self) -> None:
    self.ser = serial.Serial()
    self.ser.port = self.port
    self.ser.baudrate = self.baud
    self.ser.bytesize = serial.EIGHTBITS #number of bits per bytes
    self.ser.parity = serial.PARITY_NONE #set parity check: no parity
    self.ser.stopbits = serial.STOPBITS_ONE #number of stop bits
    #self.ser.timeout = None          #block read
    self.ser.timeout = 0            # non blocking read
    self.ser.xonxoff = False     #disable software flow control
    self.ser.rtscts = False     #disable hardware (RTS/CTS) flow control
    self.ser.dsrdtr = False       #disable hardware (DSR/DTR) flow control
    self.ser.writeTimeout = 2     #timeout for write

  def set_port(self,port:'str') -> None:
    self.port = port

  def open(self):
    try:
      self.ser.open()
    except Exception as e:
      print("<serialPort><func: open()>:error open serial port: " + str(e))

  # def read_serial(self,textReceived:'tk.Text()'):
  def read_serial(self):
    try:
      self.ser.open()
    except Exception as e:
      print("<serialPort><func: read_serial()>:error open serial port: " + str(e))
      exit()

    if self.ser.isOpen():
      print("<serialPort><func: read_serial()>:Checking if port is opened")
      try:
          while True:
              c = self.ser.read(size=1024)
              with self.lock:
                if len(c) > 0:
                  # textReceived.insert(tk.END,c)
                  sys.stdout.buffer.write(c) #TODO: implement Received


          self.ser.close()

      except Exception as e1:
          print ("error communicating...: " + str(e1))

    else:
      print("<serialPort><func: read_serial()>:cannot open serial port ")
      exit()

  def set_thread(self,textReceived:'tk.Text()'):#FIXME: No está funcionando
    # Create two threads as follows
    # self.textReceived = textReceived
    print("Inside Thread")
    try:
      t = threading.Thread(target=self.read_serial(textReceived), args=[self.ser])
      t.daemon = True  # thread dies when main thread (only non-daemon thread) exits.
      t.start()

    except:
      print("<serialPort><func: set_thread()>:Error: unable to start thread")    

  def isOpen(self):
    if self.ser.isOpen():
      return True
    else:
      return False
  
  def close(self):
    self.ser.close()


if __name__ == '__main__':
  serial = SerialPort('COM11',9600)
  serial.read_serial()



























# try:
#    while True:
#       pass
# except KeyboardInterrupt:
#    exit()