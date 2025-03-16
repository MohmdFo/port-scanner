import socket
import unittest
from unittest.mock import MagicMock, patch

from scapy.all import TCP

from port_scanner.scanner import PortScanner


class TestPortScannerSocketMethods(unittest.TestCase):
    @patch("port_scanner.scanner.socket.socket")
    def test_is_port_open_socket_success(self, mock_socket):
        # Create a mock socket instance that simulates a successful connection.
        instance = MagicMock()
        mock_socket.return_value = instance

        scanner = PortScanner("127.0.0.1", 80, 80)
        self.assertTrue(scanner.is_port_open_socket(80))
        instance.connect.assert_called_once_with(("127.0.0.1", 80))
        instance.close.assert_called_once()

    @patch("port_scanner.scanner.socket.socket")
    def test_is_port_open_socket_failure(self, mock_socket):
        # Simulate a socket connection failure.
        instance = MagicMock()
        instance.connect.side_effect = Exception("Connection error")
        mock_socket.return_value = instance

        scanner = PortScanner("127.0.0.1", 80, 80)
        self.assertFalse(scanner.is_port_open_socket(80))


class TestScanPortsSocket(unittest.TestCase):
    def test_scan_ports_socket(self):
        # Override is_port_open_socket to simulate open port only on port 80.
        scanner = PortScanner("127.0.0.1", 80, 82)
        scanner.is_port_open_socket = lambda port: port == 80
        self.assertEqual(scanner.scan_ports_socket(), [80])


class TestScanPortsScapy(unittest.TestCase):
    @patch("port_scanner.scanner.sr1")
    def test_scan_ports_scapy(self, mock_sr1):
        # Dummy response object for scapy simulation.
        class DummyResponse:
            def __init__(self, flags):
                self._flags = flags

            def haslayer(self, layer):
                return True

            def getlayer(self, layer):
                # Simulate a TCP layer with flags attribute.
                return type("DummyTCP", (), {"flags": self._flags})

        # Side effect function to simulate responses.
        def side_effect(pkt, timeout, verbose):
            port = pkt[TCP].dport
            # Simulate that only port 80 responds with SYN-ACK (flag 0x12).
            if port == 80:
                return DummyResponse(0x12)
            return None

        mock_sr1.side_effect = side_effect

        scanner = PortScanner("127.0.0.1", 80, 82)
        self.assertEqual(scanner.scan_ports_scapy(), [80])
