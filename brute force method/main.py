f = open('input.txt')
n = f.readline()
n = n.split(' ')
a = int(n[0])
b = int(n[1])
c = int(n[2])
d = int(n[3])
l = []

for x in range(-100, 101):
    if a * x**3 + b * x**2 + c * x + d == 0:
        l.append(x)
print(l)