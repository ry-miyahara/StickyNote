class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.created_at = datetime.now()

class NoteManager:
    def __init__(self):
        self.notes = []

    def add_note(self, title, content):
        new_note = Note(title, content)
        self.notes.append(new_note)

    def remove_note(self, title):
        self.notes = [note for note in self.notes if note.title != title]

    def get_notes(self):
        return self.notes

    def find_note_by_title(self, title):
        for note in self.notes:
            if note.title == title:
                return note
        return None