class Pagamento:
    def __init__(self):

        self.__importo = 0.0

    def setImport (self, importo: float):
        self.__importo = importo

    def getImport(self) -> float:
        return self.__importo
    
    def dettagliPagamento(self) -> str:
        print(f'Importo del pagamento: euro {round(self.__importo, 2)}')

class PagamentoContanti(Pagamento):
    def __init__(self, importo: float):
        super().__init__()

        self.importo = importo
        
    def dettagliPagamento(self) -> str:
        print(f'Pagamento in contanti di: {round(self.importo, 2)}')

    def inPezziDa(self):
        
        soldi: list = [500, 200, 100, 50, 20, 10, 5, 2, 1, 0.50, 0.10, 0.05, 0.01]
        importo_totale = self.importo
        soldi_usati: dict = {}

        for tagli in soldi:
            if tagli <= importo_totale:
                while (importo_totale - tagli) >= 0:
                    importo_totale -= tagli
                    if tagli in soldi_usati:
                        soldi_usati[tagli] += 1
                    else:
                        soldi_usati[tagli] = 1
                
        for soldati, ripetizione in soldi_usati.items():
            if soldati <=  2:   
                print(f'{self.importo:.2f} euro da pagare in contanti con:\n{ripetizione} monete da {soldati} euro')
            else:
                print(f'{self.importo:.2f} euro da pagare in contanti con:\n{ripetizione} banconota da {soldati} euro')


    
class PagamentoCartaDiCredito(Pagamento):
    def __init__(self, importo: float, nome: str, cognome: str, numero_carta: str, data: str):
        super().__init__()

        self.importo = importo
        self.nome = nome
        self.cognome = cognome
        self.numero_carta = numero_carta
        self.data = data


    def dettagliPagamento(self):
        print(f'Pagamento di: {self.importo} effettuato con la carta di credito.\nNome sulla carta: {self.nome} {self.cognome}\nData di scadenza: {self.data}\nNumero della carta: {self.numero_carta}')

                        

if __name__ == "__main__":
    p1 = PagamentoContanti(150.00)
    p2 = PagamentoContanti(95.25)

    p1.inPezziDa()
    p2.inPezziDa()

    p3 = PagamentoCartaDiCredito(200.00, "Mario", "Rossi", "1234567890123456", "12/23")
    p4 = PagamentoCartaDiCredito(500.00, "Luca", "Bianconi", "6543210987654321", "07/29")


    for pagamento in [p1, p2, p3, p4]:
        pagamento.dettagliPagamento()