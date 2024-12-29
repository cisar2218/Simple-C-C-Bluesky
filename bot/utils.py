from enum import Enum


class CommandBot(Enum):
    ls = 0
    w = 1
    id = 2

    def execute(self):
        if self == CommandBot.ls:
            execute_ls()
        elif self == CommandBot.w:
            pass
        elif self == CommandBot.id:
            pass
        else:
            raise Exception(f'Unsupported Command: {self}')


def execute_ls():
    raise NotImplementedError()


def execute_w():
    raise NotImplementedError()


def execute_id():
    raise NotImplementedError()


class Post:
    pass