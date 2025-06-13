# Ghost Port Scanner

*A colorful, fast port scanner written in Python with a sleek terminal UI.*

---

## Description

**Ghost Port Scanner** is a simple, multi-threaded port scanning tool designed to scan a range of TCP ports on a specified host. It features:

* Colorful and stylish terminal output using `colorama` and `fade`.
* Fast scanning with multithreading (`ThreadPoolExecutor`).
* Displays your local IP address at startup.
* Pause on open ports for user interaction.
* Cross-platform clearing of terminal screen.

---

## Features

* Scan a custom range of ports on any reachable host.
* Friendly, colored output to highlight open and closed ports.
* Uses Python’s standard socket library for network interactions.
* Simple interface with an ASCII art banner for fun.

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/ghost-port-scanner.git
cd ghost-port-scanner
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Requirements

* Python 3.6+
* `colorama`
* `fade`

---

## Usage

Run the script:

```bash
python ghost_port_scanner.py
```

Follow the prompts to:

* Enter the target host (IP address or domain).
* Enter the start port.
* Enter the end port.

The scanner will display which ports are open. When an open port is found, the program pauses, allowing you to see the result before continuing.

---

## Example

```plaintext
                    Your IP Address is: 192.168.1.10

                    [?] Enter the host to scan: scanme.nmap.org

                    [?] Enter the start port: 20

                    [?] Enter the end port: 30

                    [i] Scanning ports 20 to 30 on host scanme.nmap.org...

                    [+] Port 22 is open on scanme.nmap.org
```

---

## How it works

The program uses threads to scan ports concurrently, speeding up the scanning process. For each port, it attempts to establish a TCP connection:

* If the connection succeeds, the port is open.
* If it times out or refuses connection, the port is considered closed.

---

## Notes

* Running port scans may require administrative privileges.
* Use responsibly and only scan hosts you have permission to test.
* The program clears the screen at startup and after each scan restart.

---

## License

MIT License
