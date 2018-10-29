import datetime
import csv
import numpy as np
class PID(object):

	def __init__(self, pwm, i2c):
		self.pwm = pwm
		self.i2c = i2c

	def position(self, position):
		initial_position = position
		i = 0
		error_past = 0
		Integral = 0
		location = np.zeros(1000)

		while i < 1000:
			location[i] = self.i2c.getVoltage()
			error = (location[i] - initial_position)/ initial_position

			KP = 22.99
			KI = 10.83
			KD = 126

			V = error - error_past
			D = KD * V

			P = error * KP

			Integral += error 
			I = Integral * KI

			G = P + I + D


			peak_limit = 85
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
		date = datetime.datetime.now().strftime("%H:%M-%B-%d-%Y")	
	        filename = 'PID-Response-' + date +'.csv'
                myFile = open(filename, 'w')  
		with myFile:  
   			writer = csv.writer(myFile)
   			writer.writerows(myData)
