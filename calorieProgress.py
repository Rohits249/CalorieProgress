# Takes in goal weight loss / weight gain per week, takes in your weight over the course of two week
# and calculates the amount of calories you need to consume to reach your goal weight loss / weight gain per week

progressInput = input("Enter your goal weight loss / weight gain per week in pounds (for loss, use -): ")
progress = float(progressInput)

weights = []
print("Enter your weight for the next two weeks. If you missed a day, skip it and hit return:")
for i in range(14):
    weight = input("Enter your weight for day " + str(i + 1) + ": ")
    if weight:
        weights.append(float(weight))
    else:
        weights.append(None)

# Filter out None values and calculate daily changes where possible
dailyChanges = []
last_valid_weight = None
last_valid_index = None

for i, weight in enumerate(weights):
    if weight is not None:
        if last_valid_weight is not None:
            # Calculate the change from the last non-None weight to the current weight
            change = weight - last_valid_weight
            # Append the change to dailyChanges
            dailyChanges.append(change)
            
        # Update last valid weight and its index
        last_valid_weight = weight
        last_valid_index = i

# Proceed only if there are valid daily changes
if dailyChanges:
    totalChange = sum(dailyChanges)
    averageDailyChange = totalChange / len(dailyChanges)
    averageWeeklyChange = averageDailyChange * 7

print("Average weekly change: " + str(round(averageWeeklyChange, 2)) + " lbs")

# Calculate the increase/decrease in daily calories needed to reach the goal weight loss / weight gain per week
# based off of totalChange
if averageWeeklyChange > progress:
    # If the average weekly change is greater than the goal, then the user needs to consume less calories
    # to reach the goal
   neeededCalories = (averageWeeklyChange - progress) * 500
   print("You need to consume " + str(round(neeededCalories, 2)) + " less calories per day to reach your goal")
else:
    # If the average weekly change is less than the goal, then the user needs to consume more calories
    # to reach the goal
    neeededCalories = (progress - averageWeeklyChange) * 500
    print("You need to consume " + str(round(neeededCalories, 2)) + " more calories per day to reach your goal")
