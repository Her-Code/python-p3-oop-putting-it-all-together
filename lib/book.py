#!/usr/bin/env python3

class Book:
    def __init__(self, title: str, page_count: int):
        self._title = title
        self._page_count = None
        self.page_count = page_count  # Use the property setter to apply validation

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value: str):
        if isinstance(value, str):
            self._title = value
        else:
            print("Title must be a string")

    @property
    def page_count(self) -> int:
        return self._page_count

    @page_count.setter
    def page_count(self, value: int):
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

    pass
    
        