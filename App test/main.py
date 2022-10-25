from PySide2.QtWidgets import QApplication, QWidget

# Only needed for access to command line arguments
import sys

from package.main_window import MainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    #changer la taille de l'ecran
    window.resize(250, 250)
    window.show()
    sys.exit(app.exec_())

# Your application won't reach here until you exit and the event
# loop has stopped