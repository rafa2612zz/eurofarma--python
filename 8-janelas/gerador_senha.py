#importando a biblioteca e nomeando de tk
import tkinter as tk 
import random 
import string

ALTURA = "600"
LARGURA = "450"


# 7.0 Funçoes Do Sistema 

def gerar_senha():
    try:
        tamanho = int (entry_tamanho_da_senha.get())
        # Verificando se a quantidade de caracteres definida é menor do que 4
        if tamanho < 4:
            lbl_resultado.config(
                text="Erro: Minimo de 4 caracteres",
                fg="#FF0000"
            )
            return
        caracteres = ""
        if war_maiusculas.get():
                caracteres += string.ascii_uppercase
        if war_minusculas.get():
                caracteres += string.ascii_lowercase
        if war_numeros.get():
                caracteres += string.digits
        if war_simbolos.get():
                caracteres += string.punctuation

        if not caracteres:
              lbl_resultado.config(
                    text = "Erro selecione ao menos uma opção!",
                    fg= "#FF0000"
              )
              return

        senha = "".join(random.choice(caracteres) for i in range(tamanho))

        lbl_resultado.config(
            text=f"Senha: {senha}",
            fg= "#FFFFFF"
        )
        

    except ValueError :
          lbl_resultado.config(
               text="Erro: Digite Um Numero Valido!",
                fg="#FF0000"
                )

def copiar_senha():
    texto_resultado = lbl_resultado.cget("text")

    if "Senha: " in texto_resultado:
          senha = texto_resultado.replace("senha: ", "")
          janela.clipboard_clear()
          janela.clipboard_append(senha)
          lbl_resultado.config(
            text="Senha copiada ",
            fg="#FFFFFF"
     
            )

    else:
          lbl_STSCP.config(
                text= "sem senha para copiar",
                fg= "#FFD900"
          )

#===================================
#1. Configuração da Janela Principal
#===================================


janela = tk.Tk()
janela.title("BALEIA SEGURA - GERADOR DE SENHAS")
janela.geometry(f"{LARGURA}x{ALTURA}")
janela.config(bg="#0004FF")

# 2. Titulo principal do aplicativo
titulo = tk.Label(
    text="BALEIA SEGURA 🐋",
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

# 6.0 criar botao gerador de senha 
btn_gerar = tk.Button(
    janela,
    text="CONFIRMAR SUA SENHA ",
    command=gerar_senha,
    bg="#0408FF",
    fg="#FFFFFF",
    padx=10,
    pady=5
)

btn_gerar.pack(padx=10, pady=5)

# label que apresenta o resultado no programa
lbl_resultado = tk.Label(
      janela,
      text="A SENHA APARECERAR AQUI",
      font=("segoe UI", 11,"bold"),
      bg="#0408FF",
      fg="#FFFFFF"
)
lbl_resultado.pack(pady=5)


btn_copiar = tk.Button(
      janela,
      text="COPIAR",
      font=(" segue UI", 7, "bold"),
      command=copiar_senha,
      bg="#0408FF",
      fg="#FFFFFF",
      padx=5,
      pady=2
      
)

btn_copiar.pack(padx=10, pady=5)


lbl_STSCP = tk.Label(
      bg="#0408FF",
      fg="#FFFFFF"
)

lbl_STSCP.pack(pady=5)


janela.mainloop()