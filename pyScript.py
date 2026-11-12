import psutil 
import urllib.request
import json

url = "http://localhost:8085/data.json"

# functions to convert bytes info to GiB
def convert_to_gib(bytes_value):
    return bytes_value / 1024**3

# main function
def main():
    # CPU Usage
    cpu_usage = psutil.cpu_percent(interval=1) 
    
    # Memory RAM Info
    memory = psutil.virtual_memory()
    
    # Read the JSON in Python
    with urllib.request.urlopen(url) as response:
        data = json.load(response)
    
    print (f"CPU USAGE: {cpu_usage}%")
    print (f"RAM Percentage: {memory.percent}%")
    print (f"TOTAL RAM: {convert_to_gib(memory.total):.2f} GiB")
    print (f"USED RAM: {convert_to_gib(memory.used):.2f} GiB")
    print (f"AVAILABLE RAM: {convert_to_gib(memory.available):.2f} GiB")
    
    # CPU temperature
    cpu = data["Children"][0]["Children"][1]
    for category in cpu["Children"]:
        if category["Text"] == "Temperatures":
            for sensor in category["Children"]:
                if sensor ["Text"] == "CPU Package":
                 print(f"CPU Temperature: {sensor["Value"]}")
    
    
if __name__ == "__main__":
    main()