from tkinter import Tk, Label, Entry, Button, filedialog, messagebox, Frame, Text, END

print("Iniciando...")

# variavel global para armazenar o caminho do arquivo
caminho_arquivo = ""

def log(mensagem):
    caixa_texto.insert(END, mensagem + "\n")
    caixa_texto.see(END) # rola automaticamente

def carregar_arquivo():
    global caminho_arquivo
    caminho_arquivo = filedialog.askopenfilename(
        title="Selecione arquivo:",
        filetypes=[("Arquivos de texto", "*.txt")]
    )
    #label2.config(text=f"✅ Arquivo carregado: {caminho_arquivo}", fg="green")
    #print("arquivo carregado:", caminho_arquivo)
    log(f"✅ Arquivo carregado: {caminho_arquivo}")

def buscar_texto():
    if not caminho_arquivo:
        #label2.config(text="❌ Nenhum arquivo carregado...", fg="red")
        log("❌ Nenhum arquivo carregado...")
        return
    
    texto_busca = entrada.get()

    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()

    if texto_busca in conteudo:
        #label2.config(text=f"✅ O texto '{texto_busca}' foi encontrado no arquivo!", fg="green")
        log(f"✅ O texto '{texto_busca}' foi encontrado no arquivo!")
    else:
        #label2.config(text=f"❌ O texto '{texto_busca}' não foi encontrado no arquivo!", fg="red")
        log(f"❌ O texto '{texto_busca}' não foi encontrado no arquivo!")


root = Tk()
root.title("Editor de Texto")
root.geometry("600x400")

# Frames
frame_dados = Frame(root)
frame_dados.pack(side="left", padx=20, pady=20)

frame_comandos = Frame(root)
frame_comandos.pack(side="right", padx=20, pady=20)


# Frame_esquerda
label = Label(frame_dados, text="Digite o texto a ser buscado:")
label.pack(pady=10)

label2 = Label(frame_dados, text="", font=("Arial", 8), fg="red")
label2.pack(pady=10)

entrada = Entry(frame_dados, width=30)
entrada.pack(pady=5)

label2 = Label(frame_dados, text="Histórico de execução", font=("Arial", 8))
label2.pack(pady=10)

caixa_texto = Text(frame_dados, width=40, height=30)
caixa_texto.pack(pady=5)

# Frame_direita
botao_carregar = Button(frame_comandos, text="Carregar Arquivo", command=carregar_arquivo)
botao_carregar.pack(pady=5)

botao_buscar = Button(frame_comandos, text="Buscar Texto", command=buscar_texto)
botao_buscar.pack(pady=5)

root.mainloop()
