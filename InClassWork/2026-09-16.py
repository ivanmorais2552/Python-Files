#Definite = We know how many times we want it to run
#Indefinite = We don't know how many times it will run

#Day 1, Appointment 1
#Day 2, Appointment 2
#...
#Day 1, Appointment 5
#...
#Day 3, Appointment 5

for days in range(3):
    for appointments in range (5):
        print(f"Day {days + 1}, Appointment {appointments + 1}")