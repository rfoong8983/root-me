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

upperalphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

upperdict = {}
lowerdict = {}

#create mapping for ROT-13
for idx, val in enumerate(upperalphabet):
	#if index is (n-14th char) after thirteenth character (m-13th char)
	if idx > 12:
		#set key to letter associated with : (index - 13 characters)
		upperdict[val] = upperalphabet[idx - 13]
		lowerdict[val.lower()] = upperalphabet[idx - 13].lower()
	else:
		upperdict[val] = upperalphabet[idx + 13]
		lowerdict[val.lower()] = upperalphabet[idx + 13].lower()

#print(upperdict)
#print(lowerdict)

output = ""
message("PRIVMSG Candy :!ep3")
time.sleep(0.5)

#2 seconds to decode
rot13_encoded = receive()
for val in rot13_encoded:
	if val in upperdict.keys():
		output += upperdict[val]
	elif val in lowerdict.keys():
		output += lowerdict[val]
	else:
		output += val

message("PRIVMSG Candy :!ep3 -rep %s" % output)
time.sleep(0.5)
receive()
