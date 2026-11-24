# Python System Monitor

## Project Overview

A Python-based system monitoring application that automatically collects CPU and RAM measurements, timestamps them and stores them in a CSV file for further analysis.

The project was developed to move beyond learning Python programming concepts in isolation and apply them to a practical application. It also establishes a foundation for future data engineering projects involving data ingestion, transformation and storage.

## Features

- Real-time CPU usage monitoring.
- CPU temperature retrieval through LibreHardwareMonitor.
- RAM usage, total, used and available memory monitoring.
- Memory conversion from bytes to gibibytes (GiB).
- Automatic date and time recording.
- Continuous data collection with a configurable delay.
- Persistent CSV storage without duplicate headers.
- Exception handling for connection failures.
- Automatic resumption of temperature collection when the connection is restored.
- Graceful shutdown using Ctrl+C.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| psutil | CPU usage and RAM measurements |
| LibreHardwareMonitor | CPU temperature monitoring |
| urllib.request | HTTP communication |
| JSON | Reading and parsing sensor data |
| CSV | Persistent data storage |
| datetime | Timestamp generation |
| os | File size checking |
| time | Collection delay |
| Git and GitHub | Version control |

## How It Works

1. Collects CPU usage and RAM measurements using psutil.
2. Retrieves CPU temperature through LibreHardwareMonitor's local HTTP server.
3. Converts memory measurements from bytes to GiB and rounds them to two decimal places.
4. Generates a date and time for each record.
5. Combines the measurements into a single Python dictionary.
6. Appends the record to a CSV file.
7. Waits for the configured collection delay before repeating the process.

## Installation and Usage

### Prerequisites

- Python 3
- Windows
- LibreHardwareMonitor

### Setup

Install the required Python dependency:

```bash
pip install psutil
```

Download LibreHardwareMonitor from its official repository:

https://github.com/LibreHardwareMonitor/LibreHardwareMonitor

Launch LibreHardwareMonitor and enable its web server using port 8085.

Ensure that the following endpoint is accessible:

```text
http://localhost:8085/data.json
```

Run the Python script from the terminal.

Press Ctrl+C to stop monitoring.

## Configuration

The application uses three configuration constants:

```python
URL = "http://localhost:8085/data.json"
CSV_FILE = "system_monitor.csv"
COLLECTION_DELAY = 5
```

These allow the data source URL, output filename and collection delay to be modified without changing the core application logic.

## Example Output

The application generates a CSV file containing the following structure:

```csv
cpu_usage,cpu_temp,ram_percentage,total_ram,used_ram,available_ram,date,time
24.7,50.0 °C,91.7,7.72,7.07,0.64,24-11-2026,13:44:11
12.6,50.0 °C,89.4,7.72,6.90,0.82,24-11-2026,13:44:17
```

CPU usage and RAM percentage are recorded as percentages. Memory measurements are recorded in GiB, and CPU temperature is recorded in degrees Celsius.

## Error Handling

If LibreHardwareMonitor becomes unavailable, the application handles specified connection errors and continues collecting CPU usage, RAM measurements and timestamps.

Unavailable CPU temperature readings are represented by `None` in Python and stored as empty fields in the CSV file.

Temperature collection resumes automatically when the connection becomes available again.

## Testing

The application was manually tested against the following scenarios:

- Normal hardware data collection.
- CSV creation and continuous record appending.
- Prevention of duplicate CSV headers.
- LibreHardwareMonitor connection failure.
- Connection restoration during monitoring.
- Continuous automated execution.
- Graceful shutdown using Ctrl+C.

## Key Learning Outcomes

Through developing this project, I gained practical experience in:

- Applying Python fundamentals to a functional application.
- Retrieving data from multiple sources.
- Making HTTP requests and navigating nested JSON data.
- Processing and combining structured data.
- Working with files and persistent storage.
- Implementing exception handling and graceful shutdown.
- Automating repetitive tasks.
- Applying separation of concerns and refactoring code for maintainability.

## Current Limitations

- CPU temperature monitoring depends on LibreHardwareMonitor.
- Sensor navigation is based on the JSON structure of the development machine and may require adjustment for different hardware.
- The collection delay does not guarantee an exact sampling interval because processing and HTTP requests also require time.
- The application does not currently handle every possible error, such as malformed JSON.
- Monitoring requires the script to be manually launched.

## Future Development

The next stage of this project will focus on developing a data engineering pipeline using the collected hardware measurements.

Planned development includes:

- Data cleaning and validation.
- Handling missing values and inconsistent data formats.
- Creating derived measurements.
- Loading processed data into a relational database.
- Querying and analysing historical system performance using SQL.

These features are planned extensions and are not part of the current implementation.
