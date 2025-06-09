from string import ascii_lowercase

key = int(input('Inserire valore key: '))
frase = input('Inserire frase da voler cifrare: ')

def caesar_cypher_encrypt(key: int, frase: str):

    parola_cifrata: list[str] = []
    contatore_lowercase: int = 0

    alfabeto_numerato_lowercase: dict[str, int] = {}

    for lettera in ascii_lowercase:
        alfabeto_numerato_lowercase[lettera] = contatore_lowercase
        contatore_lowercase += 1

    for i in frase.lower():
        if i in alfabeto_numerato_lowercase:
            posizione_carattere: int = alfabeto_numerato_lowercase[i]
            nuova_posizione_carattere: int = (posizione_carattere + key) % 26
            for parola, posizione in alfabeto_numerato_lowercase.items():
                if nuova_posizione_carattere == posizione:
                    nuovo_carattere: str = parola
                    parola_cifrata.append(nuovo_carattere)
    return parola_cifrata

def caesar_cypher_decrypt(key: int, parola_cifrata: list[str]):

    parola_decifrata: list[str] = []
    contatore_lowercase: int = 0

    alfabeto_numerato_lowercase: dict[str, int] = {}

    for lettera in ascii_lowercase:
        alfabeto_numerato_lowercase[lettera] = contatore_lowercase
        contatore_lowercase += 1

    for i in parola_cifrata:
        if i in alfabeto_numerato_lowercase:
            posizione_carattere: int = alfabeto_numerato_lowercase[i]
            nuova_posizione_carattere: int = (posizione_carattere - key) % 26
            for parola, posizione in alfabeto_numerato_lowercase.items():
                if nuova_posizione_carattere == posizione:
                    nuovo_carattere: str = parola
                    parola_decifrata.append(nuovo_carattere)
    return parola_decifrata


Encrypting = caesar_cypher_encrypt(key, frase)
Decrypting = caesar_cypher_decrypt(key, Encrypting)


