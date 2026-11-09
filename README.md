
# Sieťové nástroje v Pythone

Dva malé skripty na kontrolu IP adries a sieťovej dostupnosti. Používajú len štandardnú knižnicu Pythonu.

## Skripty

- `ip_ping.py`: pošle ping na pevne zadanú IP adresu a podľa odpovede vypíše, či je dostupná.
- `ip_checker.py`: zistí typ IP adresy a overí, či je na zadanej adrese otvorený TCP port.

## Požiadavky

- Python 3.6 alebo novší
- Pre `ip_ping.py` príkaz `ping` v systéme (je na Linuxe, macOS aj Windows)
- Žiadne externé knižnice

## ip_ping.py

Skript pingne adresu `142.251.211.78`, ktorá je zapísaná priamo v kóde. Ak ping uspeje, vypíše:

```
Siet funguje, IP je aktivna.
```

Ak ping neuspeje, skript nevypíše nič. Výstup samotného príkazu `ping` sa zobrazí v termináli.

```bash
python ip_ping.py
```

Skript zavolá systémový príkaz `ping` cez `os.system()`. Návratová hodnota `0` znamená, že ping uspel. Iný cieľ nastavíš zmenou premennej `ip_adresa`.

## ip_checker.py

Skript dostane IP adresu ako argument, vypíše jej typ a voliteľne overí port.

```bash
python ip_checker.py <IP> [port]
```

Príklady:

```bash
python ip_checker.py 192.168.1.1
python ip_checker.py 127.0.0.1 22
```

Pre `192.168.1.1` skript vypíše:

```
192.168.1.1: súkromná
```

Pre `127.0.0.1 22` vypíše typ adresy a stav portu, napríklad:

```
127.0.0.1: súkromná, loopback
Port 22: zatvorený alebo filtrovaný
```

Typy adries:

- **súkromná**: napríklad `192.168.1.1` alebo `10.0.0.5`
- **loopback**: `127.0.0.1`, ktorá je zároveň označená aj ako súkromná
- **verejná**: napríklad `8.8.8.8`

Port sa overuje pripojením cez TCP (IPv4) s časovým limitom 1 sekunda. Stav „otvorený“ znamená, že pripojenie sa podarilo. Stav „zatvorený alebo filtrovaný“ môže znamenať, že port je zatvorený alebo že ho firewall blokuje.

## Známe obmedzenia

- `ip_ping.py`: príkaz `ping` bez počtu pingov na Linuxe a macOS beží donekonečna, kým ho nezastavíš cez Ctrl+C. Na Windows pošle štyri pingy a skončí sám.
- `ip_ping.py`: ak firewall blokuje ICMP, skript môže hlásiť, že zariadenie nie je dostupné, aj keď je.
- `ip_ping.py`: ak by sa adresa zadávala z klávesnice, namiesto `os.system()` použi modul `subprocess`, aby sa do príkazu nedalo vložiť nič neočakávané.
- `ip_checker.py`: port sa overuje len cez IPv4, IPv6 adresy nie sú podporované.
- `ip_checker.py`: port musí byť celé číslo, inak skript skončí chybou. Ak názov domény neexistuje, skript tiež skončí chybou.
- `ip_checker.py`: argumenty nad rámec IP a portu sa ignorujú.

## Možná úprava ip_ping.py

Aktuálna verzia nemá počet pingov ani hlásenie pri neúspechu. Ak ich chceš doplniť, uprav skript takto:

```python
import os

ip_adresa = "142.251.211.78"
odpoved = os.system("ping -c 4 " + ip_adresa)

if odpoved == 0:
    print("Siet funguje, IP je aktivna.")
else:
    print("IP nie je dostupna.")
```

Na Windows použi `ping -n 4`. Po tejto úprave odstráň z obmedzení riadok o nekonečnom pingu.
