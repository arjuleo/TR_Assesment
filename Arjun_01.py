N=int(input("Enter a number: "))
y=[0]
b=1
for i in range (N):
    b=b+y[i-1]
    y.append(b)
print(y)
