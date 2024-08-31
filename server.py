import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 1028))
server.listen(5)

def download(client, file):
    client.send(b"CONFIRM")
    with open(file, 'wb') as fp:
        data = client.recv(1024)
        while data:
            fp.write(data)
            data = client.recv(1024)   
    client.close()


def upload(client, file):
    with open(file, 'rb') as fp:
        data = fp.read(1024)
        while data:
            client.send(data)
            data = fp.read(1024)
    client.close()

while True:
    client, addr = server.accept()
    data = client.recv(1024).decode().strip()
    if data.split()[0] == "UPLOAD":
        download(client, data.split()[1])
    if data.split()[0] == "DOWNLOAD":
        upload(client, data.split()[1])
