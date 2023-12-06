import socket
import datetime
import threading

def recibir_respuesta(client_socket):
    while True:
        respuesta = client_socket.recv(1024).decode('utf-8')
        print(f"\nRespuesta del servidor: {respuesta}\n")


def cliente(ip_servidor):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((ip_servidor, 12345))  # Reemplazar 'ip_del_servidor' con la dirección IP del servidor

    hiloRespuesta = threading.Thread(target=recibir_respuesta, args=(client_socket,))
    hiloRespuesta.start()

    while True:
        # Enviar mensaje al servidor
        date = datetime.datetime.now().time()
        tiempo = f"{date.hour}:{date.min}:{date.second}"
        mensaje = input("Ingrese su mensaje (exit para salir):")

        if (mensaje != "exit"):
            mensaje += " " + tiempo
            client_socket.send(mensaje.encode('utf-8'))

            with open('mensajes.txt', 'a') as file:
                file.write(f"{address}: {mensaje}\n")

            # Recibir respuesta del servidor
            respuesta = client_socket.recv(1024).decode('utf-8')
            print(f"Respuesta del servidor: {respuesta}")
        else:
            client_socket.close()
            break;

    #client_socket.close()

def servidor():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 12345))  # Bind a todas las interfaces en el puerto 12345
    server_socket.listen(5)

    print("Servidor esperando conexiones...")

    while True:
        client_socket, address = server_socket.accept()
        print(f"Cliente conectado desde: {address}")

        # Recibir mensaje del cliente
        mensaje = client_socket.recv(1024).decode('utf-8')
        print(f"Mensaje recibido: {mensaje}")

        # Almacenar el mensaje en un archivo
        with open('mensajes.txt', 'a') as file:
            file.write(f"{address}: {mensaje}\n")

        # Enviar respuesta al cliente
        respuesta = "Mensaje recibido correctamente"
        client_socket.send(respuesta.encode('utf-8'))

        # client_socket.close()


def main():
    servidor()

    maquina1 = '192.168.159.128'
    maquina2 = '192.168.159.133'
    maquina3 = '192.168.159.134'
    maquina4 = '192.168.159.135'
    maquina5 = '192.168.159.136'

    while True:
        maquina = input("Ingrese el numero de maquina al que quiere mandar un mensaje:")

        if(maquina == 1):
            cliente(maquina1)
        elif(maquina == 2):
            cliente(maquina2)
        elif (maquina == 3):
            cliente(maquina3)
        elif (maquina == 4):
            cliente(maquina4)
        elif (maquina == 5):
            cliente(maquina5)