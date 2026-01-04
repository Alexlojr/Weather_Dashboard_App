from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import Signal

class SearchButton(QPushButton):
    # Define signal customizado
    search_requested = Signal(str)  # Emite a cidade buscada

    def __init__(self, text: str = "Search") -> None:
        super().__init__(text)
        self.clicked.connect(self._on_click)

    def _on_click(self) -> None:
        # Emite signal para quem estiver escutando
        self.search_requested.emit("")  # MainWindow vai passar a cidade
        print("test")

