import datetime
import os
from base64 import encode
import hashlib
from pathlib import Path
import json



def build():
    infos = getInfoAllFile()
    GenerateBuildFile(infos)


def getInfoAllFile():
    with open('conf.json', 'r') as file:
        data = json.load(file)
    files = data["FileToCheck"]
    all_infos = []
    for file in files:
        info = getInfoFile(file)
        all_infos.append(info)
    return all_infos
        
def GenerateBuildFile(info_file):
    build_time = datetime.datetime.now().isoformat()
    content = {
        "build_time":build_time,
        "FileToCheck":info_file,
        "port_list":[]
    }
    with open("db.json", "w") as outfile:
        json.dump(content, outfile)
def getInfoFile(path):
    file = Path(path)

    SHA512 = hash_file(path,"sha512")
    SHA256 = hash_file(path,"sha256")
    MD5 = hash_file(path,"md5")
    date_last_modif = os.path.getmtime(path)
    date_creation = os.stat(file).st_ctime
    owner = file.owner()
    group = file.group()
    size = os.path.getsize(path)
    file_info = {
        "SHA512":SHA512,
        "SHA256":SHA256,
        "MD5":MD5,
        "date_last_modif":date_last_modif,
        "date_creation":date_creation,
        "owner":owner,
        "group":group,
        "size":size
    }
    return file_info

def hash_file(file_path, algorithm='sha256'):
    """Compute the hash of a file using the specified algorithm."""
    hash_func = hashlib.new(algorithm)
    
    with open(file_path, 'rb') as file:
        while chunk := file.read(8192):
            hash_func.update(chunk)
    
    return hash_func.hexdigest()

def get_file_from_directory(path='.'):
    global FileFromDirectory
    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        if os.path.isdir(full_path):
            get_file_from_directory(full_path)
        else:
            FileFromDirectory.append(full_path)

if __name__ == "__main__":
    build()
    