import time

start_time = time.time()

def sum(lista):
    temp = list_1.pop()
    if len(lista) == 0:
        return temp
    else:                                                                       
        return sum(list_1) + temp

list_1 =  list(range(1,51))
print(sum(list_1))
print(f'--- {time.time() - start_time} seconds ---')