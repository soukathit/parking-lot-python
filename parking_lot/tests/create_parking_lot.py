from parking_lot_space_test import parking_lot_space_test
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
