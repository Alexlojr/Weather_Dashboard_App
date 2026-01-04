from src.ui import *



class TemplateWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self) -> None:
        self.setWindowTitle("Template Window")
        self.setGeometry(500, 150, 1200, 700)













if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TemplateWindow()
    window.show()
    app.exec()

