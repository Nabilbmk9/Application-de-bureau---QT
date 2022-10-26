from pathlib import Path
from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtGui import QIcon

# Only needed for access to command line arguments
import sys

from package.main_window import MainWindow
current_file = Path(__file__).parent

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(open(f"{current_file}/resources/base/style.css").read())
    #change icon here
    app.setWindowIcon(QIcon(f"{current_file}/resources/base/64.png"))
    window = MainWindow()
    window.resize(550, 600)
    window.show()
    sys.exit(app.exec_())
