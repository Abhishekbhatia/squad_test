class Vehicle:
	def __init__(self,regno):
		self.regno = regno

class Car(Vehicle):

	def __init__(self,regno):
		Vehicle.__init__(self,regno)

	def getType(self):
		return "Car"
