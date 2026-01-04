#import sys
from PySide6.QtWidgets import QMainWindow

class BaseWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self) -> None:
        self.setWindowTitle("Template Window")
        self.setGeometry(500, 150, 1200, 700)













if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BaseWindow()
    window.show()
    app.exec()

