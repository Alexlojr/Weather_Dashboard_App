import sys
import os

from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QApplication, QHBoxLayout, QMessageBox
from pathlib import Path
from dotenv import load_dotenv
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap

from src.ui.widgets.search_button import SearchButton
from src.ui.widgets.infoblock import InfoBlock
from src.ui.widgets.searchbar import SearchBar
from src.ui.template_main_window import BaseWindow
from src.services.weatherAPI import WeatherService


class MainWindow(BaseWindow):
    def __init__(self) -> None:
        super().__init__()

        # Inicializar serviço
        load_dotenv()
        api_key = os.getenv('API_KEY')

        if not api_key:
            self._show_error("API Key não encontrada! Configure o arquivo .env")

        self.weather_service = WeatherService(api_key)

        self.setWindowTitle("Weather Dashboard")
        self.setup_ui()

    def setup_ui(self) -> None:
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

        search_label = QLabel("City:")
        search_layout.addWidget(search_label)

        self.search_bar = SearchBar()
        self.search_bar.search_triggered.connect(self.handle_search)  # Enter
        search_layout.addWidget(self.search_bar, 1)

        self.search_button = SearchButton()
        self.search_button.setFixedSize(100, 40)
        self.search_button.clicked.connect(self.handle_search)  # Click
        search_layout.addWidget(self.search_button)

        main_layout.addWidget(search_container)

        # === Weather Image ===
        self.weather_image = QLabel()
        self.weather_image.setFixedHeight(120)
        self.weather_image.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.weather_image)

        # === Info Block ===
        self.info_block = InfoBlock("Weather Information")
        main_layout.addWidget(self.info_block)

        # Push content to top
        main_layout.addStretch()

    def handle_search(self) -> None:
        """Handle search button click or Enter press"""
        city = self.search_bar.text().strip()

        if not city:
            self._show_error("Please enter a city name!")
            return

        # Disable button during search
        self.search_button.setEnabled(False)
        self.search_button.setText("Searching...")

        try:
            # Search data
            weather = self.weather_service.get_weather_by_city(city)

            temperature = weather.temperature_celsius

            if temperature < 15:
                self._apply_cold_theme()
            elif temperature > 30:
                self._apply_hot_theme()
            else:
                self._apply_default_theme()

            # Update UI
            self.info_block.update_field("City Name ", weather.city_name)
            self.info_block.update_field("Current Temperature °C",f"{weather.temperature_celsius}")
            self.info_block.update_field("Thermal Temperature",f"{weather.feels_like_celsius}°C")
            self.info_block.update_field("Weather Condition",weather.condition)
            self.info_block.update_field("Current Weather",weather.description.capitalize())
            self.info_block.update_field("Current Humidity",f"{weather.humidity}%")
            self.info_block.update_field("Wind Speed (km/h)",f"{weather.wind_speed} m/s")

            # Clear
            self.search_bar.clear()

        except ValueError as e:
            self._show_error(str(e))
        except Exception as e:
            self._show_error(f"Unexpected error: {str(e)}")
        finally:
            self.search_button.setEnabled(True)
            self.search_button.setText("Search")

    def _show_error(self, message: str) -> None:
        """Show error dialog"""
        QMessageBox.warning(self, "Error", message)

    def _apply_cold_theme(self):
        self.setProperty("theme", "cold")
        self.style().unpolish(self)
        self.style().polish(self)

        pixmap = QPixmap("src/resources/cold.png")
        self.weather_image.setPixmap(pixmap.scaled(
            100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation
        ))

    def _apply_hot_theme(self):
        self.setProperty("theme", "hot")
        self.style().unpolish(self)
        self.style().polish(self)

        pixmap = QPixmap("src/resources/sun.png")
        self.weather_image.setPixmap(pixmap.scaled(
            100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation
        ))

    def _apply_default_theme(self):
        self.setProperty("theme", "default")
        self.style().unpolish(self)
        self.style().polish(self)

        self.weather_image.clear()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()

    style_path = Path(__file__).parent / "styles.qss"

    with open(style_path, 'r', encoding='utf8') as f:
        window.setStyleSheet(f.read())

    window.show()
    app.exec()

