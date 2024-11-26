import random
import matplotlib.pyplot as plt #to plot th graph of winning and losing
account=0
x=[]
y=[]
#bet=int(input("Enter the bet amount from 1 to 10:"))
print("Playing game for one week")
for i in range(7):
    x.append(i+1)
    bet=random.randint(1,10)
    lucky_draw=random.randint(1,10)
    
    if bet==lucky_draw:
        account+=900-100
    else:
        account-=100
    y.append(account)
print("The amount after playing:",account)
plt.plot(x,y)
plt.show()

print("Playing game for one month")
for i in range(30):
    x.append(i+1)
    bet=random.randint(1,10)
    lucky_draw=random.randint(1,10)
    
    if bet==lucky_draw:
        account+=900-100
    else:
        account-=100
    y.append(account)
print("The amount after playing:",account)
plt.plot(x,y)
plt.show()

print("Playing game for one year")
for i in range(365):
    x.append(i+1)
    bet=random.randint(1,10)
    lucky_draw=random.randint(1,10)
    
    if bet==lucky_draw:
        account+=900-100
    else:
        account-=100
    y.append(account)
print("The amount after playing:",account)
plt.plot(x,y)
plt.show()
