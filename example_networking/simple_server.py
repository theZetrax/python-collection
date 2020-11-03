import socket

s = socket.socket()
host = socket.gethostname()
port = 9999

s.bind((host, port))

print("Waiting connection...")
s.listen(5)

while True:
    conn, addr = s.accept()
    print("Got connection", addr)
    conn.send('Server saying hi')
    conn.close()