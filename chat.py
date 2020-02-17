from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter


def receive():
    """Gelen mesajlarla ilgili foksiyon."""
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            msg_list.insert(tkinter.END, msg)
        except OSError:  # Kullanıcının sohbeti terk etme durumu.
            break


def send(event=None):  # Event binder ile gönderme işlemi.
    """Mesaj gönderme kısımı."""
    msg = my_msg.get()
    my_msg.set("")  # Mesaj gönderdikten sonra inputu temizleme.
    client_socket.send(bytes(msg, "utf8"))
    if msg == "{quit}":#çıkış komutu sohbetten ayrılma bağlantı kesme
        client_socket.close()
        top.quit()


def on_closing(event=None):
    """Sohbet ekranı kapanırken çalışır."""
    my_msg.set("{quit}")
    send()

top = tkinter.Tk()
top.geometry("340x500")
top.title("CS 364 APP")

messages_frame = tkinter.Frame(top)
my_msg = tkinter.StringVar()  # Gönderilecek mesaj kısımı
my_msg.set("Adınız:")
scrollbar = tkinter.Scrollbar(messages_frame)  # Mesaj kutusu içinde gezzinme için scrollbar.
# Mesaj kutusu ayarları.
msg_list = tkinter.Listbox(messages_frame, height=28, width=51, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
messages_frame.pack()

entry_field = tkinter.Entry(top, textvariable=my_msg, width=50)
entry_field.bind("<Return>", send) #Mesaj butonu
entry_field.pack()
send_button = tkinter.Button(top, text="Gönder", command=send)
send_button.pack()

top.protocol("WM_DELETE_WINDOW", on_closing)

#----Now comes the sockets part----
HOST = input('HOST: ')
PORT = input('PORT: ')
if not PORT:#Port belirtilmezse sabit port
    PORT = 1234
else:
    PORT = int(PORT)

BUFSIZ = 1024
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=receive)
receive_thread.start()
tkinter.mainloop()