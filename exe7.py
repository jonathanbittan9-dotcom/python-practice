total_fuel=0
sum=0
sum_total=0
for drivers in range(30):   
    distance=int(input("Enter a distance:"))
    while distance!=-1 :
        sum=sum+distance
        sum_total=sum_total+distance
        distance=int(input("Enter a distance:"))
        total_fuel=+total_fuel+distance
    print("you drove:" , sum , "kilometers")
    print("you used" , (total_fuel/10) , "liters")
print("all the drivers  drove:" , sum_total , "kilometers")




        

