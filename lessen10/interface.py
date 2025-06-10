from abc import ABC , abstractmethod
class printabel(ABC):
    @abstractmethod
    def print_info(self):
        pass

class bool(printabel):
    def __init__(self, title ,author):
        self.title=title
        self.author=author
    def print_info(self):
        print(f"book:{self.title} by {self.author}")

libri=bool("hisja e maleve ", "isnail kadarea")
libri.print_info()