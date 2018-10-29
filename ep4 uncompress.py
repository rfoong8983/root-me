import socket
import time
import base64
import zlib
import codecs

host = "irc.root-me.org"
port = 6667
channel = "#root-me_challenge"
test = "irc.root-me.org"

nick = "pepperoni_tony"
ident = "pepperoni_tony"
realname = "testing"
readbuffer = ""

# open a socket to handle the connection
IRC = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# open a connection with the server
def irc_conn():
	IRC.connect((host, port))

# simple funciton to send data through the socket
def send_data(command):
	IRC.send(command + '\n'.encode('ascii'))

# join the channel
def join(channel):
	send_data(("JOIN %s" % channel).encode("utf-8"))

#send login data (customizable)
def login(nick, username='user', password = None, \
	realname = 'testing', hostname = 'Helena', \
	servername = 'Server'):
	my_info = "USER %s %s %s %s" % (username, hostname, servername, realname)
	set_nick = "NICK %s" % (nick)
	send_data(my_info.encode("utf-8"))
	send_data(set_nick.encode("utf-8"))

def priv_message():
	send_data("PRIVMSG Candy :!ep1".encode("utf-8"))

def message(msg):
	send_data(msg.encode("utf-8"))

def receive():
	text = IRC.recv(10000).decode("ansi")
	reply = text.split('PRIVMSG pepperoni_tony :')[1]
	#numbers = reply.split(':')[1].split(' / ')
	#print(numbers[0], numbers[1])
	#return(numbers[0], numbers[1])
	#print(text, '\n')
	#print(text.split('PRIVMSG pepperoni_tony :')[0], '\n')
	print("Base64 encoded string (unicode): " + reply)
	#print("length of encoded message: " + str(len(reply)), '\n')
	return reply

irc_conn()
login(nick)
time.sleep(3)
join(channel)
time.sleep(3)
#message()
#time.sleep(1)
message("PRIVMSG Candy :!ep4")
time.sleep(0.5)
#receive()

#reply from Candy is string type and encoded using base64 encoding
b64encoded_compressed_unicode = receive()
decoded_then_decompressed_uni = zlib.decompress(base64.b64decode(b64encoded_compressed_unicode))
decoded_then_decompressed_utf = decoded_then_decompressed_uni.decode('utf-8')
message("PRIVMSG Candy :!ep4 -rep %s" % decoded_then_decompressed_utf)
receive()