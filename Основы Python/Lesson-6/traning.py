import time

class TrafficLight:
	"""docstring for TrafficLight"""
	_color = ""
	def running(self):
		TrafficLight._color = 'red'
		if TrafficLight._color == 'red':
			print(TrafficLight._color)
			time.sleep(7)
		TrafficLight._color = 'yellow'
		if TrafficLight._color == 'yellow':
			print(TrafficLight._color)
			time.sleep(2)
		TrafficLight._color = 'green'
		if TrafficLight._color == 'green':
			print(TrafficLight._color)
			time.sleep(2)


#a = TrafficLight()
#a.running()

class Road():
	"""docstring for Road"""
#	_length = 0
#	_width = 0

	def count(self, _length, _width, weight, height):
		self._length = _length
		self._width = _width
		self.weight = weight
		self.height = height
		print(_length * _width * weight * height)

rd = Road()
rd.count(20, 5000, 25, 5)