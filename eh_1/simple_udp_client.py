import socket
HOST = '127.0.0.1'
PORT = 9997
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Socket object aanmaken
client.sendto(b'AAABBBCCC', (HOST, PORT)) # Data opsturen
data, address = client.recvfrom(4096) # Data ontvangen
print(data.decode('utf-8'))
print(address.decode('utf-8'))
client.close()