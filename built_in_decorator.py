import atexit
from datetime import datetime


class Library:
    """
    A class that describes a library.
    """
    def __init__(self, name: str, reader_number: int, num_of_book: int):
        self.name = name
        self.num_of_reader = reader_number
        self.num_of_books = num_of_book
        self.is_open = 'true'

    @staticmethod
    def information() -> None:
        """
        A function that prints the description of class.
        :return:None
        """
        print(f"class of Library information")

    @classmethod
    def reduce_num_of_books(cls, name: str, reader_number: int, num_of_book: int):
        """
        A function that reduces the number of books in the library by 1.
        :param name: The name of book
        :param reader_number: The current number of reader.
        :param num_of_book:The current number of book in library.
        :return: Updated library details.
        """
        return cls(name, reader_number, num_of_book-1)

    def print_library(self) -> None:
        """
        A function that prints the library details.
        :return:None
        """
        print(f"name: {self.name},reader_number:{self.num_of_reader},num_of_book{self.num_of_books}")


@atexit.register
def end_program():
    """
    A Function of print that be performed at the end of the program.
    :return:None
    """
    print(f"end program in {datetime.now()}")


if __name__ == '__main__':
    jerusalem_library = Library("jerusalem_library", 10, 10)
    end_program()
    Library.information()
    library = Library.reduce_num_of_books("jerusalem_library", 10, 10)
    library.print_library()
