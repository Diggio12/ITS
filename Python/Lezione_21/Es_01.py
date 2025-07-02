class Documento:
    def __init__(self, testo: str):
        self.set_text(testo)

    def set_text(self, testo):
        self.text = testo

    def getText(self) -> str:
        return self.text
    
    def isintext(self, parola) -> bool:
        testo = self.text.split(' ')
        for i in testo:
            if parola.lower() == i.lower():
                return True
        return False
            

class Email(Documento):
    def __init__(self, testo, mittente: str, destinatario: str, titolo: str):
        super().__init__(testo)
        self.set_mittente(mittente)
        self.set_destinatario(destinatario)
        self.set_titolo(titolo)

    def set_mittente(self, mittente):
        self.mittente = mittente

    def set_destinatario(self, destinatario):
        self.destinatario = destinatario

    def set_titolo(self, titolo):
        self.titolo = titolo

    def get_mittente(self) -> str:
        return self.mittente
    
    def get_destinatario(self) -> str:
        return self.destinatario
    
    def get_titolo(self) -> str:
        return self.titolo
    
    def getText(self):
        return f'Da: {self.mittente}, A: {self.destinatario}\nTitolo: {self.titolo}\nMessaggio: {super().getText()}'
    
    def write_to_file(self, nome: str):
        testo_in_file = self.getText()
        with open(nome, 'w') as file:
            file.write(testo_in_file)



class File(Documento):
    def __init__(self, nomePercorso: str):
        self.nomePercorso = nomePercorso
        super().__init__(self.leggiTestoDaFile())

    def leggiTestoDaFile(self):
        with open(self.nomePercorso, 'r') as reader:
            testo = reader.read()

        return testo

    def getText(self):
        return f'Percorso: {self.nomePercorso}\nContenuto: {super().getText()}'
    

