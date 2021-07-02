str_temp = "# +++\r\nCommand '+++' not found\r\nError\r\n"

int_var = str_temp.find(">")
if int_var != -1:
    print(int_var)
else:
    print('Didn\'t found')