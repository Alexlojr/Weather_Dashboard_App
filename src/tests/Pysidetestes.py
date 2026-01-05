import sys
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Viewer")

        # Create a QLabel and set it as the central widget
        self.label = QLabel(self)
        self.setCentralWidget(self.label)

        # Load the image using QPixmap
        pixmap = QPixmap('src/resources/cold.png')  # Replace 'cat.jpg' with your image file path

        # Set the pixmap on the QLabel
        self.label.setPixmap(pixmap)

        # Optional: Resize the window to fit the image size
        self.resize(pixmap.width(), pixmap.height())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())
