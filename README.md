# Port Scanner

A simple Python-based tool designed to identify open ports on a target machine using both Python’s built-in socket module and the scapy library. This project demonstrates the fundamentals of port scanning and can serve as a starting point for more advanced network tools.

---

## Features

- **Socket-Based Scanning:** Uses standard Python sockets to test if ports are open.
- **Scapy-Based Scanning:** Sends SYN packets and listens for SYN-ACK replies (requires elevated privileges in most environments).
- **Configurable:** Easily specify the target IP, port range, and timeout.
- **Tested Codebase:** Includes unit tests for reliability and easy maintenance.

---

## Installation

You can install this project using **pip** or **Poetry**.

### Using pip

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/port-scanner.git
   ```
2. **Navigate to the Project Directory:**
   ```bash
   cd port-scanner
   ```
3. **Create and Activate a Virtual Environment (Recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. **Install Dependencies with pip:**
   ```bash
   pip install -r requirements.txt
   ```
   *(If you don’t have a `requirements.txt`, simply run `pip install scapy` or any other dependencies you need.)*

### Using Poetry

1. **Install Poetry** (if you haven’t already):  
   [Poetry Installation Guide](https://python-poetry.org/docs/#installation)
2. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/port-scanner.git
   ```
3. **Navigate to the Project Directory:**
   ```bash
   cd port-scanner
   ```
4. **Install Dependencies with Poetry:**
   ```bash
   poetry install
   ```
5. **Activate the Virtual Environment (Optional):**
   ```bash
   poetry shell
   ```

---

## Usage

There are two primary ways to run the port scanner:

### 1. Command-Line Execution

You can run the port scanner using either of the following commands:

- **Module Execution:**
  ```bash
  python -m main
  ```
- **Direct Script Execution:**
  ```bash
  python main.py
  ```

**Note:** To support these commands, create a `main.py` file in the root directory with the following content:

```python
from port_scanner import PortScanner


def main():
    target_ip = input("Enter target IP: ")
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))

    scanner = PortScanner(target_ip, start_port, end_port)

    print("\nScanning using socket method...")
    open_ports_socket = scanner.scan_ports_socket()
    print("Open ports (socket):", open_ports_socket)

    print("\nScanning using scapy method...")
    open_ports_scapy = scanner.scan_ports_scapy()
    print("Open ports (scapy):", open_ports_scapy)

if __name__ == "__main__":
    main()

```

When executed, you'll be prompted to enter:
1. **Target IP** (e.g., `127.0.0.1`)
2. **Start Port** (e.g., `1`)
3. **End Port** (e.g., `1024`)

The script will then perform two scans:
- **Socket-based** scan
- **Scapy-based** SYN scan

It will print out lists of open ports discovered by each method.

### 2. Importing as a Module

You can also use the `PortScanner` class directly in your Python code:

```python
from port_scanner.scanner import PortScanner

# Create a scanner instance
scanner = PortScanner(target_ip="127.0.0.1", start_port=1, end_port=1024, timeout=1)

# Socket-based scan
open_ports_socket = scanner.scan_ports_socket()
print("Open ports (socket):", open_ports_socket)

# Scapy-based scan
open_ports_scapy = scanner.scan_ports_scapy()
print("Open ports (scapy):", open_ports_scapy)
```

---

## Project Structure

```plaintext
port-scanner/
├── .gitignore
├── LICENSE
├── pyproject.toml
├── README.md
├── requirements.txt
├── main.py
├── port_scanner
│   ├── __init__.py
│   └── scanner.py
└── tests
    ├── __init__.py
    └── test_scanner.py
```

- **main.py**: Acts as the entry point for running the port scanner via `python -m main` or `python main.py`.
- **port_scanner/scanner.py**: Contains the `PortScanner` class with both socket-based and scapy-based scanning methods.
- **tests/test_scanner.py**: Unit tests for the `PortScanner` class using Python’s built-in `unittest` framework and `unittest.mock`.

---

## Running Tests

1. **Install Dependencies** (e.g., `scapy`, `unittest`).
2. **Run Tests**:
   ```bash
   python -m unittest discover tests
   ```
   or simply:
   ```bash
   python -m unittest
   ```
   from within the `port-scanner` directory.

The tests will:
- Mock socket connections to test both successful and failed connections.
- Mock `sr1` from scapy to simulate SYN-ACK responses for specific ports.

---

## Contributing

1. **Fork** the project.
2. **Create** a new branch for your feature or bug fix.
3. **Commit** your changes and push your branch.
4. **Submit** a Pull Request describing your changes.

We welcome suggestions, bug reports, and pull requests. Please ensure your code is well-tested and documented.

---

## License

This project is licensed under the [MIT License](LICENSE). Feel free to modify and distribute as permitted by the license terms.

---

**Enjoy scanning and exploring network security!** If you have any questions or suggestions, feel free to open an issue or submit a pull request.