from functools import partial

from PySide2 import QtWidgets, QtMultimedia, QtMultimediaWidgets, QtCore

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyPlayer")

        self.open_icon = self.style().standardIcon(QtWidgets.QStyle.SP_DriveDVDIcon)
        self.play_icon = self.style().standardIcon(QtWidgets.QStyle.SP_MediaPlay)
        self.previous_icon = self.style().standardIcon(QtWidgets.QStyle.SP_MediaSkipBackward)
        self.pause_icon = self.style().standardIcon(QtWidgets.QStyle.SP_MediaPause)
        self.stop_icon = self.style().standardIcon(QtWidgets.QStyle.SP_MediaStop)

        self.setup_ui()
    
    def setup_ui(self):
        self.create_widgets()
        self.modify_widgets()
        self.create_layouts()
        self.add_widgets_to_layouts()
        self.setup_connections()

    def create_widgets(self):
        self.video_widget = QtMultimediaWidgets.QVideoWidget()
        self.player = QtMultimedia.QMediaPlayer()
        self.toolber = QtWidgets.QToolBar()
        self.file_menu = self.menuBar().addMenu("File")

        # ACTIONS
        self.act_open = self.file_menu.addAction(self.open_icon, "Open")
        self.act_open.setShortcut("Ctrl+O")
        self.act_play = self.toolber.addAction(self.play_icon, "Play")
        self.act_previous = self.toolber.addAction(self.previous_icon, "Previous")
        self.act_pause = self.toolber.addAction(self.pause_icon, "Pause")
        self.act_stop = self.toolber.addAction(self.stop_icon, "Stop")

    def modify_widgets(self):
        pass

    def create_layouts(self):
        pass

    def add_widgets_to_layouts(self):
        self.addToolBar(self.toolber)
        self.setCentralWidget(self.video_widget)
        self.player.setVideoOutput(self.video_widget)

    def setup_connections(self):
        self.act_open.triggered.connect(self.open)
        self.act_play.triggered.connect(self.player.play)
        self.act_pause.triggered.connect(self.player.pause)
        self.act_stop.triggered.connect(self.player.stop)
        self.act_previous.triggered.connect(partial(self.player.setPosition, 0))
        self.player.stateChanged.connect(self.update_ui)

    def open(self):
        file_dialog = QtWidgets.QFileDialog(self)
        file_dialog.setMimeTypeFilters(["video/mp4"])
        movies_dir = QtCore.QStandardPaths.writableLocation(QtCore.QStandardPaths.MoviesLocation)
        file_dialog.setDirectory(movies_dir)
        if file_dialog.exec_() == QtWidgets.QDialog.Accepted:
            movie = file_dialog.selectedUrls()[0]
            self.player.setMedia(movie)
            self.player.play()
    
    def update_ui(self, state):
        if state == QtMultimedia.QMediaPlayer.PlayingState:
            self.act_play.setEnabled(False)
            self.act_pause.setEnabled(True)
            self.act_stop.setEnabled(True)
        else:
            self.act_play.setEnabled(True)
            self.act_pause.setEnabled(False)
            self.act_stop.setEnabled(False)