import time

'''
I'll define as much as functions as commands to decode
'''

# src_str     = '00800 bits/sec\nMOD:05 ERR:000 SNR:27.1 AGC:07 SPD:+00.0 CCERR:014'   


############# Send command functions #############

# +++#CR#LFCommand '+++' not found#CR#LFError#CR#LF
# +++#CR#LFuser:145>
# +++CONNECT 00800 bits/sec#CR#LF#CR#LFuser:147>


def commandMode():
    serial.print('+++\r\n') #COMEBACK: Implementar esto con el objeto serial del programa principal
    src_str = serial.read() 
    sub_index   = src_str.find('>')
    if sub_index != -1:
        return True
    else:
        sub_index   = src_str.find('Command')
        
        if sub_index != -1:
            print('<checkCommandMode>: Command mode activo')
            return True
        else:
            print('<checkCommandMode>: No se estabeció comunicacion con modem')
            return False

#+++CONNECT 00800 bits/sec#CR#LF#CR#LFuser:122>at#CR#LFOK#CR#LFuser:123>atl#CR#LF#CR#LFuser:124>Lowpower#CR#LF+++CONNECT 00800 bits/sec#CR#LF#CR#LFuser:124>at#CR#LFOK#CR#LFuser:125>atl#CR#LF#CR#LFuser:126>Lowpower#CR#LF+++CONNECT 00800 bits/sec#CR#LF#CR#LFuser:126>at#CR#LFOK#CR#LFuser:127>atl#CR#LF#CR#LFuser:128>Lowpower#CR#LF+++CONNECT 00800 bits/sec#CR#LF#CR#LFuser:128>at#CR#LFOK#CR#LFuser:129>atl#CR#LF#CR#LFuser:130>Lowpower#CR#LF
#+++CONNECT 00800 bits/sec#CR#LF#CR#LFuser:147>




#TODO: Debo importar el objeto externo "serial" para poder leer y enviar comandos desde acá
#This function works after an if when you check commmand mode is started(after commandMode) 
def sentCommand(command):
    serial.print(command + '\r\n')#COMEBACK: implement serial object
    
# user:87>ATL#CR#LF#CR#LF#CR#LFuser:88>Lowpower#CR#LF
# user:89>ATL#CR#LF#CR#LF#CR#LFuser:90>Lowpower#CR#LF
def closeCommandLow() -> bool:
    serial.print('ATL\r\n') #COMEBACK: implement serial object
    src_str = serial.read() 
    sub_index   = src_str.find('Lowpower')
    if sub_index != -1:
        return True
    else:
        return False

def closeCommandOnline() -> bool:
    serial.print('ATO\r\n') #COMEBACK: implement serial object
    src_str = serial.read() 
    sub_index   = src_str.find('Lowpower')
    if sub_index != -1:
        return True
    else:
        return False







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

def AT(cmd_answer:'str'):
    # user:10>AT#CR#LF#CR#LFOK#CR#L











if __name__ == "__main__":
    src_str     = '00800 bits/sec\nMOD:05 ERR:000 SNR:27.1 AGC:07 SPD:+00.0 CCERR:014'    
    ver_1(src_str)