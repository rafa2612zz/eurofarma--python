import csv
dados_tabela = [
    ["BAIRRO","CIDADE","ESTADO","CEP"],
    ["jardim Belval","barueri","SP","06420320"],
    ["parque santana I","Santana de parnaiba","SP","06325800"],
    ["centro","jandira","SP","05230000"]
]

with open("7.02-cidade.csv","w",encoding="utf-8",newline="") as arquivos_csv:
    escrevendo = csv.writer(arquivos_csv)
    escrevendo.writerows(dados_tabela)