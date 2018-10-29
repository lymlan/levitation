import smbus
import time
# for RPI version 1, use 'bus = smbus.SMBus(0)'
bus = smbus.SMBus(1)

# This is the address we setup in the Arduino Program
address = 0x04

def writeNumber(value):
	bus.write_byte(address, value)
# bus.write_byte_data(address, 0, value)
	return -1

def readNumber():
    #number = bus.read_byte(address)
    number = bus.read_i2c_block_data(address, 0, 4)
    #number = bus.read_byte_data(address, 1)
    return number

while True:
	var = input("Enter 1-9 \n")
	if not var:
		continue

	writeNumber(int(var))
	print ('RPI: Hi Arduino, I sent you ', var)
	# sleep one second
	#time.sleep(1)

	number = readNumber()
	test = ''.join(str(x) for x in number)
	voltage = float(test)/ 1000
	print(voltage * 2)


    
