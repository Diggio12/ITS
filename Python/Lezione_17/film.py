class Film:
    def __init__(self, Id_Code: int, title: str):
        self.setIdCode(Id_Code)
        self.setTitle(title)

    def setIdCode(self, Id_Code) -> None:
        self.__IdCode = Id_Code

    def setTitle(self, title) -> None:
        self.__title = title

    def getIdCode(self) -> int:
        return self.__IdCode
    
    def getTitle(self) -> str:
        return self.__title
    
    def isEqual(self, new_Id: str):
        if new_Id == self.getIdCode():
            return True
        
        