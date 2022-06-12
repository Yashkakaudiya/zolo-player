from PyQt5.QtWidgets import*
import sys
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Style import *
from DarkMode import *
class zolo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Zoloplay")
        self.setWindowIcon(QIcon("images/zolo1.png"))
        self.setGeometry(200,200,760,600)
        # calling menubar function
        self.menuBar()
        # calling videosurface function
        self.videoSurface()

    def  videoSurface(self):

    # videosurface********************************
        self.mediaPlay=QMediaPlayer(self,QMediaPlayer.VideoSurface)
        self.videoWidget=VideoWidget()
        if self.videoWidget!='':
            self.videoWidget.setWindowIcon(QIcon('images/zolo1.png'))

        # self.videoWidget.setStyleSheet('background: black;')
        


        self.playlist = QMediaPlaylist()
        self.mediaPlay.setPlaylist(self.playlist)      




    #  Play button ******************************* 
        self.playButton=QPushButton()
        self.playButton.setEnabled(False)
        self.playButton.setIcon(QIcon('png/003-play-button.png'))
        self.playButton.setStyleSheet('background-color:transparent;')
        self.playButton.setIconSize(QSize(40,40))
        self.playButton.setMaximumWidth(40)
        self.playButton.clicked.connect(self.playVideo)
        self.playButton.clicked.connect(self.play_to_pauseBTN)




    # pause button ********************************
        self.PreviousButton=QPushButton()
        self.PreviousButton.setEnabled(False)
        self.PreviousButton.setIcon(QIcon('png/001-previous.png'))   
        self.PreviousButton.setStyleSheet('background-color:transparent;')
        self.PreviousButton.setIconSize(QSize(40,40))
        self.PreviousButton.setMaximumWidth(40)
        self.PreviousButton.pressed.connect(self.playlist.previous)




    # next button ********************************
        self.nextButton=QPushButton()
        self.nextButton.setEnabled(False)
        self.nextButton.setIcon(QIcon('png/002-next.png'))
        self.nextButton.setStyleSheet('background-color:transparent;')
        self.nextButton.setIconSize(QSize(40,40))
        self.nextButton.setMaximumWidth(40)
        self.nextButton.pressed.connect(self.playlist.next)





    # slider *************************************
        self.slider=QSlider(Qt.Horizontal)
        self.slider.setRange(0,0)
        self.slider.sliderMoved.connect(self.moveSlider)
        




    # volume button**********************************
        self.iconVol=QPushButton()
        self.iconVol.setIcon(QIcon('png/004-volume-1.png'))
        self.iconVol.setStyleSheet("background-color:transparent")
        self.iconVol.setEnabled(False)
        self.iconVol.setIconSize(QSize(30,30))
        self.iconVol.setMaximumWidth(30)

        self.iconVol.clicked.connect(self.muteUnmute)

        



    # slider for volume******************************************************
        self.sliderVol=QSlider(Qt.Horizontal)
        self.sliderVol.setEnabled(True)
        self.sliderVol.setRange(0,100)
        self.sliderVol.setMaximumWidth(130)
        self.sliderVol.setSliderPosition(70)
        self.sliderVol.valueChanged.connect(self.mediaPlay.setVolume)
        
        


        # hbox layout ********************************
        hBoxlayout=QHBoxLayout()
        hBoxlayout.setContentsMargins(0,0,0,0)




    #     # set widget to layout 




        hBoxlayout2=QHBoxLayout()
        hBoxlayout2.setContentsMargins(0,0,0,0)
        hBoxlayout.addWidget(self.slider)
        hBoxlayout2.addWidget(self.PreviousButton)
        hBoxlayout2.addWidget(self.playButton)
        hBoxlayout2.addWidget(self.nextButton)
        hBoxlayout2.addWidget(self.iconVol)
        hBoxlayout2.addWidget(self.sliderVol)




    # vbox layout ********************************
        vBoxlayout=QVBoxLayout()
        vBoxlayout.addWidget(self.videoWidget)
        vBoxlayout.addLayout(hBoxlayout)
        vBoxlayout.addLayout(hBoxlayout2)
        self.setLayout(vBoxlayout)
        self.mediaPlay.setVideoOutput(self.videoWidget)



    # connect function to player *********************************
        self.mediaPlay.positionChanged.connect(self.sliderBarPosition)
        self.mediaPlay.durationChanged.connect(self.sliderBarRange)



# Function to open the file ****************************************
    def openFile(self):
        fileName, _= QFileDialog.getOpenFileNames(self, 'open video')
        if fileName !='':
            self.playButton.setEnabled(True)
            self.nextButton.setEnabled(True)
            self.PreviousButton.setEnabled(True)
            self.iconVol.setEnabled(True)
            self.addToPlaylist(fileName)

    def addToPlaylist(self,fileName):
        for name in fileName:
            fileInfo = QFileInfo(name)
            if fileInfo.exists():
                url = QUrl.fromLocalFile(fileInfo.absoluteFilePath())
                if fileInfo.suffix().lower() == 'm3u':
                    self.playlist.load(url)
                else:
                    self.playlist.addMedia(QMediaContent(url))
            else:
                url = QUrl(name)
                if url.isValid():
                    self.playlist.addMedia(QMediaContent(url))




# function for play video ******************************************
    def playVideo(self):
        if self.mediaPlay.state()== QMediaPlayer.PlayingState:
            self.mediaPlay.pause()
        else:
            self.mediaPlay.play()




# function for change the state of play button ***********************
    def play_to_pauseBTN(self):
        if self.mediaPlay.state()==QMediaPlayer.PlayingState:
            self.playButton.setIcon(QIcon('png/002-pause.png'))
        else:
            self.playButton.setIcon(QIcon('png/007-play-button-1.png'))
 
# volume button function *****************************************
    def muteUnmute(self):
        if self.mediaPlay.mediaStatus() == 6 :
            if self.mediaPlay.isMuted() == 1:
                self.mediaPlay.setMuted(0)
                self.iconVol.setIcon(QIcon('png/004-volume-1.png'))
                self.sliderVol.setSliderPosition(70)
            elif self.mediaPlay.isMuted() == 0:
                self.mediaPlay.setMuted(1)
                self.iconVol.setIcon(QIcon('png/003-mute-1.png')) 
                self.sliderVol.setSliderPosition(0)
# slider to zero when muted *****************************************

#  function for change the position of slider **********************************
    def sliderBarPosition(self,sliderposition):
        self.slider.setValue(sliderposition)




# function for move according to the size of video ****************************
    def sliderBarRange(self,sliderDuration):
        self.slider.setRange(0,sliderDuration)




# function for rander the slider ****************************
    def moveSlider(self,position):
        self.mediaPlay.setPosition(position)


    def menuBar(self):
        self.myQMenuBar =QMenuBar(self)
        self.FileMenu = self.myQMenuBar.addMenu('File')
        self.Open_File=QAction('Open File',self)
        self.Open_File.setShortcut("ctrl+o")
        self.Open_File.triggered.connect(self.openFile)
        self.FileMenu.addAction(self.Open_File)
        self.setting=self.myQMenuBar.addMenu('Settings')
        self.dark_Mode=QAction('DarkMode',self, checkable=True)
        self.dark_Mode.setShortcut("ctrl+d")
        self.dark_Mode.setChecked(False)
        self.dark_Mode.triggered.connect(self.toggleMenu)

        self.setting.addAction(self.dark_Mode)
        self.exitAction =QAction('Exit',self)        
        self.exitAction.triggered.connect(qApp.quit)
        self.FileMenu.addAction(self.exitAction)
    def toggleMenu(self, state):
        if state:
            self.show()

        else:
            self.show()



# class to get fullscreen**************************
class VideoWidget(QVideoWidget):

    def __init__(self, parent=None):
        super(VideoWidget, self).__init__(parent)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape and self.isFullScreen():
            self.setFullScreen(False)
            event.accept()
        elif event.key() == Qt.Key_Enter and event.modifiers() & Qt.Key_Alt:
            self.setFullScreen(not self.isFullScreen())
            event.accept()
        else:
            super(VideoWidget, self).keyPressEvent(event)
    def mouseDoubleClickEvent(self, event):
        self.setFullScreen(not self.isFullScreen())
        event.accept()
 
class PlaylistModel(QAbstractItemModel):

    Title, ColumnCount = range(2)

    def __init__(self, parent=None):
        super(PlaylistModel, self).__init__(parent)

        self.m_playlist = None

    def rowCount(self, parent=QModelIndex()):
        return self.m_playlist.mediaCount() if self.m_playlist is not None and not parent.isValid() else 0

    def columnCount(self, parent=QModelIndex()):
        return self.ColumnCount if not parent.isValid() else 0

    def index(self, row, column, parent=QModelIndex()):
        return self.createIndex(row, column) if self.m_playlist is not None and not parent.isValid() and row >= 0 and row < self.m_playlist.mediaCount() and column >= 0 and column < self.ColumnCount else QModelIndex()

    def parent(self, child):
        return QModelIndex()

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid() and role == Qt.DisplayRole:
            if index.column() == self.Title:
                location = self.m_playlist.media(index.row()).canonicalUrl()
                return QFileInfo(location.path()).fileName()

            return self.m_data[index]

        return None

    def playlist(self):
        return self.m_playlist

    def setPlaylist(self, playlist):
        if self.m_playlist is not None:
            self.m_playlist.mediaAboutToBeInserted.disconnect(
                    self.beginInsertItems)
            self.m_playlist.mediaInserted.disconnect(self.endInsertItems)
            self.m_playlist.mediaAboutToBeRemoved.disconnect(
                    self.beginRemoveItems)
            self.m_playlist.mediaRemoved.disconnect(self.endRemoveItems)
            self.m_playlist.mediaChanged.disconnect(self.changeItems)

        self.beginResetModel()
        self.m_playlist = playlist

        if self.m_playlist is not None:
            self.m_playlist.mediaAboutToBeInserted.connect(
                    self.beginInsertItems)
            self.m_playlist.mediaInserted.connect(self.endInsertItems)
            self.m_playlist.mediaAboutToBeRemoved.connect(
                    self.beginRemoveItems)
            self.m_playlist.mediaRemoved.connect(self.endRemoveItems)
            self.m_playlist.mediaChanged.connect(self.changeItems)

        self.endResetModel()

    def beginInsertItems(self, start, end):
        self.beginInsertRows(QModelIndex(), start, end)

    def endInsertItems(self):
        self.endInsertRows()

    def beginRemoveItems(self, start, end):
        self.beginRemoveRows(QModelIndex(), start, end)

    def endRemoveItems(self):
        self.endRemoveRows()

    def changeItems(self, start, end):
        self.dataChanged.emit(self.index(start, 0),
                self.index(end, self.ColumnCount))


    
        
app=QApplication(sys.argv)
window=zolo()
app.setStyleSheet(darkMode)
window.show()
sys.exit(app.exec_())





# how to style title head 