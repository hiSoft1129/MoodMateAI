import sys
from PySide6.QtWidgets import QApplication
from ui.dashboard import Dashboard

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Dashboard()
    window.show()
    sys.exit(app.exec())