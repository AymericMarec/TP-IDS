# TP-IDS

## Installation

### Python

```powershell
sudo dnf install python3
sudo dnf install python3-pip
pip install psutil
```

### Le repo

**Cloner ce repo dans /srv**

## Utilisation

### Conf

Configurer l'ids dans le fichier **conf.json** :
- **"FileToCheck"**: liste des fichiers à vérifier
- **"FoldersToCheck"**: liste des dossiers à vérifier
- **"CheckPorts"**: true ou false, pour vérifier les ports aussi

Lancer le fichier ids.py avec un des arguments disponibles :
- **--check / -c** : lance une vérification des fichiers/dossiers/ports enregistrés
- **--build / -b**: enregistre les données des fichiers/dossiers/ports donnés dans la conf
- **--help / -h** : affiche un menu d'aide

Exemple :

```powershell
[toto@localhost srv]$ python ids.py --build
```

## Service (pour check toutes les 15 minutes)

- Mettre le fichier ids.service et ids.timer dans */etc/systemd/system*

- Lancer le service avec "systemctl start ids"

