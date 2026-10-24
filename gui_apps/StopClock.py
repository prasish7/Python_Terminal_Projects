import sys
from pathlib import Path
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QHBoxLayout  
from PyQt5.QtCore import QTimer, QTime, Qt 
from PyQt5.QtGui import QFont ,QFontDatabase

class StopWatch(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 100, 300, 200)
        self.setWindowTitle('Stop Watch')
        self.time = QTime(0, 0, 0, 0)
        self.time_label = QLabel('00:00:00.00', self)
        self.time_label.setAlignment(Qt.AlignCenter)
        self.startTimer = QPushButton('Start', self)
        self.stopTimer = QPushButton('Stop', self)
        self.resetTimer = QPushButton('Reset', self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        # vbox.addWidget(self.startTimer)
        # vbox.addWidget(self.stopTimer)
        # vbox.addWidget(self.resetTimer)
        self.setLayout(vbox)
        hbox = QHBoxLayout()
        hbox.addWidget(self.startTimer)
        hbox.addWidget(self.stopTimer)
        hbox.addWidget(self.resetTimer)
        vbox.addLayout(hbox)
        self.setStyleSheet(''' 
                           QPushButton {
                font-size: 20px;
                color: LightGreen;
                background-color: Black;
                border: 2px solid Gray;
                border-radius: 10px;
                padding: 10px;}
                            QLabel { 
                font-size: 24px;
                color: LightGreen;
                background-color: Black;
                border: 2px solid Gray;
                border-radius: 10px;
                padding: 10px;}
                           ''')
        self.startTimer.clicked.connect(self.start)
        self.stopTimer.clicked.connect(self.stop)
        self.resetTimer.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_display)
        font = QFontDatabase.addApplicationFont(
            str(Path(__file__).resolve().parent / "DS-DIGIT.TTF")
        )
        FONT_FAMILY = QFontDatabase.applicationFontFamilies(font)[0]
        MY_FONT = QFont(FONT_FAMILY, 48)
        self.time_label.setFont(MY_FONT)


    def start(self):
        self.timer.start(10)

    def stop(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.time_label.setText('00:00:00.00')

    def formatTime(self , time):
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        milliseconds = time.msec() // 10
        return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}"

    def update_display(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.formatTime(self.time))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    stopwatch = StopWatch()
    stopwatch.show()
    sys.exit(app.exec_())