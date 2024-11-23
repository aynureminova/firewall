import socket
import argparse

def scan_ports(target_ip, start_port, end_port):
    print(f"Scanning ports {start_port}-{end_port} on {target_ip}...")
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Ayarlayabilirsiniz, bir saniyeden daha uzun süren bağlantı girişimlerini zaman aşımına uğratır
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            print(f"Port {port} is open.")
        sock.close()

def main():
    parser = argparse.ArgumentParser(description="Simple Network Scanner")
    parser.add_argument("192.168.0.1", help="Target IP address")
    parser.add_argument("start_port", type=int, help="Start port number")
    parser.add_argument("end_port", type=int, help="End port number")
    args = parser.parse_args()

    target_ip = args.target_ip
    start_port = args.start_port
    end_port = args.end_port

    scan_ports(target_ip=192.168.1.1 , start_port=1, end_port=100)

if __name__ == "__main__":
    main()
