sum_of_class=0
sum_total=0
for classes in range(6):
    for student in range(30):
        contribution=int(input("Enter a contribution:"))
        sum_of_class=sum_of_class+contribution
        sum_total=sum_total+contribution
    print("the total contribution of class is:" , sum_of_class)
    sum_of_class=0
print("the total contribution of all classes is:" , sum_total)
