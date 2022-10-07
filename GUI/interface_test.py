from appJar import gui

def set_interface():
   pass

app = gui("Conversor", useTtk=True)
app.setTtkTheme('alt')
app.setSize(500, 200)

   # Add the interactive components
app.addLabel("Espaço um")
app.addFileEntry("Insira arquivo")

app.addLabel("Espaço dois")
app.addDirectoryEntry("Insira diretorio")

app.addLabel("Espaço 3")
app.addEntry("Insira arquivo de saída")

app.addButtons(["Process", "Quit"], funcs=set_interface)
app.go()