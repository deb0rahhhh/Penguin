import psutil 
import urllib.request
import json

url = "http://localhost:8085/data.json"

# functions to convert bytes info to GiB
def convert_to_gib(bytes_value):
    return bytes_value / 1024**3

# function for CPU
def cpu_info():
     # Read the JSON in Python
        with urllib.request.urlopen(url) as response:
            data = json.load(response)
    
    # CPU Usage
        cpu_usage = psutil.cpu_percent(interval=1)
        print (f"CPU USAGE: {cpu_usage}%")
    
    # CPU Temperature
        cpu = data["Children"][0]["Children"][1]
        for category in cpu["Children"]:
            if category["Text"] == "Temperatures":
                for sensor in category["Children"]:
                    if sensor ["Text"] == "CPU Package":
                     print(f"CPU TEMPERATURE: {sensor["Value"]}")
    

# function for Memory RAM 
def memory_info():
    # Memory RAM Info
    memory = psutil.virtual_memory()
    print (f"RAM PERCENTAGE: {memory.percent}%")
    print (f"TOTAL RAM: {convert_to_gib(memory.total):.2f} GiB")
    print (f"USED RAM: {convert_to_gib(memory.used):.2f} GiB")
    print (f"AVAILABLE RAM: {convert_to_gib(memory.available):.2f} GiB")
    

# main function that coordinates the script
def main(): 
    cpu_info()
    memory_info()
       
    
if __name__ == "__main__":
    main()