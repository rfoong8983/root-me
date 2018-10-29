import socket
import time
import base64

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
	text = IRC.recv(10000).decode("utf-8")
	reply = text.split('PRIVMSG pepperoni_tony :')[1]
	#numbers = reply.split(':')[1].split(' / ')
	#print(numbers[0], numbers[1])
	#return(numbers[0], numbers[1])
	#print(text, '\n')
	#print(text.split('PRIVMSG pepperoni_tony :')[0], '\n')
	print("Encoded string: " + reply)
	#print("length of encoded message: " + str(len(reply)), '\n')
	return reply

irc_conn()
login(nick)
time.sleep(3)
join(channel)
time.sleep(3)
#message()
#time.sleep(1)
message("PRIVMSG Candy :!ep2")
time.sleep(0.5)
#receive()

#reply from Candy is string type and encoded using base64 encoding
encoded_str_from_candys_reply = receive()

#decoding using base64 returns a bytes type (8-bits per char)
#strings in python3 are unicode by default
#(?) b64decode probably encodes string to utf-8 and decodes as such (?)
decoded_b64_bytestype = base64.b64decode(encoded_str_from_candys_reply)

print("Base64 encoded string-type (unicode) from Candy decoded and")
print("...decoded string returned as bytes type (encoded utf-8) - ", '\n')
to_send = decoded_b64_bytestype.decode('utf-8')

print("Base64.b64decode returns: b'" + to_send + "'")
print("...bytes type decoded using utf-8 encoding back to unicode string")
print("%s sent back to Candy for password" % to_send, '\n')

message("PRIVMSG Candy :!ep2 -rep %s" % to_send)
receive()