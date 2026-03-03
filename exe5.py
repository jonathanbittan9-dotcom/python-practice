avg=0
avg_of_all_class=0
for student in range(35):
    for subject in range(12):
        grade=int(input("Enter a grade:"))
        avg=avg+grade
        avg_of_all_class=avg_of_all_class+grade
    print(avg/12)
    avg=0
avg_of_all_class=avg_of_all_class/(35*12)
print(avg_of_all_class)
