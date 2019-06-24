# Voici un script Python qui va sauvergarder sur un serveur FTP
# un fichier choisi dans un dossier d'upload choisi
# Le script classe les sauvegardes dans un dossier daté du jour et de l'heure du transfert
# Olivier IGUAL


# On importe les modules
import ftplib
import os
from datetime import date
import time


# On transforme la date du jour et l'heure en variable
today = date.today()
date = today.strftime("%d-%m-%Y")
heure = time.strftime("%H-%M-%S")

# On défini le fichier à transferer en variable
fichier = "NOM_DU_FICHIER"
# On défini les accès FTP en variable
serveur = "VOTRE_SERVEUR"
utilisateur = "VOTRE_UTILISATEUR"
motdepasse = "VOTRE_MOTDEPASSE"
# On défini le dossier d'upload racine en variable
dossier = "/upload"
# On créé une variable pour le nommage du dossier d'upload daté et timé
dossiertrans = date + "_" + heure

# On teste si le fichier existe
if os.path.isfile(fichier):
      print("Le fichier existe bien, le backup va commencer")
      # On se connecte au FTP
      ftp = ftplib.FTP(serveur)
      ftp.login(utilisateur, motdepasse)
      # On affiche le message de bienvenue du FTP
      print(ftp.getwelcome())
      # On affiche la date et un message de confirmation
      print("Nous somme le", date)
      print("Vous êtes bien connecté au FTP !")
      # On change de dossier pour upload
      ftp.cwd(dossier)
      # On affiche le contenu du dossier
      print("Voici le contenu dossier d'upload : ")
      print(ftp.dir())
      # On créé le dossier de la date du jour puis on se place dedans
      ftp.mkd(dossiertrans)
      ftp.cwd(dossiertrans)
      # On transfers notre fichier
      fp = open(fichier, 'rb')
      ftp.storbinary('STOR %s' % os.path.basename(fichier), fp, 1024)
      fp.close()
      # On affiche le contenu du dossier journalier
      print("Voici le contenu dossier journalier après upload : ")
      print(ftp.dir())
      # On affiche le contenu du dossier racine upload
      ftp.cwd(dossier)
      print("Voici le contenu dossier de sauvegarde après upload : ")
      print(ftp.dir())
      # On quitte
      ftp.quit()

      
else:
      print("Le fichier n'existe pas, merci de vérifier dans votre dossier")
