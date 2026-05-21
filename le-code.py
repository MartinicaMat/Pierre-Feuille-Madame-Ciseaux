import random
import sys

def jouer_manche():
    options = ["pierre", "feuille", "madame", "ciseaux"]
    
    print("\n--- NOUVELLE MANCHE ---")
    choix_joueur = input("Choisis (pierre, feuille, madame, ciseaux) ou 'quitter' : ").lower().strip()
    
    if choix_joueur == "quitter":
        print("Merci d'avoir joue !")
        sys.exit()
        
    if choix_joueur not in options:
        print("Choix invalide ! Fais attention a l'orthographe.")
        return None

    choix_ordi = random.choice(options)
    print(f"L'ordinateur a choisi : {choix_ordi}")
    
    # Egalite
    if choix_joueur == choix_ordi:
        print("Egalite complete !")
        return "egalite"
        
    elif (
        (choix_joueur == "madame" and choix_ordi == "feuille") or
        (choix_joueur == "pierre" and choix_ordi == "madame") or
        (choix_joueur == "ciseaux" and choix_ordi == "madame") or
        (choix_joueur == "feuille" and choix_ordi == "pierre") or
        (choix_joueur == "ciseaux" and choix_ordi == "feuille")
    ):
        # Phrases personnalisees sans accent
        if choix_joueur == "madame" and choix_ordi == "feuille":
            print("Gagne ! Ta Madame a mange la feuille !")
        elif choix_joueur == "pierre" and choix_ordi == "madame":
            print("Gagne ! Ta Pierre a detruit la Madame !")
        elif choix_joueur == "ciseaux" and choix_ordi == "madame":
            print("Gagne ! Tes Ciseaux ont coupe la Madame !")
        else:
            print("Gagne ! Bien joue.")
        return "joueur"
        
    # Si c'est l'ordinateur qui gagne
    else:
        if choix_ordi == "madame" and choix_joueur == "feuille":
            print("Perdu ! La Madame de l'ordi a mange ta feuille...")
        elif choix_ordi == "pierre" and choix_joueur == "madame":
            print("Perdu ! La Pierre de l'ordi a detruit ta Madame...")
        elif choix_ordi == "ciseaux" and choix_joueur == "madame":
            print("Perdu ! Les Ciseaux de l'ordi ont coupe ta Madame...")
        else:
            print("Perdu pour cette fois !")
        return "ordi"
    
print("      Create Studios presente :")
print("=========================================")
print("    PIERRE-FEUILLE-MADAME-CISEAUX ")
print("=========================================")

score_joueur = 0
score_ordi = 0

while True:
    resultat = jouer_manche()
    
    if resultat == "joueur":
        score_joueur += 1
    elif resultat == "ordi":
        score_ordi += 1
        
    print(f"Score actuel -> Toi : {score_joueur} | Ordi : {score_ordi}")
