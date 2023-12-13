import socket
import threading
import datetime

PUERTO = 12345
IP = socket.gethostbyname(socket.gethostname())
DIR = (IP, PUERTO)
MAQUINA1 = "192.168.159.128"
MAQUINA2 = "192.168.159.133"
MAQUINA3 = "192.168.159.134"
MAQUINA4 = "192.168.159.135"
MAQUINA5 = "192.168.159.136"
SERVIDOR = '0'
ADDR = (SERVIDOR, PUERTO)

# Socket para ser servidor
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(DIR)

# Socket para ser cliente
cliente = socket.socket(socket.AD_INET, socket.SOCK_STREAM)

def manejar_cliente(con, dir):
    print(f"[Nueva conexion] {dir} conectada.")

    conectado = True

    while conectado:
        data =  con.recv(1024).decode('utf-8')

        if data == 'exit':
            conectado = False

        print(f"[{dir} dice:] {data}")

    con.close()


def iniciar_servidor():
    servidor.listen()
    while True:
        con, dir = servidor.accept()
        thread = threading.Thread(target=manejar_cliente, args=(con, dir))
        thread.start()
        print(f"[Conexiones activas] {threading.active_count()-1}")



def envio():
    mensaje = input("\nMensaje a enviar: ")
    cliente.send(mensaje.encode('utf-8'))


def iniciar_cliente():

    while True:
        maquina = input("Ingrese en número de maquina al que quiere conectarse ('quit' para salir): ")

        if maquina == '1':
            SERVIDOR = MAQUINA1
        elif maquina == '2':
            SERVIDOR = MAQUINA2
        elif maquina == '3':
            SERVIDOR = MAQUINA3
        elif maquina == '4':
            SERVIDOR = MAQUINA4
        elif maquina == '5':
            SERVIDOR = MAQUINA5
        elif maquina.lower() == 'quit':
            SERVIDOR = '0'
            return  # Terminar el hilo y cerrar el programa

        cliente.connect(ADDR)

        thread = threading.Thread(target=envio, args=())
        thread.start()


iniciar_servidor()
iniciar_cliente()