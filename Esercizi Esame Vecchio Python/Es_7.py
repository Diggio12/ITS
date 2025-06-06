class ContactManager:
    def __init__(self, contacts: dict[str, list[str]]):
        self.contacts = contacts

    def create_contact(self, name:str, phone_numbers:list[str])-> dict:
        new_dict:dict = {}
        if name in self.contacts:
            print('Errore: Il contatto esiste già')
        elif name not in self.contacts:
            self.contacts[name] = [phone_numbers]
            new_dict[name] = [phone_numbers]
            return new_dict

    def add_phone_number(self, contact_name: str, phone_number: str) -> dict:
        new_dict:dict = {}
        if contact_name in self.contacts:
            if phone_number in self.contacts[contact_name]:
                print('Errore: il numero di telefono esiste già')
            else:
                self.contacts[contact_name].append(phone_number)
                new_dict[contact_name] = [phone_number]
            return new_dict
        elif contact_name not in self.contacts:
            print('Errore: il contatto non esiste!')
        

    def remove_phone_number(self, contact_name: str, phone_number: str) -> dict:
        new_dict:dict = {}
        if contact_name in self.contacts:
            if phone_number in self.contacts[contact_name]:
                self.contacts[contact_name].remove(phone_number)
                new_dict[contact_name] = [self.contacts[contact_name]]
                return new_dict
            elif phone_number not in self.contacts[contact_name]:
                print('Errore: il numero di telefono non è presente!')
        else:
            print('Errore: il contatto non esiste!')

    def update_phone_number(self, contact_name: str, old_phone_number: str, new_phone_number: str) -> dict:
        new_dict: dict = {}
        if contact_name in self.contacts:
            if old_phone_number in self.contacts[contact_name]:
                self.contacts[contact_name] = [new_phone_number]
                new_dict[contact_name] = [new_phone_number]
                return new_dict
            elif old_phone_number not in self.contacts[contact_name]:
                print('Errore: il numero di telefono non è presente!')
        else:
            print('Errore: il contatto non esiste')

    def list_contacts(self) -> list:
        new_list:list = []
        for key in self.contacts:
            return new_list.append(key)

    def list_phone_numbers(self, contact_name:str) -> list:
        new_list:list  = []
        if contact_name in self.contacts:
            new_list.append(self.contacts[contact_name])
            return new_list
        else:
            print('Errore: il contatto non esiste!')

    def search_contact_by_phone_number(self, phone_number:str) -> list:
        new_list:list = []
        for key, value in self.contacts.items():
            if phone_number in value:
                new_list.append(key)
                return new_list
            else:
                print('Nessun contatto trovato con questo numero di telefono!')

    
        