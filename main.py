from colorama import Fore
import fade
import os
import socket
from concurrent.futures import ThreadPoolExecutor

os.system('title ghost (@17xet)')


def menu():
    ascii_banner = f"""   
             ▄▄▄·      ▄▄▄  ▄▄▄▄▄.▄▄ ·  ▄▄·  ▄▄▄·  ▐ ▄  ▐ ▄ ▄▄▄ .▄▄▄  
            ▐█ ▄█▪     ▀▄ █·•██  ▐█ ▀. ▐█ ▌▪▐█ ▀█ •█▌▐█•█▌▐█▀▄.▀·▀▄ █·
             ██▀· ▄█▀▄ ▐▀▀▄  ▐█.▪▄▀▀▀█▄██ ▄▄▄█▀▀█ ▐█▐▐▌▐█▐▐▌▐▀▀▪▄▐▀▀▄ 
            ▐█▪·•▐█▌.▐▌▐█•█▌ ▐█▌·▐█▄▪▐█▐███▌▐█ ▪▐▌██▐█▌██▐█▌▐█▄▄▌▐█•█▌
            .▀    ▀█▄▀▪.▀  ▀ ▀▀▀  ▀▀▀▀ ·▀▀▀  ▀  ▀ ▀▀ █▪▀▀ █▪ ▀▀▀ .▀  ▀
    """
    print(fade.purpleblue(ascii_banner))

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("8.8.8.8", 80))
            ip_address = s.getsockname()[0]
        print(f"                    Your IP Address is: {ip_address}")
    except Exception as e:
        print(f"                    Failed to retrieve IP Address: {e}")


def scan_port(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((host, port))
            if result == 0:
                print(f"\n{Fore.LIGHTGREEN_EX}                    [+]{Fore.RESET} Port {port} is open on {host}")
                os.system("pause")
                main()
    except Exception as e:
        print(f"\n{Fore.LIGHTRED_EX}                    [-]{Fore.RESET} Error scanning port {port}: {e}")
        os.system("pause")
        main()


def main():
    os.system("cls" if os.name == "nt" else "clear")
    menu()

    host = input(f"\n{Fore.CYAN}                    [?]{Fore.RESET} Enter the host to scan: ")
    start_port = int(input(f"\n{Fore.CYAN}                    [?]{Fore.RESET} Enter the start port: "))
    end_port = int(input(f"\n{Fore.CYAN}                    [?]{Fore.RESET} Enter the end port: "))

    print(f"\n{Fore.BLUE}                    [i]{Fore.RESET} Scanning ports {start_port} to {end_port} on host {host}...")

    with ThreadPoolExecutor(max_workers=50) as executor:
        for port in range(start_port, end_port + 1):
            executor.submit(scan_port, host, port)


if __name__ == "__main__":
    main()
