import random

class Notebook:
    def __init__(self):
        # lista vazia que armazena as notas
        self.notes = []

    def addNote(self, note):
        self.notes.append(note)

    def listNotes(self):
        # uma nota por linha
        for note in self.notes:
            print(note)

    def listNotesFor(self):
        # lista todas as notas na lista usando um loop 
        for i in range(len(self.notes)):
            print(self.notes[i])

    def hasNotes(self):
        # Verifica se há notas na lista e retorna true ou false
        return len(self.notes) > 0

    def compareNote(self, note):
        # Verifica se uma nota específica está na lista e retorna true ou false, exibindo a nota
        return note in self.notes

    def showNoteRandom(self):
        # Mostra uma nota aleatória da lista
        if self.hasNotes():
            print(random.choice(self.notes))
        else:
            # Se não houver notas, exibe uma mensagem informando isso
            print("\nNenhuma nota disponível.\n")

    def showMultiNoteRandom(self, num_notes):
        # Mostra várias notas aleatórias da lista
        if not self.hasNotes():
            # Se não houver notas, exibe uma mensagem informando isso
            print("\nNenhuma nota disponível\n")
            return

        count = 0
        # Usa um loop while para mostrar as notas aleatórias
        while count < num_notes and count < len(self.notes):
            print(random.choice(self.notes))
            count += 1