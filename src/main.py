import sys
from pathlib import Path
from PySide6.QtWidgets import QApplication

from ui.main_window import MainWindow


def load_stylesheet(app: QApplication) -> None:
    """Load QSS """
    style_path = Path(__file__).parent / "ui" / "styles.qss"

    if not style_path.exists():
        print(f"Style file not found: {style_path}")
        return

    with open(style_path, 'r', encoding='utf-8') as f:
        app.setStyleSheet(f.read())


def main() -> None:
    app = QApplication(sys.argv)
    app.setApplicationName("Weather Dashboard")

    load_stylesheet(app)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()