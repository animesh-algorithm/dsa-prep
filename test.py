a=2
b=4
c=6
lcm = a
if b>a:
    lcm=b
if c>lcm:
    lcm=c
while True:
    if lcm%a==0 and lcm%b==0 and lcm%c==0:
        break
    lcm+=1
print(lcm)