from tkinter import Tk, Label, Entry, Button, filedialog, messagebox

print("Iniciando...")

# variavel global para armazenar o caminho do arquivo
caminho_arquivo = ""

def carregar_arquivo():
    global caminho_arquivo
    caminho_arquivo = filedialog.askopenfilename(
        title="Selecione arquivo:",
        filetypes=[("Arquivos de texto", "*.txt")]
    )
    label2.config(text=f"✅ Arquivo carregado: {caminho_arquivo}", fg="green")
    #print("arquivo carregado:", caminho_arquivo)


def buscar_texto():
    if not caminho_arquivo:
        label2.config(text="❌ Nenhum arquivo carregado...", fg="red")
        return
    
    texto_busca = entrada.get()

    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()

    if texto_busca in conteudo:
        label2.config(text=f"✅ O texto '{texto_busca}' foi encontrado no arquivo!", fg="green")
    else:
        label2.config(text=f"❌ O texto '{texto_busca}' não foi encontrado no arquivo!", fg="red")


root = Tk()
root.title("Editor de Texto")
root.geometry("400x200")

label = Label(root, text="Digite o texto a ser buscado:")
label.pack(pady=10)

label2 = Label(root, text="", font=("Arial", 8), fg="red")
label2.pack(pady=10)

entrada = Entry(root, width=30)
entrada.pack(pady=5)

botao_carregar = Button(root, text="Carregar Arquivo", command=carregar_arquivo)
botao_carregar.pack(pady=5)

botao_buscar = Button(root, text="Buscar Texto", command=buscar_texto)
botao_buscar.pack(pady=5)

root.mainloop()
