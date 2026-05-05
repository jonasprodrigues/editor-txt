from tkinter import Tk, Label, Entry, Button, filedialog, messagebox

print("Iniciando...")

def carregar_arquivo():
    print("carregar arquivo...")

def buscar_texto():
    print("buscar texto...")

root = Tk()
root.title("Editor de Texto")
root.geometry("400x200")

label = Label(root, text="Digite o texto a ser buscado:")
label.pack(pady=10)

entrada = Entry(root, width=30)
entrada.pack(pady=5)

botao_carregar = Button(root, text="Carregar Arquivo", command=carregar_arquivo)
botao_carregar.pack(pady=5)

botao_buscar = Button(root, text="Buscar Texto", command=buscar_texto)
botao_buscar.pack(pady=5)

root.mainloop()
