from Crypto.Cipher import AES
import base64

def pad(testo):
    while len(testo) % 16 != 0:
        testo += ' '
    return testo


def encrypt (testo_originale, key):
    cypher = AES.new(pad(key).encode("utf-8"), AES.MODE_ECB)
    encrypted_text = cypher.encrypt(pad(testo_originale).encode("utf-8"))
    return base64.b64encode(encrypted_text).decode("utf-8")
    


def decrypt (encrypted_text, key):
    cypher = AES.new(pad(key).encode("utf-8"), AES.MODE_ECB)
    decrypted_text = cypher.decrypt(base64.b64decode(encrypted_text)).decode("utf-8").strip()
    
    return decrypted_text



key = 'Manna'

testo_originale = 'Emiliano Spaicciaz'

testo_crittato = encrypt(testo_originale, key)
testo_decriptato= decrypt(testo_crittato, key)

print(testo_crittato, testo_decriptato)