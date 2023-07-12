each_line = []
with open(r"c:\Users\vidit\Downloads\nyc_weather.csv") as file:
    for line in file.readlines():
        each_line.append(line.split(","))
        
                

# Q1)(i) What was the average temperature in first week of Jan?
sum = 0
for i in range(1,8):
    sum += int(each_line[i][1][:2])
average = round(sum/7, 2)
print(average)

# Q1)(ii) What was the maximum temperature in first 10 days of Jan?
cur_max = 0
for i in range(1,11):
    if int(each_line[i][1][:2]) > cur_max:
        cur_max = int(each_line[i][1][:2])
print(cur_max)

# Q2)(i) What was the temperature on Jan 9?
print(int(each_line[9][1][:2]))

# Q2)(ii) What was the temperature on Jan 4?
print(int(each_line[4][1][:2]))


### Q2 with Dict dataset
weather_dict = {}
with open(r"c:\Users\vidit\Downloads\nyc_weather.csv") as f:
    for line in f:
        tokens = line.split(',')
        day = tokens[0]
        try:
            temperature = int(tokens[1])
            weather_dict[day] = temperature
        except:
            print("Invalid temperature.Ignore the row")