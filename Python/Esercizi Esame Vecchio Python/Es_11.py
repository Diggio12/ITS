from string import ascii_lowercase

def occorrenze(sentence: str) -> dict[str, int]:
    occorrenze_dict = {}
    parole_in_frase = sentence.lower().split()

    for parola in parole_in_frase:
        parola_pulita = ""
        for i in parola:
            if i in ascii_lowercase:
                parola_pulita += i

        if parola_pulita:
            if parola_pulita not in occorrenze_dict:
                occorrenze_dict[parola_pulita] = 1
            else:
                occorrenze_dict[parola_pulita] += 1

    return occorrenze_dict


occorrenze('Ciao Python, come va Python?')

    

