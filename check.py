import build
import ports
import json
from log import logger
def check():
    infos = build.getInfoAllFile()
    listening_port = ports.get_udp_and_tcp()
    change = False
    with open('db.json', 'r') as file:
        data = json.load(file)
    if not infos == data["FileToCheck"]:
        logger.warning("Changement détecté dans les fichiers surveillés.")
        change = True
    if not listening_port == data["port_list"]:
        logger.warning("Modification des ports détectée.")
        change = True
    if not change :
        logger.info("Aucune modification détectée dans les fichiers ou les ports.")

    

if __name__ == "__main__":
    check()