import Vehicle
import Driver
import argparse
import sys
import os

if sys.version_info[0] == 2:
	inp = input()

class ParkingLot:
	def __init__(self):
		self.capacity = 0
		self.slotid = 0
		self.numOfOccupiedSlots = 0
		self.regnos = []

	def createParkingLot(self,capacity):
		self.slots = [-1] * capacity
		self.capacity = capacity
		return self.capacity

	def getEmptySlot(self):
		try:
			for i in range(len(self.slots)):
				if self.slots[i] == -1:
					return i
		except AttributeError as error:
			print("~~~ Please make sure to create the parking lot before retrieving the information from it.")
			exit(0)

	def park(self,regno,driver_age):
		try:
			if self.numOfOccupiedSlots < self.capacity:
				if regno in self.regnos:
					print("The car registration number is not unique. Inform the cops !!!")
					exit(0)
				slotid = self.getEmptySlot()
				self.slots[slotid] = {"reg_no" : Vehicle.Car(regno), "driver_age": Driver.Driver(driver_age)}
				self.slotid = self.slotid+1
				self.numOfOccupiedSlots = self.numOfOccupiedSlots + 1
				self.regnos.append(regno)
				return slotid+1
				
			else:
				return -1
		except AttributeError as error:
			print("~~~ Please make sure to create the parking lot before retrieving the information from it.")
			exit(0)

	def leave(self,slotid):
		try:
			if self.numOfOccupiedSlots > 0 and self.slots[slotid-1] != -1:
				self.slots[slotid-1] = -1
				self.numOfOccupiedSlots = self.numOfOccupiedSlots - 1
				return True
			else:
				return False
		except AttributeError as error:
			print("~~~ Please make sure to create the parking lot before retrieving the information from it.")
			exit(0)	

	def status(self):
		try:
			print("Slot No.\tRegistration No.\tDriver_Age")
			for i in range(len(self.slots)):
				if self.slots[i] != -1:
					print(str(i+1) + "\t\t" +str(self.slots[i]['reg_no'].regno) + "\t\t" + str(self.slots[i]['driver_age'].driver_age))
				else:
					continue
		except AttributeError as error:
			print("~~~ Please make sure to create the parking lot before retrieving the information from it.")
			exit(0)

			
	def getSlotNoFromRegNo(self,regno):

		try:
			for i in range(len(self.slots)):
				if self.slots[i]['reg_no'].regno == regno:
					return i+1
				else:
					continue
			return -1
		except AttributeError as error:
			print("~~~ Please make sure to create the parking lot before retrieving the information from it.")
			exit(0)
			

	def getSlotNoFromDriverAge(self,age):
		
		slotnos = []
		try:
			for i in range(len(self.slots)):
				if self.slots[i] == -1:
					continue
				if self.slots[i]['driver_age'].driver_age == age:
					slotnos.append(str(i+1))
			return ",".join(slotnos)
		except AttributeError as error:
			print("~~~ Please make sure to create the parking lot before retrieving the information from it.")
			exit(0)
	
	def getRegNoFromDriverAge(self,age):

		regnos = []
		try:
			for i in range(len(self.slots)):
				if self.slots[i] == -1:
					continue
				if self.slots[i]['driver_age'].driver_age == age:
					regnos.append(self.slots[i]['reg_no'].regno)			
			return regnos
		except AttributeError as error:
			print("~~~ Please make sure to create the parking lot before retrieving the information from it.")
			exit(0)

	def show(self,line):
		if line.lower().startswith('create_parking_lot'):
			n = int(line.split(' ')[1])
			res = self.createParkingLot(n)
			print('+++ Created a parking lot with '+str(res)+' slots')

		elif line.lower().startswith('park'):
			if self.capacity and self.capacity > 0:
				regno = line.split(' ')[1]
				driver_age = line.split(' ')[3]
				res = self.park(regno,driver_age)
				if res == -1:
					print("Sorry, parking lot is full")
				else:
					print(f'+++ Car with vehicle registration number \"{regno}\" has been parked at slot number {res}')
			else:
				print("~~~ Please create a parking lot before parking the vehicles!!")
				exit(0)

		elif line.lower().startswith('leave'):
			leave_slotid = int(line.split(' ')[1])
			driver_age = self.slots[leave_slotid-1]['driver_age'].driver_age
			reg_no = self.slots[leave_slotid-1]['reg_no'].regno
			status = self.leave(leave_slotid)
			if status:
				print(f'--- Slot number {str(leave_slotid)} vacated, car with vehicle registration number \"{reg_no}\" left the parking space, the driver of the car was of age {driver_age}')

		elif line.lower().startswith('status'):
			self.status()

		elif line.lower().startswith('slot_numbers_for_driver_of_age'):
			driver_age = line.split(' ')[1]
			slotnos = self.getSlotNoFromDriverAge(driver_age)
			if len(slotnos) <=0 :
				print("Not Found")
			else:
				print(f'*** Slot number(s) for driver with age {driver_age} : {slotnos}')

		elif line.lower().startswith('slot_number_for_car_with_number'):
			regno = line.split(' ')[1]
			slotno = self.getSlotNoFromRegNo(regno)
			if slotno == -1:
				print("Not found")
			else:
				print(f'*** Slot number for car with registration number {regno} : {slotno}')

		elif line.lower().startswith('vehicle_registration_number_for_driver_of_age'):
			driver_age = line.split(' ')[1]
			regno = self.getRegNoFromDriverAge(driver_age)
			if len(regno) == 0:
				print(f"*** No car found for driver age {driver_age}")
			else:
				print(",".join(regno))
		elif line.startswith('exit'):
			exit(0)

def main():

	parkinglot = ParkingLot()
	parser = argparse.ArgumentParser()
	parser.add_argument('-f', action="store", required=False, dest='src_file', help="Input File. If not provided, default file input/commands.txt will be picked up")
	args = parser.parse_args()
	

	if os.path.exists(os.path.join(os.path.dirname(os.path.realpath(__file__)),'input','commands.txt')):
		file_name = os.path.join(os.path.dirname(os.path.realpath(__file__)),'input','commands.txt')
	elif args:
		file_name = args.src_file
	
	if file_name:
		with open(file_name) as f:
			for line in f:
				line = line.rstrip('\n')
				parkinglot.show(line)
	else:
			while True:
				line = input("$ ")
				parkinglot.show(line)

if __name__ == '__main__':
	main()
