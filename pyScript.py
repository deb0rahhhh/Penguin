import psutil 
import urllib.request
import json
from datetime import datetime
import csv
import os

url = "http://localhost:8085/data.json"

# function to convert bytes info to GiB
def convert_to_gib(bytes_value):
    return round(bytes_value / 1024**3, 2) # round to 2dp

# function for CPU
def cpu_info():
     # Read the JSON in Python
        with urllib.request.urlopen(url) as response:
            data = json.load(response)
    
    # CPU Usage
        cpu_usage = psutil.cpu_percent(interval=1)
    
    # CPU Temperature
        cpu_temp = None
        cpu = data["Children"][0]["Children"][1]
        for category in cpu["Children"]:
            if category["Text"] == "Temperatures":
                for sensor in category["Children"]:
                    if sensor ["Text"] == "CPU Package":
                     cpu_temp = (sensor["Value"])
    
    # cpu dict
        cpu_measurements = {
            "cpu_usage": cpu_usage,
            "cpu_temp": cpu_temp
        }
        return cpu_measurements

# function for Memory RAM 
def memory_info(): 
    memory = psutil.virtual_memory()
    
    ram_measurements = {
        "ram_percentage": memory.percent,
        "total_ram": convert_to_gib((memory.total)),
        "used_ram": convert_to_gib((memory.used)),
        "available_ram": convert_to_gib((memory.available))
    }
    return ram_measurements

# function for date-time
def datetime_info():
    timestamp = datetime.now()
    date = timestamp.strftime("%d-%m-%Y") # formats the date (DD/MM/YY)
    time = timestamp.strftime("%H:%M:%S") # formats the time (hr, min, sec)
    
    date_time = {
        "date": date,
        "time": time
    }
    return date_time    

# main function that coordinates the script
def main():
    # System Record
    system_record = {**cpu_info(), **memory_info(), **datetime_info()}
    print(system_record)
    
    file_size = os.path.getsize("system_monitor.csv") 
    
    with open("system_monitor.csv", 'a', newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=system_record.keys())
        
        if file_size == 0:
            writer.writeheader()
        writer.writerow(system_record) 

if __name__ == "__main__":
    main()