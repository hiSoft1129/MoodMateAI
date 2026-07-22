from PySide6.QtWidgets import QWidget,QVBoxLayout,QLabel,QPushButton
from ui.theme import dark_theme

class Dashboard(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("MoodMate AI")
        self.resize(1000,700)
        self.setStyleSheet(dark_theme())

        layout=QVBoxLayout()

        layout.addWidget(
            QLabel("🧠 MoodMate AI Dashboard")
        )

        layout.addWidget(
            QLabel("Current Mood: Waiting...")
        )

        layout.addWidget(
            QPushButton("Start Camera Analysis")
        )

        self.setLayout(layout)