import csv
import random
from datetime import datetime, timedelta

# --- Function to generate random datetime between two datetimes ---
def random_datetime(start, end):
    delta = end - start
    random_seconds = random.randint(0, int(delta.total_seconds()))
    return start + timedelta(seconds=random_seconds)

# --- Get user input ---
print("=== CSV Event Data Generator ===")

# Timestamp range
start_date_str = input("Enter start date (YYYY-MM-DD HH:MM:SS): ")
end_date_str = input("Enter end date (YYYY-MM-DD HH:MM:SS): ")
start_date = datetime.strptime(start_date_str, "%Y-%m-%d %H:%M:%S")
end_date = datetime.strptime(end_date_str, "%Y-%m-%d %H:%M:%S")

# Battery range
battery_min = int(input("Enter minimum battery percent (0-100): "))
battery_max = int(input("Enter maximum battery percent (0-100): "))

# Duration range for AC and DC
ac_min = int(input("Enter minimum duration (seconds) for AC: "))
ac_max = int(input("Enter maximum duration (seconds) for AC: "))
dc_min = int(input("Enter minimum duration (seconds) for DC: "))
dc_max = int(input("Enter maximum duration (seconds) for DC: "))

# Number of events
num_records = int(input("How many records do you want to generate? "))

# --- Generate data ---
records = []
for i in range(num_records):
    event = random.choice(["AC", "DC"])
    battery_percent = random.randint(battery_min, battery_max)
    timestamp = random_datetime(start_date, end_date)
    
    if event == "AC":
        duration = random.randint(ac_min, ac_max)
    else:
        duration = random.randint(dc_min, dc_max)
    
    records.append([timestamp.strftime("%Y/%m/%d %H:%M:%S"), event, battery_percent, duration])

# --- Write to CSV file ---
filename = "event_data.csv"
with open(filename, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp", "Event", "BatteryPercent", "Duration"])
    writer.writerows(records)

print(f"\n✅ CSV file '{filename}' generated successfully with {num_records} records!")
