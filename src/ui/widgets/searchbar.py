from PySide6.QtWidgets import QLineEdit
from PySide6.QtCore import Signal


class SearchBar(QLineEdit):
    # Signal when Enter is Pressed
    search_triggered = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setPlaceholderText("Enter city name (e.g., London, Paris)...")
        self.returnPressed.connect(self.search_triggered.emit)