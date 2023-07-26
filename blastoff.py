n=5
while n > 0:
    print(n)
    n=n-1
print(n)
print('Blastoff!')

print()

for i in [5, 4, 3, 2, 1] :
    print(i)
print('Blastoff!')

print()

friends = ['Luis', 'Drew', 'Joseph', 'Nelson']
for friend in friends:
    print('Happy New Year,', friend,'!')
print('Done')

print()

for i in [5, 4, 3, 2, 1] :
    print(i)

print()

lsf = -1
print('Before', lsf)
for tn in [9,41,12,3,74,15] :
    if tn > lsf :
        lsf = tn
    print(lsf, tn)
print('After', lsf)

print()

lsf = -1
for tn in [9,41,12,3,74,15] :
    while tn > lsf :
        lsf = tn
    print(tn)
print('Largest Number', lsf)

print()

sum = 0
print('Before', sum)
for num in [9,41,12,3,74,15] :
    sum = sum + num
    print(sum, num)
print('After', sum)

print()

count = 0
sum = 0
print('Before', count, sum)
for value in [9,41,12,3,74,15] :
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print('After', count, sum, sum / value)

print()

print('Before')
for value in [9,41,12,3,74,15] :
    if value > 20 :
        print('Large number', value)
print('After')

print()

found = False
print('Before', found)
for value in [9,41,12,3,74,15] :
    if value == 3 :
        found = True
    print('Found', value)
print('After', found)

print()

smallest = None
for value in [9,41,12,3,74,15] :
    if smallest is None :
        smallest = value
    elif value < smallest :
        smallest = value
print(smallest)

print()

tot = 0
for i in [5, 4, 3, 2, 1] :
    tot = tot + 1
print(tot)

print()

friends = ['Joseph', 'Glenn', 'Sally'] 
for friend in friends :
    print('Happy New Year', friend)
print('Done.')