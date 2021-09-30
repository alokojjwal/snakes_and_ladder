snk = input("Enter the details of snakes and ladder: ").split(',')
snk_ldr = {}
snake = 0
ladder = 0
for i in snk:
    t = i.split(':')
    snk_ldr[int(t[0])] = int(t[1])
for i,j in snk_ldr.items():
    if i<j:
        ladder+=1
    else:
        snake+=1
print("The number of snakes are:",snake,"and the number of ladders are:",ladder)