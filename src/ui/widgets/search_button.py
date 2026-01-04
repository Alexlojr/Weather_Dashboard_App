from src.ui import *

class SearchButton(QPushButton):

    def __init__(self,text="Search",parent=None) -> None:
        super().__init__(text,parent)




        self.clicked.connect(self.on_click)

    def on_click(self) -> None:
        print("test")




