from typing import Optional
from enum import Enum
from time import sleep


BOT_DELAY = 10 # TODO adjust to bot maybe config/env in common file


def execute_ls():
    raise NotImplementedError()


def execute_w():
    raise NotImplementedError()


def execute_id():
    raise NotImplementedError()


class CommandController(Enum):
    ls = 0
    w = 1
    id = 2

    def execute(self):
        if self == CommandController.ls:
            execute_ls()
        elif self == CommandController.w:
            pass
        elif self == CommandController.id:
            pass
        else:
            raise Exception(f'Unsupported Command: {self}')

class Controller:
    def __init__(self):
        self.bot_available = False
        print('> Controller instance created.')

    def check_for_bot(self):
        print(f'> Checking for bot via C&C channel.')
        self._alert_bot()
        # # TODO delay required based on max(api_max_rate, bot_delay)
        # wait ... display what is happening
        # scan feed for response
        # update availability

        # handle bot not available
        if not self.bot_available:
            print(f'Error: No bot found.')
            response = input(f'Check for bot? [Y/n]')
            if response.lower() not in ['yes', 'y']:
                exit(0)
            else:
                self.check_for_bot()


    def display_menu(self):
        print('> Commands:')
        if self.bot_available:
            print(f'2. id')
            print(f'3. ls')
            print(f'4. w')
        else:
            print(f'No commands are available (bot not available).')


    def loop(self):
        print('> Starting controller')        
        
        while True:
            if not self.bot_available:
                self.check_for_bot()

            self.display_menu()

            command = self.read_input_as_command()
            if not command:
                print('> Not valid command. Please input just the number.')
                continue

            command.execute()
            print('...waiting for bot to receive and process...')

            sleep(BOT_DELAY)

            response = self._scan_feed_for_response()
            print(response)


    def read_input_as_command(self) -> Optional[CommandController]:
        try:
            option = CommandController(int(input()))
            return option
        except ValueError:
            return None


    def _alert_bot(self):
        raise NotImplementedError
    

    def _scan_feed_for_bot(self):
        raise NotImplementedError
    
    def _scan_feed_for_response(self):
        raise NotImplementedError


def main():
    controller = Controller()
    controller.loop()
    

if __name__=='__main__':
    response = input('Do you wish to run the C&C controller? [Y/n]')
    if response.lower() not in ['yes', 'y']:
        print('Exiting')
        exit(0)

    main()