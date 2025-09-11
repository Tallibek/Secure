import socket


#HOST = "127.0.0.1"
#PORT = "65434"

def scan_ports(host, ports):
    print(f"Skanowanie hosta {host}...")
    for port in ports:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                result = s.connect_ex((host, port))
                if result == 0:
                    print(f"Port {port} otwarty!")
        except Exception as e:
            print(f"Błąd przy porcie {port}: {e}")


if __name__ == "__main__":
    target = input("Podaj hosta (np. 127.0.0.1 lub google.com): ")
    ports_to_scan = range(1, 1025)
    scan_ports(target, ports_to_scan)



