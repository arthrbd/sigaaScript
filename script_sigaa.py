#Bibliotecas necessarias para o funcionamento do matriculador
import time
import winsound
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

#Navegador
driver = webdriver.Chrome()

#Acessa o login
driver.get("https://autenticacao.unb.br/sso-server/login?service=https%3A%2F%2Fsig.unb.br%2Fsigaa%2Flogin%2Fcas")

#Preenche e entra
driver.find_element(By.NAME, "username").send_keys("seuLogin")
driver.find_element(By.ID, "password").send_keys("suaSenha")
driver.find_element(By.NAME, "submit").click()
time.sleep(5)

#Acessar hover
menu = driver.find_element(By.CLASS_NAME, "ThemeOfficeMainItem")
acao = ActionChains(driver)
acao.move_to_element(menu).perform()
time.sleep(2)

#Hover 2
ext = driver.find_element(By.XPATH, '//*[@id="cmSubMenuID1"]/table/tbody/tr[14]/td[2]')
acao.move_to_element(ext).perform()
time.sleep(2)

#Entra na matricula
matr = driver.find_element(By.XPATH, '//*[@id="cmSubMenuID3"]/table/tbody/tr[3]/td[2]')
acao.move_to_element(matr).click().perform()
time.sleep(5)

#Animacao de carregamento
for i in range(5): 
    for pontos in ["", ".", "..", "..."]:
        print(f"\rInicializando procura de matéria {pontos:<3}", end="")
        sys.stdout.flush()
        time.sleep(0.3)

#Procura a matéria desejada
driver.find_element(By.XPATH, '//*[@id="form:txtCodigo"]').send_keys("materiaDesejada")
driver.find_element(By.XPATH, '//*[@id="form:buscar"]').click()
time.sleep(3)

#Logica para busca
intervalo = 3

while True:
    try:
        driver.find_element(By.XPATH, '//*[@id="form:buscar"]').click()
        time.sleep(2)

        if driver.find_elements(By.XPATH, '//*[@id="lista-turmas-extra"]/caption'):
            vagaDisponivel = 1
        else:
            vagaDisponivel = 0

        tempo = time.strftime("%H:%M:%S")
        print(f'[{tempo}] Vagas disponíveis: {vagaDisponivel}')

        if vagaDisponivel > 0:
            print('Vaga encontrada! Corre!')
            winsound.Beep(1000, 10000)  
            break 

    except Exception as e:
        print(f'Erro ao buscar vagas: {e}')

    time.sleep(intervalo)
