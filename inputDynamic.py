team_members = ["Neha" , "Chander" , "Ankit" , "Manoj" , "Prabhjot" , "Prashant" , "Parvinder"]
team_age = [23 , 25 , 24 , 26 , 25 , 27 , 24]
team_active = [True , True , True , False , True , False , True]    
team_location = ["India" , "USA" , "India" , "UK" , "India" , "USA" , "India"]
team_coordinates = [(28.6139, 77.2090) , (37.7749, -122.4194) , (19.0760, 72.8777) , (51.5074, -0.1278) , (12.9716, 77.5946) , (34.0522, -118.2437) , (22.5726, 88.3639)]
team_occupation = ["BE Developer" , "BE Developer" , "QA Engineer" , "Full Stack" , "Full Stack" , "FE Developer" , "Designer"]

print("Total Team Members = " + str(len(team_members)))

member_num = int(input("Enter member number (1-7): ")) - 1

if 0 <= member_num < len(team_members):
    print("Member {} is {} and age is {} coordinates are {} location is {} and occupation is {} Right now status is {}".format(
        member_num + 1,
        team_members[member_num],
        team_age[member_num],
        team_coordinates[member_num],
        team_location[member_num],
        team_occupation[member_num],
        team_active[member_num]
    ))
else:
    print("Invalid member number. Please enter a number between 1 and 7.")
