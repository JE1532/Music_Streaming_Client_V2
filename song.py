class Song:
    def __init__(self, name, artist, gui_rep):
        self.gui_rep = gui_rep
        self.name = name
        self.artist = artist


    def delete_from_gui(self):
        self.gui_rep[0].deleteLater()
