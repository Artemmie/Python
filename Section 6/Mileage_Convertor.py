print("How many kilometers did you cycle today?")
human_input = float(input())
mileage_convertion_float = 1.60934
miles = human_input / mileage_convertion_float
print(f"That is equal to {round(miles, 2)} miles.")