heart_rate = 77
too_low = heart_rate < 60
too_high = heart_rate > 100
print("Is heart rate low?" + str(too_low))
print("Is heart rate high?" +str(too_high))

if heart_rate <= 60: 
    print("Heart rate low!")
elif heart_rate >= 100: 
    print("Heart rate high!")
else:
    print("Heart rate ok!")

id_1 = "#4"
average_grade_1 = "A"
test_score_1 = 90

id_2 = "#5"
average_grade_2 = "A"
test_score_2 = 70

no_duplicates = id_1 != id_2
print("No duplicate entries" + str(no_duplicates))

same_average = average_grade_1 == average_grade_2
print("Same average grade:" + str(same_average))

higher_score = test_score_1 > test_score_2
print("id_has a higher score:" + str(higher_score))
