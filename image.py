import cv2
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import sys

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 textbox - pythonspot.com'
        self.left = 100
        self.top = 100
        self.width = 500
        self.height = 140
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280, 40)

        # Create a button in the window
        self.button2 = QPushButton('Orignal', self)
        self.button2.move(150, 80)
        self.button1 = QPushButton('Make image blur', self)
        self.button1.move(20, 80)

        # connect button to function on_click
        self.button2.clicked.connect(self.image)
        self.button1.clicked.connect(self.imageblur)
        self.show()

    def image(self):
        textboxValue = self.textbox.text()
        for word in textboxValue:
            if word == "\\":
                textboxValue.replace("\\","/")
        img = cv2.imread(textboxValue)
        cv2.imshow("orignal", img)
        cv2.waitKey()
        print(img)
        cv2.destroyAllWindows()


    def imageblur(self):
        textboxValue = self.textbox.text()
        for word in textboxValue:
            if word == "\\":
                textboxValue.replace("\\","/")
        img = cv2.imread(textboxValue)
        img = img + 10
        cv2.imshow("blur", img)
        cv2.waitKey()
        print(img)
        cv2.destroyAllWindows()

    @pyqtSlot()
    def on_click(self):
        textboxValue = self.textbox.text()
        QMessageBox.question(self, 'Message - pythonspot.com', "You typed: " + textboxValue, QMessageBox.Ok,
                             QMessageBox.Ok)
        self.textbox.setText("")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
