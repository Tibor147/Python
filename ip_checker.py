"""Zistí typ IP adresy a voliteľne overí, či je na adrese otvorený TCP port (len IPv4)."""

import argparse
import ipaddress
import socket
import sys

PORT_TIMEOUT = 1.0  # sekundy


def over_ip(adresa: str):
    """Vráti (text_vysledku, objekt_ip) alebo (chybove_hlasenie, None)."""
    try:
        ip = ipaddress.ip_address(adresa)
    except ValueError:
        return f"{adresa} nie je platná IP adresa", None

    typy = []
    if ip.is_private:
        typy.append("súkromná")
    if ip.is_loopback:
        typy.append("loopback")
    if ip.is_global:
        typy.append("verejná")
    return f"{adresa}: {', '.join(typy) or 'iná'}", ip


def over_port(host: str, port: int, timeout: float = PORT_TIMEOUT) -> bool:
    """Vráti True, ak sa na host:port podarí otvoriť TCP spojenie."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            return s.connect_ex((host, port)) == 0
    except OSError:
        return False


def hlavny_program(argumenty=None) -> int:
    parser = argparse.ArgumentParser(description="Zistí typ IP adresy a stav TCP portu.")
    parser.add_argument("ip", help="IPv4 adresa, napríklad 192.168.1.1")
    parser.add_argument("port", nargs="?", type=int, help="TCP port na overenie (1 až 65535)")
    args = parser.parse_args(argumenty)

    vysledok, ip = over_ip(args.ip)
    print(vysledok)
    if ip is None:
        return 1

    if args.port is None:
        return 0

    if not 1 <= args.port <= 65535:
        print("Port musí byť číslo od 1 do 65535.")
        return 1

    if ip.version != 4:
        print("Overenie portu je podporované len pre IPv4 adresy.")
        return 1

    stav = "otvorený" if over_port(args.ip, args.port) else "zatvorený alebo filtrovaný"
    print(f"Port {args.port}: {stav}")
    return 0


if __name__ == "__main__":
    sys.exit(hlavny_program())
