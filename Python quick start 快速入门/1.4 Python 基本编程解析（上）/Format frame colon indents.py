from random import random
List = [0,0]
for i in range(0,1000000):
	x = random()
	y = random()
	if pow(x,2)+pow(y,2)<=1:
		List[0] += 1
	else:
		List[1] += 1
print("Pi的值是 {:.5f}F".format(4*float(List[0])/(i + 1)))
