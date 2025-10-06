# Convert the time entered in hh, min and sec into seconds

hour= int(input("Enter the time in hour:"))
min= int(input("Enter the time in min:"))
sec= int(input("Enter the time in sec:"))

total_sec= (hour *3600) + (min * 60) + sec

print(F"Conversion of given time {hour} hour, {min} min & {sec} sec is {total_sec}.")