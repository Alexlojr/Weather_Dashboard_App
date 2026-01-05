import sys
import os

from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel,QApplication,QHBoxLayout
from pathlib import Path
from dotenv import load_dotenv

from src.ui.widgets.search_button import SearchButton
from src.ui.widgets.infoblock import InfoBlock
from src.ui.widgets.searchbar import SearchBar
from src.ui.template_main_window import BaseWindow
from src.services.weatherAPI import WeatherService


class MainWindow(BaseWindow):
    def __init__(self) -> None:
        super().__init__()

        load_dotenv()
        api_key = os.getenv('API_KEY')
        self.weather_service = WeatherService(api_key)


        self.setWindowTitle("Weather Dashboard")

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Main Layout
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(40, 40, 40, 40)
        main_layout.setSpacing(20)

        # Header
        header_label = QLabel("Weather Dashboard")
        header_label.setObjectName("headerTitle")
        main_layout.addWidget(header_label)

        # === Search Area ===
        search_container = QWidget()
        search_layout = QHBoxLayout(search_container)
        search_layout.setContentsMargins(0, 0, 0, 0)

        search_label = QLabel("City Name:")
        search_layout.addWidget(search_label)

        self.search_bar = SearchBar()
        search_layout.addWidget(self.search_bar, 1)

        self.search_button = SearchButton()
        self.search_button.setFixedSize(100, 40)
        self.search_button.clicked.connect(self._handle_search)
        search_layout.addWidget(self.search_button)

        main_layout.addWidget(search_container)

        # === Info Block ===
        self.info_block = InfoBlock("Weather Information")
        main_layout.addWidget(self.info_block)

        # === Push content to top ===
        main_layout.addStretch()

    def _handle_search(self) -> None:
        city = self.search_bar.text().strip()
        if not city:
            print("Digite uma cidade!")
            return

        print(f"Buscando: {city}")

    # def search_weather(self):
    #     city = self.city_input.text()
    #
    #     try:
    #         # Recebe objeto WeatherData
    #         weather = self.weather_service.get_weather_by_city(city)
    #
    #         # Acessa dados facilmente
    #         self.temp_label.setText(f"{weather.temperature_celsius}°C")
    #         self.condition_label.setText(weather.condition)
    #         self.humidity_label.setText(f"{weather.humidity}%")
    #
    #     except ValueError as e:
    #         self.show_error(str(e))






if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()

    style_path = Path(__file__).parent / "styles.qss"

    with open(style_path, 'r', encoding='utf8') as f:
        window.setStyleSheet(f.read())

    window.show()
    app.exec()

