#exercise 2
print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 % 4)
print(3 / 4)
print(3 ** 4)
print(15 // 4)
#exercise 3, Part-1
print("Asif Ahmed")
print("Howlader")
print("Fiji")
print("I am enjoying learning python.")

print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4 - 4j))
print(type(['Asif', 'Fiji', 'Python']))
print(type('Howlader'))
#exercise 3
print(type(3)) #integer
print(type(3.14)) #float
print(type(4j)) #complex
print(type('Asif')) #string
print(type(True)) #boolean
print(type(['Asif', 'Pyhton','Fiji']))
print(type((1, 2, 3, 4.5, 9, 6)))
print(type({2, 3, 4, 5, 6}))
print(type({'name':'Asif'}))

#Part-2
import math

p = [2, 3]
q = [ 10, 8]

print(math.dist(p,q))

distance = math.sqrt((q[0] - p[0])**2 + (q[1] - p[1])**2)
print(distance)