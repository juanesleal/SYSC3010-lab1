#program for area of a triangle

a = 4
b = 3
c = 5

s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5


print('The area of the triangle is %0.2f' %area)