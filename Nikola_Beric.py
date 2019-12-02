import math

n = int(input ("Enter number of polygon edges: "))



while n < 3:
    n = int(input("Please insert a value higher than two: "))

i = 0 
x = []
y = []


while i < n:
    i = i + 1
    x.append (int(input(f"input coordinate x{i}: ")))
    y.append (int(input(f"input coordinate y{i}: ")))
   

print(f"{'n':>3} {'x':>7} {'y':>7}")
print("_" * 26)





b = 0
c = 0
j = 0
A = 0
Sx = 0
Sy = 0
Ix = 0
Iy = 0
Ixy = 0

for b in range(0,n):
    c = c + 1
    print(f"{'n'} {c}   {x[b]:.2f}   {y[b]:.2f}")

while j < (n - 1):

    A = 1 / 2 * ((x [j + 1] + x[j]) * (y [j + 1] - y [j])) + A

    Sx = - 1 /6 * (x [j + 1] - x [j]) * (y[j+1] **2 + y [j] * y [j+1] + y[j] **2) + Sx
    Sy = 1 / 6 * (y [j + 1] - y [j]) * (x[j+1] **2 + x [j] * x [j+1] + x[j] **2) + Sy

    Ix = - 1 / 12 * (x[j+1] - x[j]) * (y[j+1] **3 + y[j+1] **2 * y[j] + y[j+1] * y[j] **2 + y[j] **3 ) + Ix
    Iy = 1 / 12 * (y[j+1] - y[j]) * (x[j+1] **3 + x[j+1] **2 * x[j] + x[j+1] * x[j] **2 + x[j] **3 ) + Iy
    Ixy = - 1 / 24 * (y[j+1] - y[j]) * ((y[j+1] * (3 * x[j+1] **2 + 2 * x[j+1] * x[j] + x[j] **2)) + (y[j] * (3 * x[j+1] **2 + 2 * x[j+1] * x[j] + x[j] **2))) + Ixy
    j = j + 1


Xt = Sy / A 
Yt = Sx / A 
Ixt = Ix - Yt **2 * A 
Iyt = Iy - Xt **2 * A 
Ixyt = Ixy + Xt * Yt * A 



print("_" * 26)

print ("Geometric characteristics: ")


print (f"{'A: ':10} {A:>5.2f}")
print (f"{'Sx: ':10} {Sx:>5.2f}")
print (f"{'Sy: ':10} {Sy:>5.2f}")
print (f"{'Ix: ':10} {Ix:>5.2f}")
print (f"{'Iy: ':10} {Iy:>5.2f}")
print (f"{'Ixy: ':10} {Ixy:>5.2f}")
print (f"{'Xt: ':10} {Xt:>5.2f}")
print (f"{'Yt: ':10} {Yt:>5.2f}")
print (f"{'Ixt: ':10} {Ixt:>5.2f}")
print (f"{'Iyt: ':10} {Iyt:>5.2f}")
print (f"{'Ixyt: ':10} {Ixyt:>5.2f}")