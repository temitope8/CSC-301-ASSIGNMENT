fib = DynamicArray(capacity=2)

a = 0
b = 1
fib.append(a)
fib.append(b)

for i in range(6):
    c = a + b
    fib.append(c)
    a = b
    b = c