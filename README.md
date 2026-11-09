
# Sieťové nástroje v Pythone

Dva malé skripty na kontrolu IP adries a sieťovej dostupnosti. Používajú len štandardnú knižnicu Pythonu, nie sú potrebné žiadne externé balíčky.

## Obsah repozitára

- `ip_ping.py` – pošle ping na pevne zadanú IP adresu a vypíše, či je dostupná.
- `ip_checker.py` – zistí typ IP adresy a voliteľne overí, či je na IPv4 adrese otvorený TCP port.

## Požiadavky

- Python 3.6 alebo novší
- Pre `ip_ping.py` príkaz `ping` v systéme (Linux, macOS aj Windows)

## ip_ping.py

Adresa, ktorú skript testuje, je zapísaná v premennej `ip_adresa` na začiatku súboru. Ak chceš testovať inú, zmeň jej hodnotu.

```
python ip_ping.py
```

Skript pošle 4 pingy. Výstup príkazu `ping` sa zobrazí v termináli. Na konci skript vypíše jedno z týchto hlásení:

- `Sieť funguje, IP je aktívna.` – ping uspel
- `IP nie je dostupná.` – ping zlyhal

Ak ping nedokončí do 20 sekúnd, skript ho ukončí a vypíše, že vypršal časový limit.

## ip_checker.py

```
python ip_checker.py <IP> [port]
```

Príklady a skutočný výstup:

```
$ python ip_checker.py 192.168.1.1
192.168.1.1: súkromná

$ python ip_checker.py 8.8.8.8
8.8.8.8: verejná

$ python ip_checker.py 127.0.0.1 22
127.0.0.1: súkromná, loopback
Port 22: zatvorený alebo filtrovaný
```

Typy adries, ktoré skript rozlišuje:

- **súkromná** – napríklad `192.168.1.1` alebo `10.0.0.5`
- **loopback** – `127.0.0.1` (adresa samotného počítača); je označená aj ako súkromná
- **verejná** – napríklad `8.8.8.8`

Port sa overuje TCP pripojením (len IPv4) s časovým limitom 1 sekunda:

- **otvorený** – pripojenie sa podarilo
- **zatvorený alebo filtrovaný** – pripojenie zlyhalo; port môže byť zatvorený, alebo ho blokuje firewall

Skript skončí s návratovou hodnotou `0` pri úspechu a `1` pri chybe. Pri chýbajúcom argumente vypíše návod na použitie a skončí s hodnotou `2`.

## Obmedzenia

- `ip_ping.py`: ak firewall blokuje ICMP (ping), skript môže hlásiť, že zariadenie nie je dostupné, aj keď je.
- `ip_ping.py`: adresa je pevne zapísaná v kóde, zámerne, aby sa do príkazu `ping` nedalo vložiť nič iné.
- `ip_checker.py`: podporované sú len IPv4 adresy pri overovaní portu. IPv6 adresy sa dajú zistiť, ale port sa pri nich neoverí.
- `ip_checker.py`: názvy domén nie sú podporované, len IP adresy.
- `ip_checker.py`: rozdiel medzi zatvoreným a filtrovaným portom skript nerozlišuje. V pomalých sieťach môže časový limit 1 sekunda dať výsledok „zatvorený“, aj keď je port otvorený.

## Upozornenie

Porty overuj len na zariadeniach, ktoré sú tvoje, alebo na ktorých máš súhlas správcu.
