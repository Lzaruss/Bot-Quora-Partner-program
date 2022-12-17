from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver import ActionChains
import time

def request_question():
    filename = 'preguntas.txt'
    f = open(filename, 'r+', encoding='utf-8')
    # Leemos todas las líneas del archivo
    lines = f.readlines()
    first_line =  lines[0]
    # Borramos la primera línea
    lines.pop(0)
    f = open(filename, "w", encoding='utf-8')
    f.writelines(lines)
    f.close
    return first_line

driver = webdriver.Chrome()

url = "https://es.quora.com/"
driver.get(url)

#Tiempo de espera para que puedas iniciar sesion
time.sleep(35)
i = 0
while i != 100:
    try:
        clickable = driver.find_element(By.XPATH, "//*[@id='mainContent']/div/div/div[1]/div/div/div[1]/div/div[2]")
        ActionChains(driver)\
                .click(clickable)\
                .perform()
        time.sleep(1)
        textArea = driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/div/div/div/div/div[2]/div/div/div[1]/div/div/textarea")
        textArea.send_keys(request_question())
        time.sleep(2)
        #TODO poner la opcion para cuando ya se haya hecho esa pregunta
        #Le damos al boton de preguntar 
        driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div[2]/button[2]').click()
        time.sleep(4)
        #TODO en un futuro añadir la opcion de presionar los demas temas
        driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/button').click()
        time.sleep(3)
        #Pulsamos el boton de continuar sin editar los temas
        driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div/div[3]/div[2]/button').click()
        time.sleep(4)
        
        #Solicitar respuestas
        for x in range(1, 22):
            driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[3]/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/div[3]/div[2]/div/div/div/div/div[1]/div[2]/div['+str(x)+']/div/div/div/div[3]/div/div/div').click()
            time.sleep(0.2)

        time.sleep(1)

        #Enviamos la pregunta
        driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[3]/div/div/div/div[2]/div/div/div[2]/div[2]/div/div[2]/button').click()
        time.sleep(1.5)
    except:
        pass
    time.sleep(1.5)
    driver.get("https://es.quora.com/")
    i +=1



time.sleep(30)

driver.close()