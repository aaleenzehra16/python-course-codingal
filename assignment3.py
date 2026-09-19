#asking user for details and storing them using different data types
member_name=input("Enter your name.")
club_name=input("Enter the name of your school club.")
member_number=5
points_earned=75.5
event_count=10
meeting_hours=2
active_status=True

#Printing the user details and the data types
print(f"{member_name}{type(member_name)} is a member of the {club_name} club {type(club_name)}")
print(f"{member_name} earned {points_earned} points\n {type(points_earned)}")
print(f"{member_name}'s meeting lasts {meeting_hours} hours\n {type(meeting_hours)}")
print(f"the member is active:{active_status}\n {type(active_status)}")

#typecasting the member details into text
membernum_str=str(member_name)
points_str=str(points_earned)
eventcount_str=str(event_count)
hours_str=str(meeting_hours)
status_str=str(active_status)

#printing the text with its datatype
print(f"member name as text:{membernum_str}\n{type(membernum_str)}")
print(f"points earned as text:{points_earned}\n{type(points_str)}")
print(f"event count as text:{eventcount_str}\n{type(eventcount_str)}")
print(f"meeting hours as text:{hours_str}\n{type(hours_str)}")
print(f"active status as text:{status_str}\n{type(status_str)}")

#slicing member name to create a badge code
badge_code=member_name[0:3]+member_name[-1:]
print("the badge code is", badge_code)

#reversing the club name to create a secret code
secret_code=club_name[::-1]
print("the secret code is", secret_code)

#creating the final badge using the text values
line_1="badge code:",badge_code
line_2="Member Name:", member_name+"Member Number:",membernum_str
line_3="Club Name:",club_name+"secret code:",secret_code
line_4="Events attended:",eventcount_str+"Meeting Duration:",hours_str
line_5="Active status:",status_str

#Printing the badge
print("School Club Member Badge")
print(line_1)
print(line_2)
print(line_3)
print(line_4)
print(line_5)