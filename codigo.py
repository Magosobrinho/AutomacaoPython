# Escrever passo a passo da tarefa que você quer executar 
# pip install pyautogui
# pip install pandas

# 1: Entrar no sistema da empresa no link abaixo>
# https://dlp.hashtagtreinamentos.com/python/intensivao/login
import pyautogui
import time
import pandas

#pyautogui.write -> escrever um texto 
#pyautogui.click -> clicar com mouse senhasenha

#pyautogui.press -> pressionar uma tecla
#pyautogui.hotkey -> apertar atalhos do teclado (Ctrl, c)

pyautogui.PAUSE = 0.8
#abrir o navegador
#apertar a tecla windowns 
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.click(x=778, y=583)
time.sleep(3)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# 2: Fazer login (no link pode colocar qualquer e-mail e qualquer senha )

#quero dar pause de 3 segundos crome

time.sleep(3)
pyautogui.click(x=648, y=557)
time.sleep(2)
pyautogui.write("pythonforpython@gmail.com")
pyautogui.press("tab")
pyautogui.write("senhasenha")
pyautogui.press("enter")


# 3: Importar base de dados
# pip install pandas
import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

# 4: Cadastrar produto 
time.sleep(2)
pyautogui.click(x=855, y=429)

linha = 0

#texto = string = str()

#código
codigo = tabela.loc[linha,"codigo"]
pyautogui.write(str(codigo))
pyautogui.press("tab")

#marca
marca = tabela.loc[linha, "marca"]
pyautogui.write(str(marca))
pyautogui.press("tab")

#tipo
tipo = tabela.loc[linha, "tipo"]
pyautogui.write(str(tipo))
pyautogui.press("tab")

#categoria
categoria = tabela.loc[linha, "categoria"]
pyautogui.write(str(categoria))
pyautogui.press("tab")

#preco unitario
preco_unitario = tabela.loc[linha, "preco_unitario"]
pyautogui.write(str(preco_unitario))
pyautogui.press("tab")

#custo
custo = tabela.loc[linha, "custo"]
pyautogui.write(str(custo))
pyautogui.press("tab")

#obs
obs = tabela.loc[linha, "obs"]
pyautogui.write(str(obs))
pyautogui.press("tab")

#clicar no botao enviar 
pyautogui.press("enter")


# 5: Repetir o processo de cadastro até acabar os produtos 



