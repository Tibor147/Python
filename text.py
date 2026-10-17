# 1. Načítanie podmienok zo súboru a vytvorenie slovníka zmien
pravidla = {}

with open("podmienky.txt", "r", encoding="utf-8") as f_podmienky:
    for riadok in f_podmienky:
        # Ignorujeme prázdne riadky
        if not riadok.strip():
            continue
            
        # Rozdelíme riadok podľa znaku '=>'
        if "=>" in riadok:
            stare, nove = riadok.split("=>")
            # .strip() odstráni prebytočné medzery a konce riadkov
            pravidla[stare.strip()] = nove.strip()

# 2. Načítanie dokumentu, ktorý chceme upraviť
with open("dokument.txt", "r", encoding="utf-8") as f_dokument:
    obsah_dokumentu = f_dokument.read()

# 3. Aplikovanie všetkých podmienok zo súboru
for stare_slovo, nove_slovo in pravidla.items():
    obsah_dokumentu = obsah_dokumentu.replace(stare_slovo, nove_slovo)

# 4. Uloženie upraveného textu späť do dokumentu
with open("dokument.txt", "w", encoding="utf-8") as f_dokument:
    f_dokument.write(obsah_dokumentu)

print("Dokument bol úspešne upravený podľa podmienok zo súboru.")
