import time

'''
I'll define as much as functions as commands to decode
'''
# src_str     = '00800 bits/sec\nMOD:05 ERR:000 SNR:27.1 AGC:07 SPD:+00.0 CCERR:014'   



#+++CONNECT 00800 bits/sec#CR#LF#CR#LFuser:122>at#CR#LFOK#CR#LFuser:123>atl#CR#LF#CR#LFuser:124>Lowpower#CR#LF+++CONNECT 00800 bits/sec#CR#LF#CR#LFuser:124>at#CR#LFOK#CR#LFuser:125>atl#CR#LF#CR#LFuser:126>Lowpower#CR#LF+++CONNECT 00800 bits/sec#CR#LF#CR#LFuser:126>at#CR#LFOK#CR#LFuser:127>atl#CR#LF#CR#LFuser:128>Lowpower#CR#LF+++CONNECT 00800 bits/sec#CR#LF#CR#LFuser:128>at#CR#LFOK#CR#LFuser:129>atl#CR#LF#CR#LFuser:130>Lowpower#CR#LF
def checkLocalConnection(src_str):
    #Message expectec:  CONNECT 00800 bits/sec#CR#LF
    sub_index   = src_str.find('CONNECT')
    baud        = src_str[sub_index + 8:sub_index + 13]
    status      = src_str[sub_index:sub_index + 7]
    if status == 'CONNECT':
        return True
    else:
        print('<ATD5>: No se estabeció comunicacion con modem remoto')

#TODO: Debo importar el objeto externo "serial" para poder leer y enviar comandos desde acá
def sentCommand(command):
    serial.print('+++\r\n')
    src_str = serial.read()
    status = checkLocalConnection(src_str) 
    # time.sleep(100) #Calibrate the time
    if status:
        serial.print('command\r\n')
    else:
        print('<sentCommand>: No se estabeció comunicacion con modem Local') #TODO: what would the program response if this happens?
#close communication with local modem - Local modem in low power
def closeCommunication():
    serial.print('ATL\r\n') #COMEBACK: adsgsdgsdfgsdhd
    







#   
def ATX(src_str):
    sub_index   = src_str.find('MOD:')
    MOD         = src_str[sub_index + 4:sub_index + 6]
    sub_index   = src_str.find('ERR:')
    ERR         = src_str[sub_index + 4:sub_index + 7]
    sub_index   = src_str.find('SNR:')
    SNR         = src_str[sub_index + 4:sub_index + 8]
    sub_index   = src_str.find('AGC:')
    AGC         = src_str[sub_index + 4:sub_index + 6]
    sub_index   = src_str.find('SPD:')
    SPD         = src_str[sub_index + 4:sub_index + 9]
    sub_index   = src_str.find('CCERR:')
    CCERR       = src_str[sub_index + 6:sub_index + 9]

    print(f'el valor de MOD es: {MOD}')
    print(f'el valor de ERR es: {ERR}')
    print(f'el valor de SNR es: {SNR}')
    print(f'el valor de AGC es: {AGC}')
    print(f'el valor de SPD es: {SPD}')
    print(f'el valor de CCERR es: {CCERR}')

if __name__ == "__main__":
    src_str     = '00800 bits/sec\nMOD:05 ERR:000 SNR:27.1 AGC:07 SPD:+00.0 CCERR:014'    
    ver_1(src_str)