score = input("Enter Score: ")

sc =  float(score)
x = 'There has been an ERROR'

if sc >= 0.9:
	x = 'A'
elif sc >=0.8:
	x='B'
elif sc >=0.7:
	x='C'
elif sc >= 0.6:
	x='D'
elif sc < .6:
	x ='F'
else:
	x ="Out of Range"
	
print (x)