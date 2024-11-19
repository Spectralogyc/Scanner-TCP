import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(ip, port):
    """
    Scans a single port to check if it's open.
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            s.connect((ip, port))
            return f"Port {port}: OPEN"
    except (socket.timeout, ConnectionRefusedError):
        return f"Port {port}: CLOSED"

def scan_ports(ip, start_port, end_port, threads=50):
    """
    Scans a range of ports using multithreading.
    """
    print(f"Scanning {ip} from port {start_port} to {end_port}...")
    with ThreadPoolExecutor(max_workers=threads) as executor:
        results = executor.map(lambda port: scan_port(ip, port), range(start_port, end_port + 1))
    for result in results:
        if "OPEN" in result:
            print(result)

# Example usage
if __name__ == "__main__":
    target_ip = input("Enter target IP or domain: ")
    start_port = int(input("Enter starting port: "))
    end_port = int(input("Enter ending port: "))
    scan_ports(target_ip, start_port, end_port)
