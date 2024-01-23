from Bot_2 import AbstractBot
from Bot_2 import(
    AddBot,
    SearchBot,
    EditBot,
    RemoveBot,
    SaveBot,
    LoadBot,
    CongratulateBot,
    ViewBot,
    ExitBot)

class Assistant:
    Auto_Save_File = 'auto_save'

    def __init__(self):
        self.bot_list = {
            'add': AddBot(),
            'edit': EditBot(),
            'load': LoadBot(),
            'exit': ExitBot(),
            'view': ViewBot(),
            'congratulate': CongratulateBot(),
            'remove': RemoveBot(),
            'save': SaveBot(),
            'search': SearchBot(),
    }

    def display_commands(self):
        format_str = '{:^10}'
        for command in self.bot_list:
            print(format_str.format(command))

    def get_intance(self, action):
        if action in self.bot_list:
            return self.bot_list[action]
        else:
            return None
        
    def launch(self):
        print("Hello. I am your contact-assistant. What should I do with your contacts?")
        while True:
            self.display_commands()
            action = input('Enter action: ')
            if not action:
                continue
            if action not in self.bot_list:
                print(f'Unknown action: {action}')
                continue
            bot_instance = self.get_intance(action)
            if action in ['add', 'remove', 'edit']:
                bot_instance.handle()
            elif action == 'help':
                self.display_commands()
            elif action == 'exit':
                break

if __name__ == '__main__':
    assistant = Assistant()
    assistant.launch()


                        


            