seconds = 1
minutes = 60 * seconds
hours = 60 * minutes
depart = 6 * hours + 52 * minutes 
miles_run_easy = 2 * (8 * minutes + 15 * seconds)
miles_run_hard = 3 * (7 * minutes + 12 * seconds)
total_time_run = miles_run_easy + miles_run_hard + depart

hours2 = total_time_run // hours

part_hour = total_time_run % hours
minutes2 = part_hour // minutes
seconds2 = part_hour % minutes
print('Total Time Run: {}, Hours: {}, Minutes: {}, Seconds: {}'. format(total_time_run, hours2, minutes2, seconds2))
#I worked with a group on this project