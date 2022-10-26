from pathlib import Path
from functools import partial
from PySide2.QtWidgets import QApplication, QWidget

from PySide2 import QtWidgets, QtCore, QtGui

current_dir = Path(__file__).parent

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self.setup_ui()
        self.create_file_model()
    
    def setup_ui(self):
        self.create_widgets()
        self.modify_widgets()
        self.create_layouts()
        self.add_widgets_to_layouts()
        self.add_actions_to_toolbar()
        self.setup_connections()

    def create_widgets(self):
        self.toolbar = QtWidgets.QToolBar()
        self.tree_view = QtWidgets.QTreeView()
        self.list_view = QtWidgets.QListView()
        self.sld_iconSize = QtWidgets.QSlider()
        self.main_widget = QtWidgets.QWidget()

    def modify_widgets(self):
        self.list_view.setViewMode(QtWidgets.QListView.IconMode)
        self.list_view.setUniformItemSizes(True)
        self.list_view.setIconSize(QtCore.QSize(48, 48))

        self.sld_iconSize.setRange(48, 256)
        self.sld_iconSize.setValue(48)

        self.tree_view.setSortingEnabled(True)
        self.tree_view.setAlternatingRowColors(True)
        self.tree_view.header().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)

    def create_layouts(self):
        self.main_layout = QtWidgets.QHBoxLayout(self.main_widget)
        
    def add_widgets_to_layouts(self):
        self.addToolBar(QtCore.Qt.TopToolBarArea, self.toolbar)
        self.setCentralWidget(self.main_widget)
        self.main_layout.addWidget(self.tree_view)
        self.main_layout.addWidget(self.list_view)
        self.main_layout.addWidget(self.sld_iconSize)

    def add_actions_to_toolbar(self):
        locations = ["home", "desktop", "documents", "music", "movies", "pictures"]
        for location in locations:
            action = QtWidgets.QAction(QtGui.QIcon(f"{current_dir.parent}/resources/base/{location}.svg"), location, self)
            action.triggered.connect(partial(self.change_location, location))
            self.toolbar.addAction(action)

    def change_location(self, location):
        standard_paths = QtCore.QStandardPaths()
        path = eval(f"standard_paths.standardLocations(QtCore.QStandardPaths.{location.capitalize()}Location)")
        path = path[0]
        self.tree_view.setRootIndex(self.model.index(path))
        self.list_view.setRootIndex(self.model.index(path))

    def setup_connections(self):
        self.tree_view.clicked.connect(self.tree_view_clicked)
        self.list_view.clicked.connect(self.listview_clicked)
        self.list_view.doubleClicked.connect(self.listview_double_clicked)
        self.sld_iconSize.valueChanged.connect(self.change_icon_size)

    def change_icon_size(self, value):
        self.list_view.setIconSize(QtCore.QSize(value, value))

    def create_file_model(self):
        self.model = QtWidgets.QFileSystemModel()
        root_path = QtCore.QDir.rootPath()
        self.model.setRootPath(root_path)
        self.tree_view.setModel(self.model)
        self.list_view.setModel(self.model)
        self.tree_view.setRootIndex(self.model.index(root_path))
        self.list_view.setRootIndex(self.model.index(root_path))
    
    def tree_view_clicked(self, index):
        if self.model.isDir(index):
            self.list_view.setRootIndex(index)
        else:
            self.list_view.setRootIndex(index.parent())
        
    def listview_clicked(self, index):
        self.tree_view.selectionModel().setCurrentIndex(index, QtCore.QItemSelectionModel.ClearAndSelect)

    def listview_double_clicked(self, index):
        self.list_view.setRootIndex(index)