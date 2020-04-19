from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter
import tkinter as tk
from winsound import *

def receive():
    """Gelen mesajlarla ilgili foksiyon."""
    counter=0
    while True:
        try:
            counter+=1
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            msg_list.insert(tkinter.END, msg)
            if counter > 3:
                song_id = msg.split(":")[1]
                if song_id ==" {ses1}":
                    PlaySound("A-Computer Error", SND_FILENAME)
                if song_id ==" {ses2}":
                    PlaySound("a-ice-cubes-glass-daniel_simon", SND_FILENAME)
                if song_id ==" {ses3}":
                    PlaySound("Air Plane Ding-Sound", SND_FILENAME)
                if song_id ==" {ses4}":
                    PlaySound("a-service-bell_daniel_simion", SND_FILENAME)
                if song_id ==" {ses5}":
                    PlaySound("A-Tone-His_Self", SND_FILENAME)
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

def play(id):
    if id == 1:
        tag = "{ses1}"
        client_socket.send(bytes(tag,"utf8"))
        return PlaySound("A-Computer Error", SND_FILENAME)
    if id == 2:
        tag = "{ses2}"
        client_socket.send(bytes(tag, "utf8"))
        return PlaySound("a-ice-cubes-glass-daniel_simon", SND_FILENAME)
    if id == 3:
        tag = "{ses3}"
        client_socket.send(bytes(tag, "utf8"))
        return PlaySound("Air Plane Ding-Sound", SND_FILENAME)
    if id == 4:
        tag = "{ses4}"
        client_socket.send(bytes(tag, "utf8"))
        return PlaySound("a-service-bell_daniel_simion", SND_FILENAME)
    if id == 5:
        tag = "{ses5}"
        client_socket.send(bytes(tag, "utf8"))
        return PlaySound("A-Tone-His_Self", SND_FILENAME)

def on_closing(event=None):
    """Sohbet ekranı kapanırken çalışır."""
    my_msg.set("{quit}")
    send()

def create_window():
    """Ses butonunu ekrana eklemek için gerekli kısım"""
    window = tk.Toplevel(top)
    window.title('Sound')
    window.geometry('300x50')
    sound1 = tk.Button(window,text="1", command=lambda: play(1)).pack(side=tk.LEFT)
    sound2 = tk.Button(window, text="2", command=lambda: play(2)).pack(side=tk.LEFT)
    sound3 = tk.Button(window, text="3", command=lambda: play(3)).pack(side=tk.LEFT)
    sound4 = tk.Button(window, text="4", command=lambda: play(4)).pack(side=tk.LEFT)
    sound5 = tk.Button(window, text="5", command=lambda: play(5)).pack(side=tk.LEFT)

top = tkinter.Tk()
top.geometry("340x500")
top.title("CS 364 APP")

messages_frame = tkinter.Frame(top)

scrollbar = tkinter.Scrollbar(messages_frame)  # Mesaj kutusu içinde gezinme için scrollbar.
# Mesaj kutusu ayarları.
msg_list = tkinter.Listbox(messages_frame, height=28, width=51, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
messages_frame.pack()

my_msg = tkinter.StringVar()# Gönderilecek mesaj kısımı
my_msg.set("Adınız:")

entry_field = tkinter.Entry(top, textvariable=my_msg, width=50)  #Mesaj butonu
entry_field.bind("<Return>", send)
entry_field.pack()
send_button = tkinter.Button(top, text="Gönder", command=send)
send_button.pack(side=tk.LEFT)


#sound
sound_button=tk.Button(top,text='Sound',command=create_window)
sound_button.pack(in_=top, side=tk.LEFT)


top.protocol("WM_DELETE_WINDOW", on_closing)

#----Now comes the sockets part----
HOST = input('HOST: ')
PORT = input('PORT: ')
if not PORT:  #Port belirtilmezse sabit port
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
