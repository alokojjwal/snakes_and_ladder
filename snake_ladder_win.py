snk = input("Enter the details of snakes and ladder: ").split(',')
scores = list(map(int,input("Enter the dice values: ").split(',')))
snk_ldr = {}
count = 0
for i in snk:
    t = i.split(':')
    snk_ldr[int(t[0])] = int(t[1])
for val in scores:
    count += val
    if count in snk_ldr:
        count = snk_ldr[count]
        
if count >= 100:
    print("Yes, This combination will win", end='')
else:
    print("No, This combination won't let win", end='')