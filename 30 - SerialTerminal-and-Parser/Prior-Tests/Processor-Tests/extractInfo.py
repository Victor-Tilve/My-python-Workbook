#
#A demo of find() function
#


# src_str     = '00800 bits/sec\nMOD:05 ERR:000 SNR:27.1 AGC:07 SPD:+00.0 CCERR:014'    
def ver_1(src_str):
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