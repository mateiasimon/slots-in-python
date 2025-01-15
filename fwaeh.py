import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
a=0
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button = QPushButton("button", self)
        self.setWindowTitle("SigmaGUI")
        self.setGeometry(0, 0, 500, 500)
        self.initui()

    def initui(self):
        self.button.setGeometry(150, 200, 200, 100)
        self.button.setStyleSheet("font-size: 30px;")
        self.button.clicked.connect(self.on_click)

    def on_click(self):
        global a
        a=a+1
        print(a)
        self.button.setText("button count")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
