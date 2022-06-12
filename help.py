from PyQt5.QtWidgets import*
import sys
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import *
from PyQt5.QtGui import *



class Player(QMainWindow):
    def __init__(self, master=None):
        QMainWindow.__init__(self, master)
        
        self.widget = QWidget(self)
        self.setCentralWidget(self.widget)

        self.setWindowTitle("Media Player")
        url= QUrl.fromLocalFile("path to video")
        content= QMediaContent(url)
        self.player = QMediaPlayer()
        self.player.setMedia(content)

        video_widget = QVideoWidget()

        self.player.setVideoOutput(video_widget)
        self.player.play()
        vlayout = QVBoxLayout()
        vlayout.addWidget(video_widget)
        self.widget.setLayout(vlayout)

        pixmap =QPixmap()
        pixmap.load("path to transparent image")
        my_label = QLabel(self)
        my_label.setPixmap(pixmap)
        my_label.setGeometry(300, 250, 100, 100)
        my_label.setFrameStyle(QFrame.NoFrame)
        my_label.setAttribute(Qt.WA_TranslucentBackground)


app=QApplication(sys.argv) # C.QCoreApplication(sys.argv)
player = Player()
player.resize(640, 480)
player.show()
player.player.stateChanged.connect( app.quit )
app.exec()