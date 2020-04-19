#https://github.com/samuhay/Python-Chat-App/tree/master
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread


def accept_incoming_connections():
    """Gelen bağlantıları halleder."""
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s bağlandı." % client_address)
        client.send(bytes("Server bağlantısı başarılı", "utf8"))  # Kullanıcı adı için mesaj
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()


def handle_client(client):  # Bağlantı soketini bekliyor.
    """Tekil bağlantı kısımı."""

    name = client.recv(BUFSIZ).decode("utf8")
    x=name.split(":")
    real_name=x[1]
    welcome = 'Hoşgeldin %s! Eğer çıkmak isterseniz, {quit} yazınız!' % real_name
    client.send(bytes(welcome, "utf8"))
    msg = "%s sohbete katıldı!" % real_name
    broadcast(bytes(msg, "utf8"))
    clients[client] = real_name

    while True:
        msg = client.recv(BUFSIZ)
        if msg != bytes("{quit}", "utf8"):
            broadcast(msg, real_name + ": ")
        else:
            client.send(bytes("{quit}", "utf8"))
            client.close()
            del clients[client]
            broadcast(bytes("%s sohbetten ayrıldı." % real_name, "utf8"))
            break


def broadcast(msg, prefix=""):  # prefix kullanıcı adını için.
    """tüm bağlantılar için genel mesaj yayınlar."""

    for sock in clients:
        sock.send(bytes(prefix, "utf8") + msg)


clients = {}
addresses = {}

HOST = '192.168.1.79'  # Server ip adresi
PORT = 1234  # Server Portu
BUFSIZ = 1024  # Buffer belleği
ADDR = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)


if __name__ == "__main__":
    SERVER.listen(5)
    print("Bağlantı bekleniyor...")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()
