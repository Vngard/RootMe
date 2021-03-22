import sys, socket, ssl, time

class IrcConnect:

    ORG_URL = "irc.root-me.org"
    PORT = "6697"

    network = ''
    identifiant = ''
    nickname = ''
    name = ''
    chan = ''
    pswd = ''

    data = ''
    start = 'Start to connect.'
    connected = 'Connection estblished.'

    def __init__(self, identifiant, nickname, name, chan, pswd):
        
        self.identifiant = identifiant
        self.nickname = nickname
        self.name = name
        self.chan = chan
        self.pswd = pswd

    def connectToIrc(self):

        print(self.start)

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.ORG_URL, self.PORT))
        ircsocket = ssl.wrap_socket(s)
        ircsocket.send("USER %s %s %s :%s\r\n" %(self.nickname, self.identifiant, self.name, self.nickname))
        ircsocket.send("NICKNAME %s\r\n " % self.nickname)

        print(self.connected)

        return ircsocket
    