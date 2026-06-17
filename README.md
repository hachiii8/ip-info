# ip-info

A simple command-line tool to get information about any IP address using ipinfo.io.

## Features

- Lookup any IP address or domain
- Shows city, region, country, ISP, timezone
- Auto-detects your own IP if none provided
- No external dependencies

## Usage

```bash
# Check your own IP
python ipinfo.py

# Check a specific IP
python ipinfo.py 8.8.8.8

# Check another IP
python ipinfo.py 1.1.1.1
```

## Example Output

```
========================================
        IP INFORMATION
========================================
  IP        : 8.8.8.8
  Hostname  : dns.google
  City      : Mountain View
  Region    : California
  Country   : US
  Location  : 37.4056,-122.0775
  ISP/Org   : AS15169 Google LLC
  Timezone  : America/Los_Angeles
========================================
```

## Requirements

- Python 3.x
- Internet connection
