from parking_lot_space_test import parking_lot_space_test
from parking_car_details import parking_car_details_file
import datetime

#=======================Function to Get the Minimum Parking Slots================================================
def min_parking_slots_available(parking_lot):
    key_value = 1
    filter_parking_lots_available = filter(lambda x: parking_lot[x].slot_status =="AVAILABLE",parking_lot)
    print ("Available Parking Lots:" ,filter_parking_lots_available)
    print (type(filter_parking_lots_available)) 
    if filter_parking_lots_available:
       print ("min key value element : ", min(filter_parking_lots_available))
       min_parking_slot_available = min(filter_parking_lots_available)
       return (min_parking_slot_available)
    else:
       return 0

parking_lot1 = parking_lot_space_test(1,"Available")
#slot_id = getgetparkinglotvalues()
#print ("Parking Lot1:" , slot_id)

#========================Function to print the Status of the Parking Cars and Slot Details=======================

def getparkingcarsstatus(parking_car_details,in_no_parking_lot_slots):
    print ("Slot No.		 Registration No		Colour")
    filter_parking_cars_entry = filter(lambda x: parking_car_details[x].parking_car_exit_time ==None,parking_car_details) 
    #print (filter_parking_cars_entry)
    for key_value in filter_parking_cars_entry:
        #print ("Key Value :" , key_value)
        print("{}				{}				{}").format(parking_car_details[key_value].parking_slot_id,parking_car_details[key_value].parking_car_number,parking_car_details[key_value].parking_car_color)
        #print(parking_car_details[key_value].parking_car_number)
        #print(parking_car_details[key_value].parking_car_color)
     


#======================== Get the Input to create the parking lots================================================
in_no_parking_lot_slots = input("create_parking_lot")
print("Number of Parking Slots Requested :",in_no_parking_lot_slots)
parking_lot = {}
parking_car_details = {}
parking_car_details_temp = {}
i=1
j=1
parking_car_details_id = 1

while  i<= in_no_parking_lot_slots:
  parking_lot[i]=parking_lot_space_test(i,"AVAILABLE")
  print ("Parking Lot",i)
  print ("Parking Lot Values" , parking_lot[i].slot_id)
  print ("Parking Lot Values" , parking_lot[i].slot_status)
  i=i+1


print ("Created a parking lot with %s Slots" % (i-1) )

#==========================Please ignore the below comment lines==================================================
#now = datetime.datetime.now()
#parking_car_entry_time = now.strftime('%Y-%m-%d %H:%M:%S')
#parking_car_details1 = {}
#parking_car_details1 = parking_car_details_file()
#parking_car_details1[1] = parking_car_details_file(1,1,"KA","BLUE",parking_car_entry_time)
#print(parking_car_details1[1].parking_id)
#print(parking_car_details1[1].parking_slot_id)
#print(parking_car_details1[1].parking_car_number)
#print(parking_car_details1[1].parking_car_color)


#============================Get the Parking Car Details and the slot Number======================================
#Get the Parking car details and Allocate the Slot Number
park_car_id = 1
min_parking_slot_available =0
while (park_car_id <=in_no_parking_lot_slots):
      in_car_details_input = raw_input("")
      car_details=in_car_details_input.split(" ")
      car_details_car_number = car_details[1]
      car_details_car_color = car_details[2]
      print("Car Details:" , car_details)
      print ("Card Details - Car Number " ,car_details_car_number )
      print ("Card Details - Car Color" ,car_details_car_color)
      #Get the minimum values of the parking slots available and assign this to the Incoming car.
      #key_value = 1
      #filter_parking_lots_available = filter(lambda x: parking_lot[x].slot_status =="AVAILABLE",parking_lot)
      #print ("Available Parking Lots:" ,filter_parking_lots_available) 
      #print (type(filter_parking_lots_available))
      min_parking_slot_available = min_parking_slots_available(parking_lot)
      #print ("min key value element : ", min(filter_parking_lots_available))
      #parking_lot[1].slot_status ="NA"
      parking_lot[min_parking_slot_available].setparkingslotstatus("Not Available")
      print("Parking Lot1 :" , parking_lot[min_parking_slot_available].slot_id)
      print("Parking Lot 1 status :" , parking_lot[min_parking_slot_available].slot_status)
      print ("Allocated slot number: " , min_parking_slot_available)
      now = datetime.datetime.now()
      print(now.strftime('%Y-%m-%d %H:%M:%S'))
      parking_car_entry_time = now.strftime('%Y-%m-%d %H:%M:%S')
      parking_car_details[parking_car_details_id]=parking_car_details_file(parking_car_details_id,min_parking_slot_available,car_details_car_number,car_details_car_color,parking_car_entry_time)
      #parking_car_details.append(parking_car_details_temp)
      print(parking_car_details[parking_car_details_id].parking_id)
      print(parking_car_details[parking_car_details_id].parking_slot_id)
      print(parking_car_details[parking_car_details_id].parking_car_number)
      print(parking_car_details[parking_car_details_id].parking_car_color)
      print(parking_car_details[parking_car_details_id].parking_car_entry_time)
      park_car_id+=1
      parking_car_details_id+=1

#=====================================Get the Slot details of the car which is leaving=============================
in_leave_parking_lot = raw_input("")
leave_parking_car_details = in_leave_parking_lot.split(" ")
leave_parking_car_slot=int(leave_parking_car_details[1])

#Upate the status of the parking_lot_space to Available
parking_lot[leave_parking_car_slot].slot_status ="AVAILABLE"

#Update the Exit time of the parking car details
now = datetime.datetime.now()
print(now.strftime('%Y-%m-%d %H:%M:%S'))
parking_car_exit_time = now.strftime('%Y-%m-%d %H:%M:%S')
parking_car_details[leave_parking_car_slot].parking_car_exit_time = parking_car_exit_time

print("The Slot Number %s is free" %leave_parking_car_slot)
print (parking_lot[leave_parking_car_slot].slot_status )


#=======================================Print the Status of the Parking Car details and Slot Numbers================
in_status=raw_input("")
getparkingcarsstatus(parking_car_details,in_no_parking_lot_slots)

#=======================================Another Set of Cars Entry===================================================

inp_car_details_input_1 = raw_input("")
car_details_1 = inp_car_details_input_1.split(" ")
car_details_car_number_1 = car_details_1[1]
car_details_car_color_1 = car_details_1[2]

min_parking_slot_available = min_parking_slots_available(parking_lot)
parking_lot[min_parking_slot_available].setparkingslotstatus("Not Available")
now = datetime.datetime.now()
print(now.strftime('%Y-%m-%d %H:%M:%S'))
parking_car_entry_time = now.strftime('%Y-%m-%d %H:%M:%S')
parking_car_details[parking_car_details_id]=parking_car_details_file(parking_car_details_id,min_parking_slot_available,car_details_car_number_1,car_details_car_color_1,parking_car_entry_time)
print ("Allocated Slot Number: %s" , min_parking_slot_available)
print ("=============parking_car_details_id=========== %s :",parking_car_details_id )
print(parking_car_details[parking_car_details_id].parking_id)
print(parking_car_details[parking_car_details_id].parking_slot_id)
print(parking_car_details[parking_car_details_id].parking_car_number)
print(parking_car_details[parking_car_details_id].parking_car_color)
print(parking_car_details[parking_car_details_id].parking_car_entry_time)

parking_car_details_id = parking_car_details_id+1
inp_car_details_input_2 = raw_input("")
car_details_2 = inp_car_details_input_2.split(" ")
car_details_car_number_2 = car_details_2[1]
car_details_car_color_2 = car_details_2[2]

min_parking_slot_available = min_parking_slots_available(parking_lot)
if(min_parking_slot_available==0):
   print ("Sorry , Parking Lot is Full")
else:
   parking_lot[min_parking_slot_available].setparkingslotstatus("Not Available")
   now = datetime.datetime.now()
   print(now.strftime('%Y-%m-%d %H:%M:%S'))
   parking_car_entry_time = now.strftime('%Y-%m-%d %H:%M:%S')
   parking_car_details[parking_car_details_id]=parking_car_details_file(parking_car_details_id,min_parking_slot_available,car_details_car_number_1,car_details_car_color_1,parking_car_entry_time)
   print ("Allocated Slot Number: %s" , min_parking_slot_available)
   print ("=============parking_car_details_id=========== %s :",parking_car_details_id )
   print(parking_car_details[parking_car_details_id].parking_id)
   print(parking_car_details[parking_car_details_id].parking_slot_id)
   print(parking_car_details[parking_car_details_id].parking_car_number)
   print(parking_car_details[parking_car_details_id].parking_car_color)
   print(parking_car_details[parking_car_details_id].parking_car_entry_time)

