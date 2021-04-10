import base64
pin = int(input("Enter Your PIN:"))
f = open("/home/yairko/Desktop/.scripts/.encodingsuni",'r+')
o = open("/home/yairko/Desktop/.scripts/.unipasswd",'w+')
if int(base64.b64decode(f.readline()).decode()) == pin:
    o.write(base64.b64decode(f.readline()).decode())
else:
    print('Wrong PIN! Exiting...')
    exit(1)
