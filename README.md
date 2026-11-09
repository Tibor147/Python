# Python
IP Checker

Malý nástroj v Pythone, ktorý zistí typ IP adresy (súkromná, verejná, loopback) a overí, či je na zadanej adrese otvorený TCP port.

## Požiadavky

- Python 3.8 alebo novší
- Žiadne externé knižnice

## Spustenie

```bash
python ip_checker.py 192.168.1.1
python ip_checker.py 127.0.0.1 22
```

Prvý príklad vypíše typ adresy. Druhý navyše skontroluje port 22 na lokálnom počítači.

## Upozornenie

Kontrolu portov spúšťaj len na zariadeniach, ktoré vlastníš, alebo na ktoré máš povolenie.
