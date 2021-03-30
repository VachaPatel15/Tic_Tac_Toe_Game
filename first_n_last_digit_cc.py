x=int(input())
if(x>=1 and x<=1000):
    for i in range(x):
        y=(input())
        z=int(y[0])+int(y[len(y)-1])
        if(z>=1 and z<=1000000):
            print(z)
            


