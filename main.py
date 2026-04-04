# Verenpaineen mittauksen keskiarvot 

def main():
    yla_aamu = [121, 119, 124, 117, 118, 115, 119]
    yla_ilta = [135, 125, 112, 125, 110]
    ala_aamu = [92, 71, 80, 82, 75, 70, 78]
    ala_ilta = [79, 78, 76, 85, 73]

    yla_paine_aamu = 0
    yla_paine_ilta = 0
    ala_paine_aamu = 0
    ala_paine_ilta = 0
    
    for paine in yla_aamu:
        yla_paine_aamu += paine
    
    for paine in yla_ilta:
        yla_paine_ilta += paine
    
    for paine in ala_aamu:
        ala_paine_aamu += paine
    
    for paine in ala_ilta:
        ala_paine_ilta += paine

    avg_yla_aamu = yla_paine_aamu / len(yla_aamu)
    avg_yla_ilta = yla_paine_ilta / len(yla_ilta)
    avg_ala_aamu = ala_paine_aamu / len(ala_aamu)
    avg_ala_ilta = ala_paine_ilta / len(ala_ilta)
    avg_yla = (yla_paine_aamu + yla_paine_ilta) / (len(yla_aamu) + len(yla_ilta))
    avg_ala = (ala_paine_aamu + ala_paine_ilta) / (len(ala_aamu) + len(ala_ilta))

    print(f"Keskiverto yläpaine aamulla: {round(avg_yla_aamu)}")
    print(f"Keskiverto yläpaine illalla: {round(avg_yla_ilta)}")
    print(f"Keskiverto alapaine aamulla: {round(avg_ala_aamu)}")
    print(f"Keskiverto alapaine illalla: {round(avg_ala_ilta)}")

    print(f"Keskiverto yläpaine: {round(avg_yla)}")
    print(f"keskiverto alapaine: {round(avg_ala)}")

main()

def update_values():
    pass
