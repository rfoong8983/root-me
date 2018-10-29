import sys
import socket
import string
import time

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
	reply = text.split('PRIVMSG')[1]
	#numbers = reply.split(':')[1].split(' / ')
	#print(numbers[0], numbers[1])
	#return(numbers[0], numbers[1])
	print(reply)
	return reply

irc_conn()
login(nick)
time.sleep(3)
join(channel)
time.sleep(3)
#message()
#time.sleep(1)
message("PRIVMSG Candy :!ep1")
time.sleep(0.5)

numbers = receive().split(':')[1].split(' / ')
n1,n2 = numbers
answer = round(float(n1)**0.5 * float(n2), 2)
print(answer)

message("PRIVMSG Candy :!ep1 -rep %s" % answer)
time.sleep(0.5)
receive()
