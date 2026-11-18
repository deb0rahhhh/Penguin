import psutil 
import urllib.request
import json

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
        #print (cpu_usage)
    
    # CPU Temperature
        cpu_temp = data["Children"][0]["Children"][1]
        
        for category in cpu_temp["Children"]:
            if category["Text"] == "Temperatures":
                for sensor in category["Children"]:
                    if sensor ["Text"] == "CPU Package":
                     print(sensor["Value"])
    
    # cpu dict
        cpu_measurements = {
            "cpu_usage": cpu_usage,
            "cpu_temp": cpu_temp
        }
        return cpu_measurements
        print(cpu_info())

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
    print(memory_info())

# main function that coordinates the script
def main(): 
    cpu_data = cpu_info()
    print(cpu_data)
    ram_data= memory_info()
    print(ram_data)
       
if __name__ == "__main__":
    main()