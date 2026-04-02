def update_values():

    yla_aamu = []
    yla_ilta = []
    ala_aamu = []
    ala_ilta = []

    answer = input("Päivitetäänkö verenpaineen arvot? KYLLÄ / EI").lower()
    if answer == "yes":
        aamu_vai_ilta = input("Aamu vai ilta arvot? AAMU / ILTA").lower()
        if aamu_vai_ilta == "aamu":
            yla_vai_ala = input("Ylä- vai alapaine? YLÄ / ALA").lower()
            if yla_vai_ala == "ylä":
                try:
                    paljonko = int(input("Paljonko oli verenpaineen ylä-arvo? NUMERO").lower())
                    yla_aamu.append(paljonko)
                except ValueError:
                    print("Kirjoita numero esim: 120")
            if yla_vai_ala == "ala":
                try:
                    paljonko = int(input("Paljonko oli verenpaineen ala-arvo? NUMERO").lower())
                    ala_aamu.append(paljonko)
                except ValueError:
                    print("Kirjoita numero esim: 120")

        if aamu_vai_ilta == "ilta": 
            yla_vai_ala = input("Ylä- vai alapaine? YLÄ / ALA").lower()
            if yla_vai_ala == "ylä":
                try:
                    paljonko = int(input("Paljonko oli verenpaineen ylä-arvo? NUMERO").lower())
                    yla_ilta.append(paljonko)
                except ValueError:
                    print("Kirjoita numero esim: 120")
            if yla_vai_ala == "ala":
                try:
                    paljonko = int(input("Paljonko oli verenpaineen ala-arvo? NUMERO").lower())
                    ala_ilta.append(paljonko)
                except ValueError:
                    print("Kirjoita numero esim: 120")
    else:
        print("Ei päivitetä")
        