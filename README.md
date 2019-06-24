# backupftp-python
Script Python de backup via FTP (utilisant le module ftplib).

Dans le cadre de ma formation Openclassrooms, j'ai écrit un script Python afin d'effectuer le backup d'un fichier donné, sur un serveur FTP.

Le script permet de définir un dossier de backup dit "racine" puis à chaque backup, le script viendra creer un sous dossier avec la date et l'heure du backup, permettant de creer un historique de backup.
Le script utilise une condition permettant de vérifier que le fichier à backuper existe bien, et vous informe si ce n'est pas le cas.

Il affiche également quelques informations (date, message de bienvenue du FTP, contenu des dossiers avant et après backup...)

Le script est conçu de façon assez modulable, l'ensemble des éléments de paramétrages sont des variables (adresse ftp, login/password, fichier à sauvergarder, dossier racine d'upload).

A vous de modifier les variables selon votre souhait. Voici la liste des variable à modifier :

fichier = "FICHIER_A_SAUVERGARDER"

serveur = "ADDRESSE_DE_VOTRE_SERVEUR"

utilisateur = "VOTRE_NOM_D_UTILISATEUR"

motdepasse = "VOTRE_MOTDEPASSE"

dossier = "LE_DOSSIER_RACINE_D_UPLOAD"

Il suffit donc d'éditer le script avec vos éléments de configuration, puis simplement de l'exécuter.
Ce script a été pensé pour être automatisable avec un gestionnaire de tâches.

Olivier IGUAL
