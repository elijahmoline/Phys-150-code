# Write your code here :-)

# using colors from resistors
zero = (32, 32, 32)#black
one =(102, 51, 0) #brown
two =(255, 0, 0) #red
three = (255,128,0)#orange
four = (255,255,0)#yellow
five = (0,255,0)#green
six = (0,0,255)#blue
seven = (127,0,255) #violet
eight = (128,128,128)#grey
nine = (255,255,255)#white

ones = (num)%10
tens = (num/10)%10
hundreds = (num/100)%10
thousands = (num/1000)%10
tenthousands = (num/10000)%10

if i = 0:
    x=(zero)
if i = 1:
    x=(one)
if i =2:
    x=(two)
if i = 3:
    x=(three)
if i = 4:
    x=(four)
if i = 5:
    x=(five)
if i =6:
    x=(six)
if i = 7:
    x=(seven)
if i = 8:
    x=(eight)
if i = 9:
    x=(nine)

for i in range 10:
    if ones = i:
        cp.pixels[0]=x
for i in range 10:
    if tens = i:
        cp.pixels[1]=x
for i in range 10:
    if hundreds = i:
        cp.pixels[2]=x
for i in range 10:
    if thousands = i:
        cp.pixels[3]=x
for i in range 10:
    if tenthousands = i:
        cp.pixels[4]=x

