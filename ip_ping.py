"""Pošle ping na pevne zadanú IP adresu a vypíše, či je dostupná."""

import platform
import subprocess

ip_adresa = "142.251.211.78"  # zmeň na adresu, ktorú chceš otestovať
POCET_PINGOV = 4
CAKANIE_SEKUND = 20  # horný limit, aby skript nezostal visieť


def prikaz_ping(adresa: str) -> list:
    if platform.system().lower() == "windows":
        return ["ping", "-n", str(POCET_PINGOV), adresa]
    return ["ping", "-c", str(POCET_PINGOV), adresa]


def main() -> int:
    try:
        vysledok = subprocess.run(prikaz_ping(ip_adresa), timeout=CAKANIE_SEKUND)
    except FileNotFoundError:
        print("Príkaz ping sa v systéme nenašiel.")
        return 2
    except subprocess.TimeoutExpired:
        print("IP nie je dostupná (vypršal časový limit).")
        return 1

    if vysledok.returncode == 0:
        print("Sieť funguje, IP je aktívna.")
        return 0

    print("IP nie je dostupná.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
