motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('honda')
print(motorcycles)

motorcycles.insert(0, 'arlen ness')
print(motorcycles)

del motorcycles[1]
print(motorcycles)

popped = motorcycles.pop()
print(popped)
print(motorcycles)

first = motorcycles.pop(0)
print(f'The first item was {first.title()}')

removed = motorcycles.remove('yamaha')
print(removed)
print(motorcycles)