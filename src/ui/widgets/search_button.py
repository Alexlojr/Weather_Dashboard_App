from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import Signal

class SearchButton(QPushButton):
    search_requested = Signal(str)

    def __init__(self, text: str = "Search") -> None:
        super().__init__(text)
