import i2c
import time


class Calibrate(object):
	def __init__(self, i2c, pwm):
		self.i2c = i2c
		self.pwm = pwm

	def setup(self):
		v_max = self.bottom()
		v_min = self.top()

		return v_min, v_max

	def bottom(self):
		self.pwm.DC(20)
		time.sleep(2)
		v_min = self.i2c.getVoltage()
		self.pwm.DC(0)

		return v_min

	def top(self):
		self.pwm.DC(100)
		time.sleep(2)
		v_min = self.i2c.getVoltage()
		self.pwm.DC(0)

		return v_min

if __name__ == '__main__':
	import i2c
	import controller
	import calibrate
	cal = Calibrate()
