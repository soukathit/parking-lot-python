#!/usr/bin/env python
from parking_lot_space import parking_lot_space
from parking_car_details.parking_car_details import parking_car_details_file
import datetime
import sys

#=======================Function to Get the Minimum Parking Slots================================================
def min_parking_slots_available(parking_lot):
    key_value = 1
    filter_parking_lots_available = filter(lambda x: parking_lot[x].slot_status =="AVAILABLE",parking_lot)
    #print ("Available Parking Lots:" ,filter_parking_lots_available)
    #print (type(filter_parking_lots_available)) 
    if filter_parking_lots_available:
       #print ("min key value element : ", min(filter_parking_lots_available))
       min_parking_slot_available = min(filter_parking_lots_available)
       return (min_parking_slot_available)
    else:
       return 0

parking_lot1 = parking_lot_space(1,"Available")
#slot_id = getgetparkinglotvalues()
#print ("Parking Lot1:" , slot_id)

#========================Function to print the Status of the Parking Cars and Slot Details=======================

def getparkingcarsstatus(parking_car_details):
    print ("Slot No.			Registration No				Colour")
    filter_parking_cars_entry = filter(lambda x: parking_car_details[x].parking_car_exit_time ==None,parking_car_details) 
    #print (filter_parking_cars_entry)
    for key_value in filter_parking_cars_entry:
        #print ("Key Value :" , key_value)
        print("{}				{}				{}").format(parking_car_details[key_value].parking_slot_id,parking_car_details[key_value].parking_car_number,parking_car_details[key_value].parking_car_color)
        #print(parking_car_details[key_value].parking_car_number)
        #print(parking_car_details[key_value].parking_car_color)
    return parking_car_details 
    
#======================Function to Create a parking lot==========================================================

def create_parking_lot_space_file(in_no_parking_lot_slots,in_parking_lot):
    i=1
    while  (i<= in_no_parking_lot_slots):
           parking_lot[i]=parking_lot_space(i,"AVAILABLE")
           #print ("Parking Lot",i)
           #print ("Parking Lot Values" , parking_lot[i].slot_id)
           #print ("Parking Lot Values" , parking_lot[i].slot_status)
           i=i+1
    print ("Created a parking lot with %s Slots" % (i-1) )
    return parking_lot

#======================Function to Allocate the Parking Slot to Cars============================================

def park(parking_lot,car_details_car_number,car_details_car_color,parking_car_details,parking_car_details_id):
   min_parking_slot_available = min_parking_slots_available(parking_lot)
   if   (min_parking_slot_available==0):
        print ("Sorry , Parking Lot is Full")
        return (parking_car_details)
   else:
        parking_lot[min_parking_slot_available].setparkingslotstatus("Not Available")
        now = datetime.datetime.now()
        #print(now.strftime('%Y-%m-%d %H:%M:%S'))
        parking_car_entry_time = now.strftime('%Y-%m-%d %H:%M:%S')
        parking_car_details[parking_car_details_id]=parking_car_details_file(parking_car_details_id,min_parking_slot_available,car_details_car_number,car_details_car_color,parking_car_entry_time)
        print ("Allocated Slot Number: %s"  %min_parking_slot_available)
        #print ("=============parking_car_details_id=========== %s :",parking_car_details_id )
        #print(parking_car_details[parking_car_details_id].parking_id)
        #print(parking_car_details[parking_car_details_id].parking_slot_id)
        #print(parking_car_details[parking_car_details_id].parking_car_number)
        #print(parking_car_details[parking_car_details_id].parking_car_color)
        #print(parking_car_details[parking_car_details_id].parking_car_entry_time)
        return (parking_car_details)

#========================Function for Leave - Parking Car Exit==================================================

def leave_parking_lot(parking_lot,parking_car_details,leave_parking_car_slot):
    #leave_parking_car_slot = int(leave_parking_car_slot)
    parking_lot[leave_parking_car_slot].slot_status ="AVAILABLE"

    #Update the Exit time of the parking car details
    now = datetime.datetime.now()
    #print(now.strftime('%Y-%m-%d %H:%M:%S'))
    parking_car_exit_time = now.strftime('%Y-%m-%d %H:%M:%S')
    parking_car_details[leave_parking_car_slot].parking_car_exit_time = parking_car_exit_time

    print("The Slot Number %s is free" %leave_parking_car_slot)
    #print (parking_lot[leave_parking_car_slot].slot_status )



#========================Put all the Init Blocks Here============================================================
parking_lot = {}
parking_car_details = {}
parking_car_details_temp = {}
i=1
j=1
parking_car_details_id = 1
car_details_car_number =""
car_details_car_color=""
input_file_flag ="N"
commands_lines_iter = 1

#======================== Get the Sequence of Command Line Inputs================================================
if __name__ == "__main__":
   if  (len(sys.argv)!=0 and len(sys.argv)==2):
       in_file_name = sys.argv[1]
       #in_file=open(in_file_name, "r")
       with open(in_file_name) as file:
            commands_list = [line.strip() for line in file]
       #print (commands_list)
       input_file_flag="Y"
       in_command_1 = commands_list[0]
   else:
       in_command_1 = raw_input("")
   #print ("The Command Entered is : %s" , in_command_1)
   while (in_command_1):
         in_command = in_command_1.split(" ")
         in_command_1=""
         if  (in_command[0] == "create_parking_lot"):
             #print ("Input Command Output After the carete_parking_lot_function : %s",in_command_1) 
             in_no_parking_lot_slots = int(in_command[1])
             #print ("The Number of Parking Slots Requested: %s",in_no_parking_lot_slots)
             parking_lot = create_parking_lot_space_file(in_no_parking_lot_slots,parking_lot)
             if (input_file_flag=="Y"):
                if (len(commands_list) == commands_lines_iter):
                   exit()
                else :
                   in_command_1 = commands_list[commands_lines_iter]
             else :
                   in_command_1 = raw_input("")
             #exit()
             commands_lines_iter+=1        
 
         if  (in_command[0] == "park"):
             car_details_car_number = in_command[1]
             car_details_car_color = in_command[2]
             #print ("Card Details - Car Number " ,car_details_car_number )
             #print ("Card Details - Car Color" ,car_details_car_color)
             parking_car_details = park(parking_lot,car_details_car_number,car_details_car_color,parking_car_details,parking_car_details_id)
             parking_car_details_id+=1
             if (input_file_flag=="Y"):
                if (len(commands_list) == commands_lines_iter):
                   exit()
                else :
                   in_command_1 = commands_list[commands_lines_iter]
             else :
                   in_command_1 = raw_input("")
             commands_lines_iter+=1

         if  (in_command[0]== "status"):
             parking_car_details = getparkingcarsstatus(parking_car_details)
             if (input_file_flag=="Y"):
                if (len(commands_list) == commands_lines_iter):
                   exit()
                else :
                   in_command_1 = commands_list[commands_lines_iter]
             else :
                   in_command_1 = raw_input("")
             commands_lines_iter+=1

         if  (in_command[0]=="leave"):
             leave_parking_car_slot=int(in_command[1])
             #print ("The requested parking car slot to leave is: %s" , leave_parking_car_slot)
             parking_lot[leave_parking_car_slot].slot_status ="AVAILABLE"
             now = datetime.datetime.now()
             #print(now.strftime('%Y-%m-%d %H:%M:%S'))
             parking_car_exit_time = now.strftime('%Y-%m-%d %H:%M:%S')
             parking_car_details[leave_parking_car_slot].parking_car_exit_time = parking_car_exit_time

             print("Slot Number %s is free" %leave_parking_car_slot)
             #print (parking_lot[leave_parking_car_slot].slot_status )
             #parking_lot = leave_parking_lot(parking_lot,leave_parking_car_slot,parking_car_details)    
             if (input_file_flag=="Y"):
                if (len(commands_list) == commands_lines_iter): 
                   exit()
                else : 
                   in_command_1 = commands_list[commands_lines_iter]
             else :
                   in_command_1 = raw_input("")
             commands_lines_iter+=1
      
         if  (in_command[0]=="registration_numbers_for_cars_with_colour"):
             car_color_search = in_command[1]
             #parking_car_details = getparkingcarsstatus(parking_car_details)
             filter_parking_cars_color = filter(lambda x: parking_car_details[x].parking_car_color ==car_color_search and parking_car_details[x].parking_car_exit_time ==None,parking_car_details)
             key_value = 1
             registration_numbers=""
             if not filter_parking_cars_color:
                #print ("The Registration numbers for car with colour %s is not found" %car_color_search)
                print ("Not Found")
             else:
                for key_value in filter_parking_cars_color:
                    #print ("Key Value :" , key_value)
                    #print("{}				{}				{}").format(parking_car_details[key_value].parking_slot_id,parking_car_details[key_value].parking_car_number,parking_car_details[key_value].parking_car_color)
                    registration_numbers = registration_numbers + "," +parking_car_details[key_value].parking_car_number
                    key_value+=1
                print (registration_numbers[1:])      
             if (input_file_flag=="Y"):
                if (len(commands_list) == commands_lines_iter):
                   exit()
                else :
                   in_command_1 = commands_list[commands_lines_iter]
             else :
                   in_command_1 = raw_input("")
             commands_lines_iter+=1

         if  (in_command[0]=="slot_numbers_for_cars_with_colour"):    
             car_color_search = in_command[1]
             #parking_car_details = getparkingcarsstatus(parking_car_details)
             filter_parking_cars_color = filter(lambda x: parking_car_details[x].parking_car_color ==car_color_search and parking_car_details[x].parking_car_exit_time ==None ,parking_car_details)
             key_value = 1
             slot_numbers =""
             if not filter_parking_cars_color:
                #print ("The Slot numbers for car with colour %s is not found" %car_color_search)
                print ("Not Found")
             else:
                for key_value in filter_parking_cars_color:
                    #print ("Key Value :" , key_value)
                    #print("{}                         {}                              {}").format(parking_car_details[key_value].parking_slot_id,parking_car_details[key_value].parking_car_number,parking_car_details[key_value].parking_car_color)
                    slot_numbers = slot_numbers + "," + str(parking_car_details[key_value].parking_slot_id)
                    key_value+=1
                print (slot_numbers[1:])
             if (input_file_flag=="Y"):
                if (len(commands_list) == commands_lines_iter):
                   exit()
                else : 
                   in_command_1 = commands_list[commands_lines_iter]
             else :
                   in_command_1 = raw_input("")
             commands_lines_iter+=1

         if  (in_command[0]=="slot_number_for_registration_number"):
             registration_number_search = in_command[1]
             #parking_car_details = getparkingcarsstatus(parking_car_details)
             filter_parking_cars_color = filter(lambda x: parking_car_details[x].parking_car_number ==registration_number_search and parking_car_details[x].parking_car_exit_time ==None,parking_car_details)
             key_value = 1
             slot_numbers =""
             if not filter_parking_cars_color:
                #print ("The Slot numbers for car with colour %s is not found" %car_color_search)
                print ("Not Found")
             else:
                for key_value in filter_parking_cars_color:
                    #print ("Key Value :" , key_value)
                    #print("{}                         {}                              {}").format(parking_car_details[key_value].parking_slot_id,parking_car_details[key_value].parking_car_number,parking_car_details[key_value].parking_car_color)
                    slot_numbers = slot_numbers + "," + str(parking_car_details[key_value].parking_slot_id)
                    key_value+=1
                print (slot_numbers[1:])
             if (input_file_flag=="Y"):
                if (len(commands_list) == commands_lines_iter):
                   exit()
                else:
                   in_command_1 = commands_list[commands_lines_iter]
             else :
                   in_command_1 = raw_input("")      
             commands_lines_iter+=1          

         if  (in_command[0]=="exit" or in_command == "exit"):
             exit()

#==========================End of the Program==================================================
