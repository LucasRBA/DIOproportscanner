import nmap

scanner = nmap.PortScanner()

print("Bem-vindo ao DIO nmap scanner!")
print( """  ,           ,
           /             \
          ((__---,,,---__))
             (_) O O (_)___________
                \ _ /              |\
                 o_o \ Python-NMAP | \
                      \ DIOScanner |  \
                       \___________|   *
                        |||    WW|||
                        |||      |||
""")

ip = input("Digite o ip a ser escaneado: ")

print("O IP digitado foi: ", ip)
type(ip)

menu = input(""" \n Escolha qual varredura será utilizada
                1) Tipo SYN
                2) Tipo UDP
                3) Tipo Intensa
                Digite a opção escolhida:  """)

print("O tipo de scan escolhido foi: ", menu)

if menu == "1":
    print("Versão utilizada do Nmap: ", scanner.nmap_version())
    scanner.scan(ip, '1-1024', 'sudo -v -sS')
    print(scanner.scaninfo())
    print("Status do IP: ", scanner[ip].state())
    print(scanner[ip].all_protocols())
    print("")
    print("No host escaneado as seguintes portas  estão abertas: \n",scanner[ip]['tcp'].keys())
elif menu == "2":
    print("Versão utilizada do Nmap: ", scanner.nmap_version()) 
    scanner.scan(ip, '1-1024', '-v -sU')
    print(scanner.scaninfo())
    print("Status do IP: ", scanner[ip].state())
    print(scanner[ip].all_protocols())
    print("")
    print("No host escaneado as seguintes portas  estão abertas: \n",scanner[ip]['udp'].keys())
elif menu == "3":
    print("Versão utilizada do Nmap: ", scanner.nmap_version())
    scanner.scan(ip, '1-1024', '-v -sC')
    print(scanner.scaninfo())
    print("Status do IP: ", scanner[ip].state())
    print(scanner[ip].all_protocols())
    print(" ")
    print("No host escaneado as seguintes portas  estão abertas: \n",scanner[ip]['tcp'].keys())
else:
    print("Opção incorreta!\nEscolha uma opção entre 1 e 3")