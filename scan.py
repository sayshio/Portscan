import socket

with open("lista_de_dns.txt","r" ,encoding= "UTF-8") as lista_dns:

    for dns in lista_dns: 
            dns = dns.strip()
            lista_de_portas = open('lista_de_portas.txt')
            for porta in lista_de_portas:
             
                    porta = int(porta)
                    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    cliente.settimeout(0.3)
                    # o valor em cliente.settimeout é para acrescentar ou diminuir o tempo de conexão, quanto menor o tempo...mais rapido, no entanto, menor a precisão.
                    try:
                        code = cliente.connect_ex((dns, porta))                    
                        if code == 0:
                            print(f' {dns} / porta: {porta} "ABERTA"')
                            #print(f' {dns}')                       
                    except:
                        continue

 
    