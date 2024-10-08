# Escrever passo a passo da tarefa que você quer executar 
# pip install pyautogui
# pip install pandas

# 1: Entrar no sistema da empresa no link abaixo>
# https://dlp.hashtagtreinamentos.com/python/intensivao/login
import pyautogui
import time

#pyautogui.write -> escrever um texto 
#pyautogui.click -> clicar com mouse senhasenha

#pyautogui.press -> pressionar uma tecla
#pyautogui.hotkey -> apertar atalhos do teclado (Ctrl, c)

pyautogui.PAUSE = 0.8
#abrir o navegador
#apertar a tecla windowns 
pyautogui.press("win")
pyautogui.write("crome")
pyautogui.press("enter")
pyautogui.click(x=778, y=583)
time.sleep(3)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# 2: Fazer login (no link pode colocar qualquer e-mail e qualquer senha )

#quero dar pause de 3 segundos crome

time.sleep(3)
pyautogui.click(x=213, y=524)
time.sleep(3)
pyautogui.write("pythonforpython@gmail.com")
time.sleep(3)
pyautogui.click(x=516, y=626)
pyautogui.write("senhasenha")
pyautogui.press("enter")


# 3: Importar base de dados
# 4: Cadastrar produto 
# 5: Repetir o processo de cadastro até acabar os produtos 



