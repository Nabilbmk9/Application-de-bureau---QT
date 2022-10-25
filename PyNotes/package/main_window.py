from PySide2 import QtWidgets, QtGui

from package.api.note import Note, get_notes

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyNotes")
        self.setup_ui()

        self.populate_notes()
    
    def setup_ui(self):
        self.create_widgets()
        self.create_layouts()
        self.modify_widgets()
        self.add_widgets_to_layouts()
        self.setup_connections()

    def create_widgets(self):
        self.btn_createNote = QtWidgets.QPushButton("Create Note")
        self.lw_notes = QtWidgets.QListWidget()
        self.te_content = QtWidgets.QTextEdit()
    def modify_widgets(self):
        pass

    def create_layouts(self):
        self.main_layout = QtWidgets.QGridLayout(self)

    def add_widgets_to_layouts(self):
        self.main_layout.addWidget(self.btn_createNote, 0, 0, 1, 1)
        self.main_layout.addWidget(self.lw_notes, 1, 0, 1, 1)
        self.main_layout.addWidget(self.te_content, 0, 1, 2, 1)

    def setup_connections(self):
        self.btn_createNote.clicked.connect(self.create_note)
        self.te_content.textChanged.connect(self.save_note)
        self.lw_notes.itemSelectionChanged.connect(self.populate_note_content)
        QtWidgets.QShortcut(QtGui.QKeySequence("Backspace"), self.lw_notes, self.delete_selected_note)

    def add_note_to_listwidget(self, note):
        lw_item = QtWidgets.QListWidgetItem(note.title)
        lw_item.note = note
        self.lw_notes.addItem(lw_item)

    def create_note(self):
        title, result = QtWidgets.QInputDialog.getText(self, "Create Note", "Title: ")
        if result and title:
            note = Note(title=title)
            note.save()
            self.add_note_to_listwidget(note)

    def delete_selected_note(self):
        print("Delete Note")
    
    def populate_notes(self):
        notes = get_notes()
        for note in notes:
            self.add_note_to_listwidget(note)

    def populate_note_content(self):
        print("Populate Note Content")

    def save_note(self):
        print("Save Note")