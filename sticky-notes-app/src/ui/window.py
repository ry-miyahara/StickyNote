from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QWidget, QListWidget, QListWidgetItem
from PyQt5.QtCore import Qt
from notes.manager import NoteManager

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sticky Notes")
        self.setGeometry(100, 100, 400, 300)

        self.note_manager = NoteManager()
        self.init_ui()

    def init_ui(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.note_list = QListWidget()
        self.layout.addWidget(self.note_list)

        self.note_text = QTextEdit()
        self.layout.addWidget(self.note_text)

        self.add_button = QPushButton("Add Note")
        self.add_button.clicked.connect(self.add_note)
        self.layout.addWidget(self.add_button)

        self.note_list.itemClicked.connect(self.display_note)

    def add_note(self):
        title = f"Note {self.note_list.count() + 1}"
        content = self.note_text.toPlainText()
        self.note_manager.add_note(title, content)
        self.note_list.addItem(QListWidgetItem(title))
        self.note_text.clear()

    def display_note(self, item):
        note = self.note_manager.get_note(item.text())
        if note:
            self.note_text.setPlainText(note.content)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()