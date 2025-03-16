import socket

from scapy.all import IP, TCP, sr1


class PortScanner:
    def __init__(self, target_ip, start_port, end_port, timeout=1):
        self.target_ip = target_ip
        self.start_port = start_port
        self.end_port = end_port
        self.timeout = timeout

    def is_port_open_socket(self, port):
        """Check if a port is open using socket."""
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(self.timeout)
        try:
            s.connect((self.target_ip, port))
            s.close()
            return True
        except Exception:
            return False

    def scan_ports_socket(self):
        """Scan ports using socket connection."""
        open_ports = []
        for port in range(self.start_port, self.end_port + 1):
            if self.is_port_open_socket(port):
                open_ports.append(port)
        return open_ports

    def scan_ports_scapy(self):
        """Scan ports using scapy by sending SYN packets.
        Note: Running scapy functions often requires elevated privileges.
        """
        open_ports = []
        for port in range(self.start_port, self.end_port + 1):
            pkt = IP(dst=self.target_ip) / TCP(dport=port, flags="S")
            resp = sr1(pkt, timeout=self.timeout, verbose=0)
            if resp is not None and resp.haslayer(TCP):
                # Check if SYN-ACK is received (flag 0x12)
                if resp.getlayer(TCP).flags == 0x12:
                    open_ports.append(port)
        return open_ports
