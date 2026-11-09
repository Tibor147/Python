
import ipaddress
import socket
import sys


def over_ip(adresa: str) -> str:
    try:
        ip = ipaddress.ip_address(adresa)
    except ValueError:
        return f"{adresa} nie je platná IP adresa"

    typy = []
    if ip.is_private:
        typy.append("súkromná")
    if ip.is_loopback:
        typy.append("loopback")
    if ip.is_global:
        typy.append("verejná")
    return f"{adresa}: {', '.join(typy) or 'iná'}"


def over_port(host: str, port: int, timeout: float = 1.0) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        return s.connect_ex((host, port)) == 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Použitie: python ip_checker.py <IP> [port]")
        sys.exit(1)

    adresa = sys.argv[1]
    print(over_ip(adresa))

    if len(sys.argv) == 3:
        port = int(sys.argv[2])
        stav = "otvorený" if over_port(adresa, port) else "zatvorený alebo filtrovaný"
        print(f"Port {port}: {stav}")
