from pathlib import Path
from src.ui import *
from src.ui.widgets.search_button import SearchButton
from src.ui.widgets.infoblock import InfoBlock
from src.ui.template_main_window import TemplateWindow
from src.ui.widgets.searchbar import SearchBar


class MainWindow(TemplateWindow):
    def __init__(self) -> None:
        super().__init__()

        #Configure Window

        self.setWindowTitle("Weather Dashboard")
        #self.set

        #Configure layout

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()

        #Label
        label = QLabel("Insert City Name")
        label.setSizePolicy(QSizePolicy.Preferred,QSizePolicy.Fixed)
        layout.addWidget(label)

        #Text input
        search_bar = SearchBar()
        search_bar.setFixedSize(800, 40)
        layout.addWidget(search_bar)

        #Search button
        search_button = SearchButton()
        search_button.setFixedSize(100, 30)
        layout.addWidget(search_button)

        #Labels Box
        labels = InfoBlock("Weather Information")
        labels.setFixedSize(800, 400)
        layout.addWidget(labels)


        central_widget.setLayout(layout)












if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()

    style_path = Path(__file__).parent / "styles.qss"

    with open(style_path, 'r', encoding='utf8') as f:
        window.setStyleSheet(f.read())

    window.show()
    app.exec()

