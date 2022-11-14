valid_code = int(123)

#class MyExecpt(Exception):
    #print ('myexce')

#try:
    #pass
    #aa = int('b')

while True:
    code = input("Insert the code: ")
    try:
        conv_code = int(code)
    except ValueError as e:
        print("The code has to be a number!")
        #raise MyExecpt(e)
        continue
    if int(code) == int(valid_code):
        print('OK')
        break

#except MyExecpt:
#    print("Except: The code has to be a number!")
#    continue