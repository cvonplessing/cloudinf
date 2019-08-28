import random as r
import math as m
import requests
import json
import time

#ratio procedure
def Montecarloratio(n):
	inside = 0
	total = n
	ratio = 0.0

	for i in range(0, total):
		x2 = r.random()**2
		y2 = r.random()**2
		if m.sqrt(x2 + y2) < 1.0:
			inside += 1

	ratio = (float(inside)/total)

	return ratio

#approximation of pi
def Montecarloaprox(ratio):
	aprox = 4.0 * ratio
	return aprox

def main():
	begin = time.time()
	pi = Montecarloaprox(Montecarloratio(1000000))
	end = time.time()
	latency1 = end - begin
	print('Local: ', pi ,'Latency: ', latency1)

	begin = time.time()
	res = requests.get('http://www.cloudinf.appspot.com/').json()['value']
	pic = Montecarloaprox(res)
	end = time.time()
	latency2 = end -begin
	print('Computer/Cloud: ', pic, 'Latency: ', latency2)



if __name__ == "__main__":
	main()

