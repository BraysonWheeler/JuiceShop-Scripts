from abc import ABC, abstractmethod

class IiFile(ABC):
    """ Interface for input file import"""
    @abstractmethod
    def get():
        pass

class GetIP(IiFile):
    """ Gets IP which exist first line"""

    def get(file) -> str:
        with open(file, "r") as f:
            return f.readline().rstrip('\n')

class GetEmails(IiFile):
    """ Returns lists with emails"""

    def get(file) -> list:
        contents = []
        with open(file, "r") as f:
            for line in iter(f.readline, ""):
                contents.append(line.rstrip('\n'))
        del contents[0] # Remove IP
        return contents


class GetContentsOfFile:
    def __init__(self, file, context):
        self.file = file
        self.context = context

    def get(self):
        if self.context == 'emails':
            return GetEmails.get(self.file)
        elif self.context == 'ip':
            return GetIP.get(self.file)

