import base64
import zlib
from ircConnect import IrcConnect

class DecodingUtil: 

    base64Text = ""

    def __init__(self, baseText):
        self.base64Text = baseText
        
    def decodeBase64(self):
        decodedText = zlib.decompress(base64.b64decode(self.base64Text))
        print("decodedText ", decodedText) 
        
        return decodedText

