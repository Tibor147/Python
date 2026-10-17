import os

ip_adresa = "142.251.211.78"
odpoved = os.system("ping " + ip_adresa + "")

if odpoved == 0:
    print("Siet funguje, IP je aktivna.")
