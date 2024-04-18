#main_menue.py
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap, QTransform, QIcon
from PyQt5.QtCore import pyqtSignal, Qt

class MyWindow(QWidget):
    go_back = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Main Menue")
        self.setGeometry(100, 100, 400, 300)

        self.button_layout = QGridLayout()

        self.Account_button = QPushButton("Account Management", self)

        
        self.button_layout.addWidget(self.Account_button, 0, 0, 1, 2)

        self.financial_button = QPushButton("Financial Transactions ", self)

        self.button_layout.addWidget(self.financial_button, 1, 0, 1, 2)

        self.loun_button = QPushButton("Invest and Loan", self)

        self.button_layout.addWidget(self.loun_button, 2, 0, 1, 2)

        self.back_button = QPushButton("Back", self)

        self.button_layout.addWidget(self.back_button, 3, 0, 1, 1)
        spacer = QLabel("", self)
        self.button_layout.addWidget(spacer, 3, 1, 1, 1)
        
        self.setLayout(self.button_layout)
  

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MyWindow()
    window.show()

    sys.exit(app.exec_())

