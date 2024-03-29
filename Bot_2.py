from AddressBook import *
from abc import ABC , abstractmethod

class AbstractBot(ABC):
    def __init__(self):
        self.book = AddressBook()

    @abstractmethod
    def handle(self):
        pass


class AddBot(AbstractBot):
    def handle(self):
        record = self.created_record()
        return self.book.add(record)
    
    def created_record(self):
        name = Name(input("Name: ")).value.strip()
        phones = Phone().value
        birth = Birthday().value
        email = Email().value.strip()
        status = Status().value.strip()
        note = Note(input("Note: ")).value
        return Record(name, phones, birth, email, status, note)
    

class SearchBot(AbstractBot):
    def handle(self):
        print("There are following categories: \nName \nPhones \nBirthday \nEmail \nStatus \nNote")
        category = input('Search category: ')
        pattern = input('Search pattern: ')
        result = (self.book.search(pattern, category))
        self.show_result(result)

    def show_result(self, result):
        for el in result:
            if el['birthday']:
                birth = el['birthday'].strftime("%d/%m/%Y")
                result = "_" * 50 + "\n" + f"Name: {el['name']} \nPhones: {', '.join(el['phones'])} \nBirthday: {birth} \nEmail: {el['email']} \nStatus: {el['status']} \nNote: {el['note']}\n" + "_" * 50
                print(result)


class EditBot(AbstractBot):
    def handle(self):
        contact_name = input('Contact name: ')
        parameter = input('Which parameter to edit(name, phones, birthday, status, email, note): ').strip()
        new_value = input("New Value: ")
        return self.book.edit(contact_name, parameter, new_value)


class RemoveBot(AbstractBot):
    def handle(self):
        pattern = input("Remove (contact name or phone): ")
        return self.book.remove(pattern)


class SaveBot(AbstractBot):
    def handle(self):
        file_name = input("File name: ")
        return self.book.save(file_name)
    

class LoadBot(AbstractBot):
    def handle(self):
        file_name = input("File name: ")


class CongratulateBot(AbstractBot):
    def handle(self):
        print(self.book.congratulate())


class ViewBot(AbstractBot):
    def handle(self):
        print(self.book)


class ExitBot(AbstractBot):
    def handle(self):
        print('Goodluck have fun!')
        exit()



    

