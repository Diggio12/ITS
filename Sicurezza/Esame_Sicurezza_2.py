from Crypto.Cipher import AES
from Crypto.Util.number import inverse


# ESERCIZIO 1


#Messaggio cifrato convertito in numero intero in base 10
messaggio_cifrato = 204751668535

e = 3        #esponente pubblico

n = 514948966453           #modulo

# insieme di caratteri permessi (A-Z + a-z)
Alfabeto_maiuscolo_minuscolo = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

# provo tutte le parole di lunghezza 5
# provo ogni combinazione, la prima che riproduce il cifrato è la soluzione
messaggio_trovato: bool = False

for prova_1 in Alfabeto_maiuscolo_minuscolo:
    if messaggio_trovato == True:
        break                           #esco se trovo la corrispondenza"
    for prova_2 in Alfabeto_maiuscolo_minuscolo:
        if messaggio_trovato == True: 
            break
        for prova_3 in Alfabeto_maiuscolo_minuscolo:
            if messaggio_trovato == True: 
                break
            for prova_4 in Alfabeto_maiuscolo_minuscolo:
                if messaggio_trovato == True:
                    break
                for prova_5 in Alfabeto_maiuscolo_minuscolo:
                    if messaggio_trovato == True: 
                        break
                    plain = prova_1 + prova_2 + prova_3 + prova_4 + prova_5         
                    try:
                        plain_text = int(plain.encode('utf-8').hex(), 16)     #converto la stringa (Unicode) primna in esadecimale e poi in un intero
                        messaggio_cifrato_2 = pow(plain_text, 3, n)
                        if messaggio_cifrato_2 == messaggio_cifrato:
                            print("Trovato Messaggio Originale:", plain)
                            messaggio_trovato = True
                    except:
                        continue


# ESERCIZIO 2

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


