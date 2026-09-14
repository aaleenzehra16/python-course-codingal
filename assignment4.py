#Classroom points calculator
classteam_1=25
classteam_2=28
classteam_3=35
classteam_4=31
classteam_5=20

#calculating the total and average using + and / operators
total_points=classteam_1+classteam_2+classteam_3+classteam_4+classteam_5
average_points=total_points/5
print("total points for all teams are",total_points)
print("average points for the teams are",average_points)

#calculating total reward stars by using a * operator
stars_per_point=3
total_reward_stars=total_points*stars_per_point
print("total stars rewarded are",total_reward_stars)

#using floor division and mod to find number of full boxes and leftover stars
number_of_boxes=(total_points*stars_per_point)//25
leftover_stars=(total_points*stars_per_point)%25
print("Number of full boxes are",number_of_boxes)
print("Number of leftover stars are",leftover_stars)

#using operators to compare last week's data to this week's data
last_week=170
print(last_week>total_points)
print(last_week==total_points)
print(last_week>=total_points)

#Using += and -= operators to update total points
bonus_points=15
total_points +=bonus_points
print("total points after adding bonus points are",total_points)
missed_task_points=5
total_points -=missed_task_points
print("total points are subtracting missed task points are",missed_task_points)