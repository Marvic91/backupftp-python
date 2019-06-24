# backupftp-python
Script Python de backup via FTP (utilisant le module ftplib).

Dans le cadre de ma formation Openclassrooms, j'ai écrit un script Python afin d'effectuer le backup d'un fichier donné, sur un serveur FTP.

Le script permet de définir un dossier de backup dit "racine" puis à chaque backup, le script viendra creer un sous dossier avec la date et l'heure du backup, permettant de creer un historique de backup.

Il affiche également quelques informations (date, message de bienvenue du FTP, contenu des dossiers avant et après backup...)

Ce script peut-être automatisable, avec un gestionnaire de tâches.

Le script est conçu de façon assez modulable, l'ensemble des éléments de paramétrages sont des variables (adresse ftp, login/password, fichier à sauvergarder, dossier racine d'upload).

A vous de modifier les variables selon votre souhait.

Le script utilise une condition permettant de vérifier que le fichier à backuper existe bien, et vous informe si ce n'est pas le cas.

Olivier IGUAL
