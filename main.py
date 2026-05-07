from tkinter import Tk, Label, Entry, Button, filedialog, messagebox, Frame, Text, END
from datetime import datetime
import os
import unicodedata
import random
import re

print("Iniciando...")

# variavel global para armazenar o caminho do arquivo
caminho_arquivo = ""  #var global
novo_conteudo = ""  #var global

def remover_acentos(texto):
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

def log(mensagem):
    caixa_texto.insert(END, mensagem + "\n")
    caixa_texto.see(END) # rola automaticamente

def carregar_arquivo():
    global caminho_arquivo

    caminho_arquivo = filedialog.askopenfilename(
        title="Selecione arquivo:",
        filetypes=[("Arquivos de texto", "*.txt")]
    )
    
    if not caminho_arquivo:
        log("❌ Nenhum arquivo selecionado...")
        return  

    log(f"✅ Arquivo carregado: {caminho_arquivo}")

    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()

    conteudo_sem_acentos = remover_acentos(conteudo)

    quantidade = conteudo_sem_acentos.lower().count("questao")

    log(f"✅ O arquivo contém {quantidade} ocorrências da palavra 'questao'.")

def buscar_texto():
    if not caminho_arquivo:
        #label2.config(text="❌ Nenhum arquivo carregado...", fg="red")
        log("❌ Nenhum arquivo carregado...")
        return
    
    texto_busca = entrada.get().strip()

    texto_busca_sem_acentos = remover_acentos(texto_busca.lower())

    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()

    conteudo_sem_acentos = remover_acentos(conteudo)

    if texto_busca_sem_acentos in conteudo_sem_acentos:
        #label2.config(text=f"✅ O texto '{texto_busca}' foi encontrado no arquivo!", fg="green")
        log(f"✅ O texto '{texto_busca}' foi encontrado no arquivo!")
    else:
        #label2.config(text=f"❌ O texto '{texto_busca}' não foi encontrado no arquivo!", fg="red")
        log(f"❌ O texto '{texto_busca}' não foi encontrado no arquivo!")

def embaralhar_resultado(conteudo):
    
    blocos = re.split(r'(?=questao\s*\d+)', conteudo, flags=re.IGNORECASE)
    
    resultado_final = []

    for bloco in blocos:

        linhas = bloco.split("\n")

        alternativas = []
        outras = []

        for linha in  linhas:
            
            if re.match(r'\s*[a-e]\)', linha):
                alternativas.append(linha)
            else:
                outras.append(linha)
            
        if len(alternativas) == 5:
            
            textos = [alt.split(")", 1)[1].strip() for alt in alternativas]

            random.shuffle(textos)

            alternativas = [
                f"a) {textos[0]}",
                f"b) {textos[1]}",
                f"c) {textos[2]}",
                f"d) {textos[3]}",
                f"e) {textos[4]}"
            ]

            bloco_final = "\n".join(outras + alternativas) + "\n\n"

            resultado_final.append(bloco_final)

        else:
            resultado_final.append(bloco)

    return "\n".join(resultado_final)

def embaralhar_todas_questoes():
    
    global novo_conteudo

    if not caminho_arquivo:
        log("❌ Nenhum arquivo carregado...")
        return
    
    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()

    novo_conteudo = embaralhar_resultado(conteudo)

    log("✅ Questões embaralhadas com sucesso!")

def salvar_novo_arquivo():

    global novo_conteudo


    if not novo_conteudo:
        log("❌ Nenhum conteúdo para salvar. Por favor, embaralhe as questões primeiro.")
        return

    data_hora = datetime.now().strftime("%Y-%m-%d_%H-%M")

    nome_original = os.path.basename(caminho_arquivo)
    nome_sem_extensao = os.path.splitext(nome_original)[0]

    novo_nome = f"{nome_sem_extensao}_novo_{data_hora}.txt"

    pasta = os.path.dirname(caminho_arquivo)

    novo_caminho = os.path.join(pasta, novo_nome)
    
    with open(novo_caminho, "w", encoding="utf-8") as arquivo:
        arquivo.write(novo_conteudo)    

    log("✅ Novo arquivo salvo:")
    log(novo_caminho)

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

botao_embaralhar = Button(frame_comandos, text="Embaralhar Respostas", command=embaralhar_todas_questoes)
botao_embaralhar.pack(pady=5)

botao_salvar = Button(frame_comandos, text="Salvar Novo Arquivo", command=salvar_novo_arquivo)
botao_salvar.pack(pady=5)

root.mainloop()
