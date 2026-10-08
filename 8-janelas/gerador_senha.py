#importando a biblioteca e nomeando de tk
import tkinter as tk 
ALTURA = "600"
LARGURA = "450"

def acao_clique():
    print("o botao foi clicado!")

#===================================
#1. Configuração da Janela Principal
#===================================
janela = tk.Tk()
janela.title("BALEIA SEGURA - GERADOR DE SENHAS")
janela.geometry(f"{LARGURA}x{ALTURA}")
janela.config(bg="#0004FF")

# 2. Titulo principal do aplicativo
titulo = tk.Label(
    text="BALEIA SEGURA 🐳",
    font=("Arial",16,"bold"),
    bg="#0004FF",
    fg="#f1f3f3"

)
titulo.pack(pady=20)

# 3. Label tamanho da senha
lbl_tamanho_senha = tk.Label(
    text="TAMANHO DE SUA SENHA",
    font=("segoe UI", 11),
    bg="#0408FF",
    fg="#FFFFFF"

)

lbl_tamanho_senha.pack(pady=10)

# ENTRADA TAMAMHO DA SENHA
entry_tamanho_da_senha = tk.Entry(
    janela,
    font=("comic sans ms",12),
    width=10,
    justify="center"

)
entry_tamanho_da_senha.pack(pady=5)

# 5.Criando as variaveis de controle true of false
war_maiusculas = tk.BooleanVar(value=True)
war_minusculas = tk.BooleanVar(value=True)
war_numeros = tk.BooleanVar(value=False)
war_simbolos = tk.BooleanVar(value=False)

# 5. Criando as caixinhas de seleção
chk_maiuscula = tk.Checkbutton(
    janela,
    text="Maiuscula (A-Z)",
    variable= war_maiusculas,
    bg="#0004FF",
    fg="#FFFFFF",
    selectcolor="#0004FF",
    activebackground="#FFFFFF",
    activeforeground="#0004FF"

)
chk_maiuscula.pack(anchor="w", padx=60, pady=2)

chk_Minuscula = tk.Checkbutton(
    janela,
    text="Minuscula (a-z)",
    variable= war_minusculas,
    bg="#0004FF",
    fg="#FFFFFF",
    selectcolor="#0004FF",
    activebackground="#FFFFFF",
    activeforeground="#0004FF"
)
chk_Minuscula.pack(anchor="w", padx=60, pady=2)


chk_Numero = tk.Checkbutton(
    janela,
    text="Numero (0-9)",
    variable= war_numeros,
    bg="#0004FF",
    fg="#FFFFFF",
    selectcolor="#0004FF",
    activebackground="#FFFFFF",
    activeforeground="#0004FF"
)
chk_Numero.pack(anchor="w", padx=60, pady=2)

chk_simbolo = tk.Checkbutton(
    janela,
    text="simbolo (@-#)",
    variable= war_simbolos,
    bg="#0004FF",
    fg="#FFFFFF",
    selectcolor="#0004FF",
    activebackground="#FFFFFF",
    activeforeground="#0004FF"
)
chk_simbolo.pack(anchor="w", padx=60, pady=2)






janela.mainloop()