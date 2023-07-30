# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa
   # https://dlp.hashtagtreinamentos.com/python/intensivao/login
import time
import pyautogui
pyautogui.PAUSE = 0.3

# Entar no navegador do google chrome

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(5)
pyautogui.click(x=646, y=392)

#Entrar no link
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

#pyautogui.write -> escrever um texto
#pyautogui.press -> apertar uma tecla
#pyautogui.click -> clicar em algum lugar da tela

# Passo 2: Fazer o login
# Selecionar campo do E-mail
time.sleep(5)
pyautogui.click(x=602, y=369)
# Escrever o seu e-mail
pyautogui.write("ricnewline@gmail.com")
# Escrever no campo Senha
pyautogui.press("tab")
pyautogui.write("123456")
# Clicar em logar
pyautogui.click(x=643, y=518)
# Passo 3: Importar a base de produtos para 
import pandas as pd 
 
tabela = pd.read_csv("produtos.csv")
#print(tabela)

# Passo 4: Cadastrar um produto
# Passo 5: Reptir o processo de cadastro até o fim.
for linha in tabela.index:
# clicar no campo codigo do produtos
   pyautogui.click(x=506, y=238)
   # Pegar da tabela o valor do campo que queremos preencher
   pyautogui.write(str(tabela.loc[linha, "codigo"]))
   # Preencher o campo 
   pyautogui.press("tab")
   pyautogui.write(str(tabela.loc[linha, "marca"]))
   pyautogui.press("tab")
   pyautogui.write(str(tabela.loc[linha, "tipo"]))
   pyautogui.press("tab")
   pyautogui.write(str(tabela.loc[linha, "categoria"]))
   pyautogui.press("tab")
   pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
   pyautogui.press("tab")
   pyautogui.write(str(tabela.loc[linha, "custo"]))
   pyautogui.press("tab")
   obs = tabela.loc[linha, "obs"]
   if not pd.isna(obs):
      pyautogui.write(str(tabela.loc[linha, "obs"]))
   pyautogui.press("tab")
   pyautogui.press("enter")
   # Para dar um scroll para selecionar o inicio do produto
   pyautogui.scroll(500)
