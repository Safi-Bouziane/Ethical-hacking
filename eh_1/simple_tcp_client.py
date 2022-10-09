import socket
HOST = 'www.google.com'
PORT = 80
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Socket object aanmaken
client.connect((HOST, PORT)) # De client verbinden
client.send(b'GET / HTTP/1.1\r\nHost: google.com\r\n\r\n') # data versturen als bytes
response = client.recv(4096) # data ontvangen
print(response.decode('utf-8'))
client.close()