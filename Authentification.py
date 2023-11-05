#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import hashlib


def authenticate(email, password):
    with open("Enregistrement.txt", "r") as file:
        for line in file:
            stored_email, stored_password = line.strip().split(',')
            if email == stored_email and hashlib.sha256(password.encode()).hexdigest() == stored_password:
                return True
    return False

# Fonction pour s'enregistrer
def register(email, password):
    with open("Enregistrement.txt", "a") as file:
        file.write(f"{email},{hashlib.sha256(password.encode()).hexdigest()}\n")

# Menu principal
while True:
    print("Menu principal:")
    print("1. Authentification")
    print("2. Quitter")

    choice = input("Choisissez une option (1/2): ")

    if choice == "1":
        email = input("Entrez votre adresse e-mail : ")
        password = input("Entrez votre mot de passe : ")

        if authenticate(email, password):
            print("Authentification réussie !")
            while True:
                print("\nMenu après authentification:")
                print("A. Hachage")
                print("B. Décalage par CESAR")
                print("C. Collecter une Dataset")
                print("D. Retour au menu principal")

                option = input("Choisissez une option (A/B/C/D): ")

                if option == "A":
                    print("1. Haché le mot par sha256")
                    print("2. Attaquer par dictionnaire le mot inséré")
                    print("3. Retour au menu après authentification")
                    
                    choice_a = input("Choisissez une option (1/2/3): ")
                    if choice_a == "1":
                        word = input("Entrez le mot à hacher : ")
                        hashed_word = hashlib.sha256(word.encode()).hexdigest()
                        print(f"Résultat du hachage : {hashed_word}")
                    elif choice_a == "2":
                        # Ajouter la logique de l'attaque par dictionnaire ici
                        pass
                    elif choice_a == "3":
                        break
                    else:
                        print("Option invalide.")
                        
                elif option == "B":
                    print("1. Donnez un mot à chiffrer")
                    print("2. Chiffrer le message (1)")
                    print("3. Déchiffrer le message (2)")
                    print("4. Retour au menu après authentification")
                    
                    choice_b = input("Choisissez une option (1/2/3/4): ")
                    if choice_b == "1":
                        word_to_encrypt = input("Entrez le mot à chiffrer : ")
                        # Ajouter la logique du chiffrement ici
                    elif choice_b == "2":
                        # Ajouter la logique du chiffrement du message ici
                        pass
                    elif choice_b == "3":
                        # Ajouter la logique du déchiffrement du message ici
                        pass
                    elif choice_b == "4":
                        break
                    else:
                        print("Option invalide.")
                        
                elif option == "C":
                    print("1. Affichez le Dataset sous forme de dictionnaire")
                    print("2. Afficher des courbes de votre choix")
                    print("3. Retour au menu après authentification")
                    
                    choice_c = input("Choisissez une option (1/2/3): ")
                    if choice_c == "1":
                        # Ajouter la logique pour afficher le Dataset ici
                        pass
                    elif choice_c == "2":
                        # Ajouter la logique pour afficher des courbes ici
                        pass
                    elif choice_c == "3":
                        break
                    else:
                        print("Option invalide.")
                elif option == "D":
                    break
                else:
                    print("Option invalide.")
        else:
            print("Authentification échouée. Veuillez vous enregistrer.")
            email = input("Entrez votre adresse e-mail : ")
            password = input("Entrez votre mot de passe : ")
            register(email, password)
    elif choice == "2":
        break
    else:
        print("Option invalide.")


# In[ ]:




