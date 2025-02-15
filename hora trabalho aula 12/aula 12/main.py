from notebook import Notebook

def main():
    notebook = Notebook()

    #Adicionar uma nota
    note = input("\nDigite uma nota para adicionar ao bloco: ")
    notebook.addNote(note)
    print("\nNota adicionada com sucesso!")

    #Listar as notas
    print("\nNotas no bloco:")
    notebook.listNotesFor()

    #Verificar se há notas
    if notebook.hasNotes():
        print("\nHá notas no bloco.")
    else:
        print("\nNão há notas no bloco.")

    # Mostrar uma nota aleatória
    print("\nMostrando uma nota aleatória:")
    notebook.showNoteRandom()

    #Mostrar várias notas aleatórias
    num_notes = int(input("\nQuantas notas aleatórias deseja ver? "))
    print(f"\nMostrando {num_notes} notas aleatórias:")
    notebook.showMultiNoteRandom(num_notes)

if __name__ == "__main__":
    main()