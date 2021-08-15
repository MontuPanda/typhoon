print("Hello Folks - this is Grade 7 Ex 2 for Python")
print("---------------------------------------------")



def fib(n):
    fibs = [0, 1]
    for i in range(2,n+1):
        fibs.append(fibs[-1]+fibs[-2])
    return fibs

print(fib(50))  