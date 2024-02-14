import pandas as pd
from scapy.all import *
import platform
import os
import ipaddress
import logging
from logging.handlers import RotatingFileHandler

# Setup basic logging
log_file = 'network_scan.log'
log_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
rotating_handler = RotatingFileHandler(log_file, maxBytes=1024*1024, backupCount=5)  # Set max file size to 1 MB and keep 5 backup files
rotating_handler.setFormatter(log_formatter)
logging.basicConfig(level=logging.DEBUG, handlers=[rotating_handler])

# Add log rotation feature
def add_rotating_handler(logger):
    rotating_handler = RotatingFileHandler(log_file, maxBytes=1024*1024, backupCount=5)
    rotating_handler.setFormatter(log_formatter)
    logger.addHandler(rotating_handler)

# Add log rotation to existing loggers
add_rotating_handler(logging.getLogger())

# Rest of your code goes here...

def scan_port(ip, port):
    try:
        pkt = IP(dst=ip)/TCP(dport=port, flags="S")
        resp = sr1(pkt, timeout=2, verbose=0)

        if resp is None:
            logging.info(f"Port {port} on {ip} is filtered")
            return port, "Filtered"
        elif resp.haslayer(TCP):
            if resp.getlayer(TCP).flags == 0x12:  # SYN-ACK
                sr(IP(dst=ip)/TCP(dport=port, flags="R"), timeout=1, verbose=0)
                logging.info(f"Port {port} on {ip} is open")
                return port, "Open"
            elif resp.getlayer(TCP).flags == 0x14:  # RST-ACK
                logging.info(f"Port {port} on {ip} is closed")
                return port, "Closed"
        return port, "Unknown"
    except Exception as e:
        logging.error(f"Error scanning port {port} on {ip}: {e}")
        return port, "Error"

def export_results(scan_results, filename):
    df = pd.DataFrame(scan_results, columns=["Port", "Status"])
    try:
        if platform.system() == "Windows":
            df.to_excel(f"{filename}.xlsx", index=False)
        else:
            df.to_csv(f"{filename}.csv", index=False)
        logging.info(f"Scan results exported to {filename}")
    except Exception as e:
        logging.error(f"Failed to export scan results: {e}")

def generate_ip_range(cidr):
    try:
        network = ipaddress.ip_network(cidr, strict=False)
        return [str(ip) for ip in network.hosts()]
    except ValueError as e:
        logging.error(f"Invalid CIDR block '{cidr}': {e}")
        return []

def icmp_ping_sweep(ip_list):
    online_hosts = 0
    for ip in ip_list:
        try:
            pkt = IP(dst=ip)/ICMP()
            resp = sr1(pkt, timeout=1, verbose=0)
            if resp is None:
                logging.info(f"{ip} is down or not responding")
            elif (resp.haslayer(ICMP) and
                  resp.getlayer(ICMP).type == 3 and
                  resp.getlayer(ICMP).code in [1, 2, 3, 9, 10, 13]):
                logging.info(f"{ip} is blocking ICMP traffic")
            else:
                logging.info(f"{ip} is responding")
                online_hosts += 1
        except Exception as e:
            logging.error(f"ICMP ping sweep error on {ip}: {e}")

    logging.info(f"Total online hosts: {online_hosts}")

def scan_ip_and_ports(target_ip):
    try:
        scan_results = []

        for port in range(1, 1025):
            result = scan_port(target_ip, port)
            scan_results.append(result)

        export_results(scan_results, "scan_results")
        logging.info("Port scan completed and results exported")
    except Exception as e:
        logging.error(f"Port scanning operation error: {e}")

def main():
    try:
        while True:
            choice = input("\n1. Scan IP Address and Ports\n2. ICMP Ping Sweep\n3. Exit\nSelect an option (1, 2, or 3): ")
            if choice == "1":
                target_ip = input("Enter target IP: ")
                logging.info(f"Initiating port scan on {target_ip}")
                scan_ip_and_ports(target_ip)
            elif choice == "2":
                cidr = input("Enter network address (CIDR format, e.g., 192.168.1.0/24): ")
                ip_list = generate_ip_range(cidr)
                if ip_list:
                    logging.info(f"Performing ICMP ping sweep on {cidr}")
                    icmp_ping_sweep(ip_list)
                else:
                    print("Invalid CIDR block. Please enter a valid CIDR.")
            elif choice == "3":
                logging.info("Program exited by user.")
                break
            else:
                print("Invalid choice. Please select a valid option.")
                logging.warning("Invalid choice made in main menu.")
    except KeyboardInterrupt:
        logging.info("Operation cancelled by user.")
        print("\nOperation cancelled by user.")

if __name__ == "__main__":
    main()
