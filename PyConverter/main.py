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
    window = MainWindow()
    window.resize(1920 / 4, 1200 / 2)
    window.show()
    sys.exit(app.exec_())
