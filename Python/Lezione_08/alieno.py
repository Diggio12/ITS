class Alieno:
    def __init__(self, galaxy: str):
        self.setGalaxy(galaxy)

    def setGalaxy(self, galaxy: str) -> None:
        if galaxy:
            self.galaxy = galaxy
        else:
            print('Errore! la galassia di provenienza non può essere una stringa vuota!')
    
    def getGalaxy(self) -> str:
        return self.galaxy
    
    def speak(self) -> None:
        print('\nHDBEIDJSbjbshws\n')

    def __str__(self):
        return f'Alieno proveniente dalla galassia {self.getGalaxy()}'