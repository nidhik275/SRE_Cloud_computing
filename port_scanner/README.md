# 🔍 Port Scanner Script

## 🧾 Overview

This Python script is a simple **port scanner** 🧠 that checks whether a specified port is open on a given remote host 🌐. It connects to the specified host and port, and returns whether the port is open ✅ or not ❌. It also includes error handling ⚠️ to manage potential DNS resolution issues or network connection failures.

---

## ✨ Features

- 🎯 Scans a specified port on a remote host.
- 🛑 Gracefully exits on keyboard interrupt or error.
- 🧱 Handles common socket exceptions like DNS resolution and connection errors.

---

## 📦 Requirements

- **Python 3.x** 🐍  
  The script is written in Python 3, so make sure it is installed.

✅ Built-in libraries used:
- `socket` 🔌
- `sys` 🧠
- `os` 🗂️

_No external dependencies required._

---

## ⚙️ Usage

### ▶️ Steps to Run the Script

1. ⬇️ Clone or download the repository containing the script.
2. 💻 Open a terminal and navigate to the directory where the script is located.
3. ▶️ Run the script:

   ```bash
   python port_scanner.py
   ```
4.	🧾 When prompted, enter:
	•	A remote hostname (e.g., google.com, 8.8.8.8)
	•	A port number (e.g., 80 for HTTP, 443 for HTTPS)

5. You should see an output like below for the provided input:
   ```bash
    Enter remote hostnam: speedtest.net
    Enter the port to be scanned: 443
    --------------------
    Scanning ports...
    --------------------
    443 is open on host speedtest.net with IP 151.101.194.219
---

## 🚨 Error Handling

The script handles the following exceptions:
	•	⌨️ KeyboardInterrupt: Pressing Ctrl+C exits the program gracefully.
	•	🌐 socket.gaierror: Triggered when hostname cannot be resolved.
	•	🔒 socket.error: When connection fails due to unreachable host or firewall block.

---
## 👩‍💻 Author

Nidhi Kumari
📅 Date: 24/04/25

