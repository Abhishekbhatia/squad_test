## ParkingLot
Design a parking lot using Python with TDD approach

## Dependencies

You just need Python. The code is compatible with Python3. Visit the link https://www.python.org/downloads/ to install Python3. 

## Description

This repository gives an overview of how we can design a basic parking lot in Python. It creates parking lot with given number of slots. The cars follow Greedy approach while being parked in the slots.

ParkingLot.py script defines the following functions -

1. `create_parking_lot n` - Given n number of slots, create a parking lot
2. `park car_regno driver_age n` - Parks a vehicle with given registration number and driver_age in the nearest empty slot possible. If there are no more empty slots available, it shows a message "Sorry, parking lot is full".
3. `status` - Prints the slot number, registration number of the parked vehicles and driver's age.
4. `leave x` - Removes vehicle from slot number x
5. There are few query functions to retrieve slot number from registration number of car, get registration numbers of cars with driver age etc.


ParkingLot.py can be run through shell or through file containing test cases. An example file `input/commands.txt` has been provided in repo.

I have followed TDD approach while designing this. `test_parking_lot.py` uses `unittest` module of python. Here 6 test cases are written in order to test each functionality mentioned in ParkingLot.py

Vehicle.py is a separate class where we can define the type of vehicles that can be parked. As of now, it only contains class `Car`
Driver.py is also a separate class where the driver's age is the only attribute present for now.

## Run instructions

To create your own ParkingLot - 

1. python ParkingLot.py --help

usage: ParkingLot.py [-h] [-f SRC_FILE]       

optional arguments:
  -h, --help   show this help message and exit
  -f SRC_FILE  Input File. If not provided, default file from
               input/commands.txt will be picked up

2. python ParkingLot.py -f <filename>

Will run the commands from the filename

3. python ParkingLot.py

- Check if default input/commands.txt is present. If not,
- Take input from user directly

## Output

+++ - Indicates something is added
--- - Indicates something is removed
*** - General Info
~~~ - Error/Exception


+++ Created a parking lot with 6 slots
+++ Car with vehicle registration number "KA-01-HH-1234" has been parked at slot number 1
+++ Car with vehicle registration number "PB-01-HH-1234" has been parked at slot number 2
*** Slot number(s) for driver with age 21 : 1,2
+++ Car with vehicle registration number "PB-01-TG-2341" has been parked at slot number 3
*** Slot number for car with registration number PB-01-HH-1234 : 2
--- Slot number 2 vacated, car with vehicle registration number "PB-01-HH-1234" left the parking space, the driver of the car was of age 21
+++ Car with vehicle registration number "HR-29-TG-3098" has been parked at slot number 2
*** No car found for driver age 18
Slot No.        Registration No.        Driver_Age
1               KA-01-HH-1234           21
2               HR-29-TG-3098           39
3               PB-01-TG-2341           40

## Test cases 

python .\test_parking_lot.py
......
----------------------------------------------------------------------
Ran 6 tests in 0.002s

OK



