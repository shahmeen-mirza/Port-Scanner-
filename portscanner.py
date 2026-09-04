import socket
import time
from concurrent.futures import ThreadPoolExecutor

open_ports = []

def scan_single_port(target_ip, port):
    try:
        rider = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        rider.settimeout(1)

        result = rider.connect_ex((target_ip, port))

        rider.close()

        if result == 0:
            print(f"[+] DISCOVERED: Port {port}/tcp is OPEN")
            open_ports.append(port)

    except socket.error:
        pass

def start_scanner():

    print("=" * 50)
    print("            PYTHON NETWORK SCANNER")
    print("=" * 50)

    target_input = input("Enter target website or IP: ")

    try:
        start_time = time.time()

        target_ip = socket.gethostbyname(target_input)

        print(f"\n 🎯 Target Resolved: {target_ip}")
        print(" 🚀 Multi-threaded engine active.")
        print("🔍 Scanning ports 1 to 500...\n")

        ports = range(1, 501)

        with ThreadPoolExecutor(max_workers=50) as executor:
            executor.map(
                lambda port: scan_single_port(target_ip, port),
                ports
            )

        scan_time = round(time.time() - start_time, 2)

        total_ports = len(ports)
        closed_ports = total_ports - len(open_ports)

        print("\n================== SCAN REPORT ==================")
        print(f"Target               : {target_input}")
        print(f"IP                   : {target_ip}")
        print(f"Total Ports Scanned  : {total_ports}")
        print(f"Open Ports           : {len(open_ports)}")
        print(f"Closed Ports         : {closed_ports}")

        if open_ports:

            print("\nPORT      STATE    SERVICE")

            for port in sorted(open_ports):

                service = "unknown"

                if port == 21:
                    service = "ftp"
                elif port == 22:
                    service = "ssh"
                elif port == 80:
                    service = "http"
                elif port == 443:
                    service = "https"

                print(f"{port}/tcp    open     {service}")

        else:
            print("\n[!] No open ports found.")

        print("-------------------------------------------------")
        print(f"Scan Duration        : {scan_time} seconds")
        print("=================================================")

    except socket.gaierror:
        print("\n[-] Invalid target. Could not resolve hostname.")

    except Exception as error:
        print("\n[-] Error:", error)

if __name__ == "__main__":
    start_scanner()
    start_scanner()
