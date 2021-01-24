

with open('matrix', 'r') as fmatrix:
    matrix = [[int(num) for num in line.split(',')] for line in fmatrix]


print('Зчитана матриця :')
print(matrix)
print('')

print('Критерій вальда')

minValues = []
maxValues = []
koef = 0.7

for x in matrix:
 minValues.append(min(x))
 maxValues.append(max(x))

hurwitz = []
iterator = 0


print(minValues)

print('Максимальне значення з матриці мінімумів(рядка)')

print(max(minValues))

print('')
print('Критерій Максимаса')
print('Максимальне значення')
print(maxValues)
print('Максимальне значення з матриці максимумів(рядка)')
print(max(maxValues))

print('')
print("Критерій гурвіта з коефіцієнтом %(koef)s"%{"koef":"{:.1f}".format(koef)})

for x, y in zip(minValues, maxValues):
    hurwitz.append(koef*x +(1-koef)*y)
    print ("K(%(iterator)d) = %(hurwitz)d" % {"iterator": iterator, "hurwitz":hurwitz[iterator]})
    iterator +=1
print("K(opt) = %(max)d"%{"max":max(hurwitz)})

print('')
print('Критерій Лапласа')


lmatrix = []
for x in matrix:
    lmatrix.append((sum(x)+0.0)/len(x))
print(lmatrix)
print('Максимальне значення')
print(lmatrix[lmatrix.index(max(lmatrix))])

print('')
print('Критерій ZBL')

qn = [.5, .35, .15]
print("q1 = %(q0)s q2 = %(q1)s q3 = %(q2)s"%{"q0":"{:.2f}".format(qn[0]),"q1":"{:.2f}".format(qn[1]),"q2":"{:.2f}".format(qn[2])})

blmatrix = []
maxbl = []
for x in matrix :
    blmatrix.append([(i+ .0) * y for i, y in zip(x,qn)])
    maxbl.append(sum([(i+ .0) * y for i, y in zip(x,qn)]))

print(blmatrix)
print('Максимальне значення ')
print(maxbl)
print("Максимум з максимумом %(max)s"%{"max":max(maxbl)})

