import build
import ports
import json

def check():
    infos = build.getInfoAllFile()
    listening_port = ports.get_udp_and_tcp()
    with open('db.json', 'r') as file:
        data = json.load(file)
    if not infos == data["FileToCheck"]:
        print(infos)
        print(data["FileToCheck"])
        print("probleme lors du check la")
    if not listening_port == data["port_list"]:
        print("changement de port la")
        print(listening_port)
        print(data["port_list"])
    

if __name__ == "__main__":
    check()