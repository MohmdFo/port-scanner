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
