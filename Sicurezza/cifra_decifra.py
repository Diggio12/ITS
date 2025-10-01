from Crypto.Cipher import AES
import base64
from Crypto.Util.number import inverse


'''# Function to pad the message to be multiple of 16 bytes
# questa funzione prende il testo e lo rende multiplo di 16
# perchè AES decifra 16 byte alla volta
def pad(text):
    while len(text) % 16 != 0:
        text += " "
    return text


# Encryption

# questa funzione prende un testo da cifrare e la chiave con cui cifrarlo
def encrypt(plain_text, key): 

    # AES.new() prende la chiave e il tipo di cifratura per creare il cifrato, 
    # pad(key) serve per far arrivare la chiave a 16 byte
    # .encode("utf-8") trasforma la stringa in byte (b' ')
    # cipher è l'oggetto che utilizzeremo per cifrare e decifrare
    cipher = AES.new(pad(key).encode("utf-8"), AES.MODE_ECB) 

    # crea un testo cifrato:
    # pad(plain_text) rende il messaggio da cifrare divisibile per 16,
    # .encode("utf-8") trasforma la stringa in byte (b' ')
    # cipher è la macchina di cifratura 
    # prendi il cifratore/decifratore e fagli cifrare questo ()
    encrypted_text = cipher.encrypt(pad(plain_text).encode("utf-8"))

    # per ogni lettera nel testo cifrato, printala una accanto all'altra 
    # printerà una sequenza di bytes cifrati ottenuti con il rigo 23
    for x in encrypted_text:
        print(x, end=" ")
    print()
    # a questo punto il testo cifrato è una sequenza incomprensibile di byte
    # con b64encode il testo rimane in byte ma è più leggibile, è in lettere, numeri e pochi simboli
    # non è più il testo cifrato ma è un arappresentazione testuale del cifrato
    # .decode("utf-8") trasforma il testo da bytes a stringa Python (rimuove b' ')
    return base64.b64encode(encrypted_text).decode("utf-8")
    


# Decryption

# semplicemente prende il testo cifrato e la chiave e decifra 
# si scrive allo stesso modo, cambia cipher.encrypt e .b64decode
# strip() rimuove spazi bianchi perchè il padding aggiunge spazi 
# pur di rendere il testo % 16
# cipher.decrypt necessario all'inizio perchè stiamo dicendo
# prendi il cifratore/decifratore e fagli decifrare questo ()
# ovviamente come argomento non c'è il testo da cifrare come prima,
# ma c'è il testo da decifrare
'''
def decrypt(encrypted_text, key):
    cipher = AES.new(pad(key).encode("utf-8"), AES.MODE_ECB)
    decrypted_text = (
        cipher.decrypt(base64.b64decode(encrypted_text)).decode("utf-8").strip()
    )
    return decrypted_text
'''


# Example usage
key = "ThisIsASecretKey"  # 16 caratteri
plain_text = "0"
encrypted_text = encrypt(plain_text, key)
decrypted_text = decrypt(encrypted_text, key)

print("Originale: ", plain_text)
print("Cifrato  : ", encrypted_text)
print("Decifrato: ", decrypted_text)

exit(0)

#print("Plain Text:", plain_text)
#print("Encrypted Text:", encrypted_text)
#print("Decrypted Text:", decrypted_text)


# prova di decifra brute force
# enc è un testo già cifrato scritto in base64
enc = "OgJuOYJZT0FDb47DBOkNgA=="

# key è la chiave segreta
# la chiave è la stessa di prima,
# le x verranno sostituite dai tentativi diversi (p1,..)
# fin quando dopo aver passato ogni lettera,
# ogni ciclo for presentera tutte X
key = "XXXXIsASecretKey"

for p1 in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
    for p2 in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
        for p3 in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
            for p4 in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
                key = p1 + p2 + p3 + p4 + "IsASecretKey"
                # il try decifrerà il testo con ogni chiave possibile
                # che il programma gli darà
                # anche se trova la chiave corretta il programma continuerà a stampare
                # fin quando non termineranno le combinazioni possibili
                try:
                    dec = decrypt(enc, key)
                    print("La chiave è: ", key, " e la stringa è: ", dec)
                # l'except silenzia ogni errore che presenta il programma
                # e lo fa continuare fin quando non finisce tutte le combinazioni
                except:
                    # continua
                    continue'''



n = 51151902024533551

e = 3

C = 10002041662569686

def fattori_primi(n):
    for i in range(2, int(n**0.5) + 1):                         # provo i possibili divisori solo da 2 fino alla radice quadrata di n (questo perchè se n = p * q, allora p/q <=> square di n)
        if n % i == 0:                
            p = i
            q = n // i                                          # una volta trovato 1 fattore primo l'altro lo ricavo facendo n diviso (fattore primo trovato)
            return p, q
    return None                                                 # se non trova niente, n non è prodotto di due primi


p, q = fattori_primi(n)
print(f'p ={p}, q ={q}')

phi = (p-1) * (q-1)

d = inverse(e, phi)
print(f'd ={d}')

c_decriptato = pow(C, d, n)
c_decriptato_str = c_decriptato.to_bytes((c_decriptato.bit_length() + 7) //8, 'big').decode()
print(f'Il messaggio decriptato è: {c_decriptato_str}')



