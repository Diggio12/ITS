from string import ascii_lowercase

def ceasar_cypher_encrypt(s: str, key: int) -> str:
    alfabeto_maiuscolo: list[str] = []
    for i in ascii_lowercase:
        alfabeto_maiuscolo = i.upper()
