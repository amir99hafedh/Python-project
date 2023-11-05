#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re
# Fonction pour vérifier si l'e-mail est valide
def valid_email(email):
    # Utilisation d'une expression régulière pour valider l'e-mail
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_pattern, email) is not None

# Fonction pour vérifier si le mot de passe est valide
def valid_pwrd(password):
    # Utilisation d'expressions régulières pour vérifier les contraintes du mot de passe
    password_pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&+=]).{8,}$'
    return re.match(password_pattern, password) is not None

# Fonction d'enregistrement
def enregistrer():
    email = input("Entrez votre adresse e-mail : ")
    if valid_email(email):
        password = input("Entrez votre mot de passe : ")
        if valid_pwrd(password):
            # Enregistrement de l'e-mail et du mot de passe
            print("Enregistrement réussi !")
        else:
            print("Le mot de passe ne respecte pas les contraintes.")
    else:
        print("L'adresse e-mail n'est pas valide.")

# Appel de la fonction d'enregistrement
enregistrer()

