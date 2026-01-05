from PySide6.QtWidgets import QGroupBox,QVBoxLayout,QLabel


class InfoBlock(QGroupBox):
    def __init__(self, title: str):
        super().__init__(title)

        # Initialize weather data
        self.WEATHER_FIELDS = {
            "City Name ": "--",
            "Current Temperature °C": "--",
            "Thermal Temperature": "--",
            "Weather Condition": "--",
            "Current Weather": "--",
            "Current Humidity": "--",
            "Wind Speed (km/h)": "--",
        }

        self._setup_ui()

    def _setup_ui(self) -> None:
        layout = QVBoxLayout()
        layout.setSpacing(10)
        self.labels = {}

        for key, value in self.WEATHER_FIELDS.items():
            label = QLabel(f"{key}: {value}")
            label.setObjectName("dataLabel")
            layout.addWidget(label)
            self.labels[key] = label

        self.setLayout(layout)

    def update_field(self, key: str, new_value: str) -> None:
        if key not in self.labels:
            raise KeyError(f"Campo '{key}' não existe")

        field_name = key.split(':')[0] if ':' in key else key
        self.labels[key].setText(f"{field_name}: {new_value}")