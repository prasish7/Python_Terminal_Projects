import sys
from pathlib import Path
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont ,QFontDatabase

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        self.initUI()
     
    def initUI(self):
        self.setWindowTitle('Digital Clock')
        self.setGeometry(50, 100, 300, 150)
        vBox = QVBoxLayout()
        vBox.addWidget(self.time_label)
        self.setLayout(vBox)
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet("font-size: 48px;"
        "color: LightGreen;"
        "background-color: Black;" \
        "border: 2px solid Gray;" \
        "border-radius: 10px;" \
        "padding: 10px;")
        font = QFontDatabase.addApplicationFont(
            str(Path(__file__).resolve().parent / "DS-DIGIT.TTF")
        )
        FONT_FAMILY = QFontDatabase.applicationFontFamilies(font)[0]
        MY_FONT = QFont(FONT_FAMILY, 48)
        self.time_label.setFont(MY_FONT)
        self.start() 
        self.timer.timeout.connect(self.start)
        self.timer.start(1000)  

    def start(self):
        current_time = QTime.currentTime().toString('hh:mm:ssAP')
        self.time_label.setText(current_time)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())
