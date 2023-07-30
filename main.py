

import pyautogui as py 
import time
py.PAUSE = 0.3

# abrir o navegador no chrome
py.press("win")
py.write("chrome")
py.press("enter")

time.sleep(5)
py.click(x=646, y=392)

# Entrar no sistema da empresa
   # https://dlp.hashtagtreinamentos.com/python/intensivao/login
#Entrar no link
py.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
py.press("enter")

#pyautogui.write -> escrever um texto
#pyautogui.press -> apertar uma tecla
#pyautogui.click -> clicar em algum lugar da tela

#Fazendo o login
# Selecionar campo do E-mail
time.sleep(5)
py.click(x=602, y=369)
# Escrever o seu e-mail
py.write("ricnewline@gmail.com")
# Escrever no campo Senha
py.press("tab")
py.write("123456")
# Clicar em logar
py.click(x=643, y=518)
# Importar a base de produtos para 
import pandas as pd 
 
tabela = pd.read_csv("produtos.csv")
#print(tabela)

# Cadastrar um produto e reptir o processo de cadastro até o fim.
for linha in tabela.index:
# clicar no campo codigo do produtos
   py.click(x=506, y=238)
   # Pegar da tabela o valor do campo que queremos preencher
   py.write(str(tabela.loc[linha, "codigo"]))
   # Preencher o campo 
   py.press("tab")
   py.write(str(tabela.loc[linha, "marca"]))
   py.press("tab")
   py.write(str(tabela.loc[linha, "tipo"]))
   py.press("tab")
   py.write(str(tabela.loc[linha, "categoria"]))
   py.press("tab")
   py.write(str(tabela.loc[linha, "preco_unitario"]))
   py.press("tab")
   py.write(str(tabela.loc[linha, "custo"]))
   py.press("tab")
   obs = tabela.loc[linha, "obs"]
   # Estrutura condicional para evitar erro quando a linha da coluna "Obs" estiver vazio:
   if not pd.isna(obs):
      py.write(str(tabela.loc[linha, "obs"]))
   py.press("tab")
   py.press("enter")
   # Para dar um scroll para selecionar o inicio do produto
   py.scroll(500)

 

