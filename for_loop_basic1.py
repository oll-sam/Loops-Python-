#Basic - Print all integers from 0 to 150.
for i in range(0,15+1):
    print(i)
    
#Multiples of Five 
for x in range(5,100+1,5):
    print(x)
#Counting, the Dojo Way 
for j in range(0,100+1):
    if(j % 10 == 0):
        print("Coding Dojo")
    elif(j % 5 == 0):
        print("Coding")
    else:
        print(j)
#Whoa. That Sucker's Huge 
x = 0
for h in range(0,500000+1):
    if(h % 2 != 0):
        x += h 
print(x)
#Countdown by Fours 
for k in range(2018,1,-4):
    print(k)
#Flexible Counter
lowNum = 2
highNum = 55
mult = 6
for g in range(2,55):
    if(g % 6 ==0):
        print(g)