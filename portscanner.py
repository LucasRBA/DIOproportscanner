import socket


ip = input("Digite o Host ou IP que será verificado pelo portscanner: ")

ports = []
count = 0

while count < 10:
    ports.append(int(input(" Digite a porta alvo do escaneamento: ")))
    count +=1

for port in ports:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.1)
    code = client.connect_ex((ip, port))


    if code == 0:
        print(str(port), " ==> Porta Aberta no site X")
    else: 
        print(str(port), " ==> Porta Fechada no site X")

print("Scan terminado com sucesso!")