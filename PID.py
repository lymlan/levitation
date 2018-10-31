import datetime
import csv
import numpy as np


class PID(object):

	def __init__(self, pwm, i2c):
		self.pwm = pwm
		self.i2c = i2c

	def position(self, position):
		target_position = position
		i = 0
		error_past = 0
		Integral = 0
		location = np.zeros(1000)
                G = 0
                peak_limit = 100
		while i < 1000:
			location[i] = self.i2c.getVoltage()
			error = (location[i] - target_position)/ target_position

			KP = 10.99
			KI = 123
			KD = 200

			V = error - error_past
			D = KD * V

			P = error * KP
                        if G != peak_limit:
			    Integral += error
			    I = Integral * KI

			G = P + I + D

			if G > peak_limit:
				G = peak_limit
			elif G < 0:
				G = 0
			self.pwm.DC(G)
			i +=1
			error  = error_past

		length = np.transpose(np.linspace(0,999,1000))
		location = np.transpose(location)
		myData = [length, location]  
		date = datetime.datetime.now().strftime("%H-%M-%S-%B-%d-%Y")	
	        filename = './logs/PID-Response-' + date +'.csv'
                myFile = open(filename, 'w')  
		with myFile:  
   			writer = csv.writer(myFile)
   			writer.writerows(myData)
