total_fuel=0
sum=0
sum_total=0
for drivers in range(30):   
    distance=int(input("Enter a distance of km:"))
    while distance!=-1 :
        sum=sum+distance
        sum_total=sum_total+distance
        total_fuel=+total_fuel+distance
        distance=int(input("Enter a distance:"))
    print("you drove:" , sum , "kilometers")
    print("you used" , (total_fuel/10) , "liters")
    sum=0
    total_fuel=0
print("all the drivers  drove:" , sum_total , "kilometers")




        

