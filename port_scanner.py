import socket

def scan_port(ip, port):
    try:
        # Cria um socket para testar a conexão
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5) # Tempo de espera rápido
        result = s.connect_ex((ip, port)) # Tenta conectar
        if result == 0:
            print(f"Porta {port}: ABERTA 🛡️")
        s.close()
    except:
        pass

target = input("Digite o IP para escanear: ")
print(f"Escaneando o alvo: {target}")

# Testando as portas mais comuns
for port in [21, 22, 80, 443, 3306]:
    scan_port(target, port)

print("Scan finalizado!")
