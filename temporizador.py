import time
t = input("Digite o tempo(em segundos):")

if t.isdigit():
    t = int(t)

else:
    print("Entrada inválida")
    quit()

while t: #!= 0: # 0 ---> false | 1,2 ..... > True
    minutes, seconds = divmod(t,60)
    timer = "{02d}:{02d}".format(minutes,seconds)        
     ## f{minutes}: {seconds}#
    print(timer,end="\r")
    time.sleep(1)

    t = t - 1

print ("O tempo acabou!!")
