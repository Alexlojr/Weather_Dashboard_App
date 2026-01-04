from src.ui import *


class InfoBlock(QGroupBox):

    def __init__(self, title, parent=None):
        super().__init__(title, parent)

        Weather_Data = {
            "Current Temperature °C": "--",
            "Thermal Temperature": "--",
            "Weather Condition": "--",
            "Current Weather": "--",
            "Current Humidity": "--",
            "Wind Speed (km/h)": "--",
        }

        self.layout = QVBoxLayout()
        self.labels = {}  # Dictionary to store and reference labels easily

        for key, value in Weather_Data.items():
            # Create a label for each data item
            label_text = f"{key}: {value}"
            label = QLabel(label_text)
            label.setWordWrap(True)  # Enable word wrapping for long text
            self.layout.addWidget(label)
            self.labels[key] = label  # Store reference to the label

        self.setLayout(self.layout)

    def update_field(self, key, new_value):
        """Method to update a specific label's text by its key."""
        if key in self.labels:
            current_text = self.labels[key].text().split(':')[0]
            self.labels[key].setText(f"{current_text}: {new_value}")