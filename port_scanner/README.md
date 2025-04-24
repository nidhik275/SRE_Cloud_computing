# Port Scanner Script

## Overview

This Python script is a simple **port scanner** that checks whether a specified port is open on a given remote host. It connects to the specified host and port, and returns whether the port is open or not. It also includes error handling to manage potential DNS resolution issues or network connection failures.

---

## Features

- Scans a specified port on a remote host and gracefully exits if there is an intrupt or an error.
- Handles common socket exceptions such as DNS resolution failure and connection errors.

---

## Requirements

- **Python 3.x**: The script is written in Python 3, so Python 3.x must be installed.
- The script uses the built-in libraries:
  - `socket`
  - `sys`
  - `os`

No additional dependencies are required.

---

## Usage

### Steps to run the script:

1. Clone or download the repository containing the script.
2. Open a terminal and navigate to the directory where the script is located.
3. Run the script with the following command:

   ```bash
   python port_scanner.py

4. When prompted, enter the remote hostname (e.g., google.com or 8.8.8.8).
5. Enter the port number you want to scan (e.g., 80 for HTTP, 443 for HTTPS).
6. You should see an output like belowfor the provided input:
   ```bash
    Enter remote hostnam: speedtest.net
    Enter the port to be scanned: 443
    --------------------
    Scanning ports...
    --------------------
    443 is open on host speedtest.net with IP 151.101.194.219
---

## Error Handling

Possible exceptions handled by the script:

- **KeyboardInterrupt**: If you press Ctrl+C, the script will print a message and exit gracefully.
- **socket.gaierror**: If the hostname cannot be resolved (DNS issues), the script will exit with an error message.
- **socket.error**: If the connection to the remote host or port fails (e.g., host is down or firewall is blocking the connection), the script will display an appropriate error message.

---

### Author: Nidhi Kumari  
### Date: 24/04/25
