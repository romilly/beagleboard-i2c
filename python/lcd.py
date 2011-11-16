#! /usr/bin/python
import i2c, time

FF = '\f' # Form Feed

class LCD:
	def __init__(self, address):	
		self.lcd = i2c.I2C_device(0x04)
		
	def pr(self, ch):
		self.lcd.begin_transmission()
		self.lcd.send(ord(ch))
		self.lcd.end_transmission()
		
	def prints(self, string):
		for ch in string:
			self.pr(ch)
			
	def clear(self):
		self.pr(FF)
			
lcd = LCD(4)
lcd.clear()
lcd.prints('Hi from BB')
time.sleep(2)
lcd.clear()
lcd.prints('Hello again')
