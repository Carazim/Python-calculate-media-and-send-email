import pyautogui
import pyperclip
import webbrowser
import time
import yfinance

ticker = input("Digite o código da ação desejada: ")

dados = yfinance.Ticker(ticker).history(start="2020-01-01", end="2020-12-31")
fechamento = dados.Close

maxima = round(fechamento.max(), 2)
minima = round(fechamento.min(), 2)
valor_medio = round(fechamento.mean(), 2)

destinatario = "mateusgm2013@gmail.com"
assunto = "Análises do Projeto 2020"

mensagem = f"""
Prezado gestor,

Seguem as análises solicitadas da ação {ticker}:

Cotação máxima: R${maxima}
Cotação mínima: R${minima}
Valor médio: R${valor_medio}

Qualquer duvida estou a disposição

Atte.
"""

# abrir o navegador e ir para o gmail
webbrowser.open("www.gmail.com")
time.sleep(6)

# configurando uma pausa de 4 segundos
pyautogui.PAUSE = 3

# clicar no botão escrever
pyautogui.click(x=163, y=197)

# digitar o email do destinatário e teclar TAB
pyperclip.copy(destinatario)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

# digitar o assunto do email
pyperclip.copy(assunto)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

# digitar a mensagem 
pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl", "v")

# clicar no botão enviar
pyautogui.click(x=1307, y=995)

# fechar o gmail
pyautogui.click("ctrl", "w")

print("Email mandado com sucesso")