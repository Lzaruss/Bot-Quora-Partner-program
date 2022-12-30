from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver import ActionChains
import time
import json
import argparse

parser = argparse.ArgumentParser(add_help=False, description="Write -n or --num to set the number of questions you want the script to ask")
parser.add_argument('-n', '--num', type=int, required=False, help="Number of questions you want for the script(if you dont say any number, by defect will be 10)")
parser.add_argument('-L', '--login', action='store_true', required=False, help="argument to log in manually (to bypass captha manually) ")
parser.add_argument('-h', '--help', action='help', help="If Login returns Captcha error put -L to login manually, -n for number of questions you want")
args = parser.parse_args()

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

def iniciar_sesion():
    credentials = cred_return()
    driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(credentials["email"])

    time.sleep(0.5)
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(credentials["password"])
    if args.login:
        time.sleep(20)
    else:
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div/div/div/div[2]/div[2]/div[4]/button').click()

def cred_return():
    cred_file = open("./credentials.json", "r")
    credentials = cred_file.read()
    credentials = json.loads(credentials)
    cred_file.close
    return credentials

#Unable LOGS
options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options, executable_path=r'C:\WebDrivers\chromedriver.exe')
driver.get("https://es.quora.com/")

iniciar_sesion()
preventiveNegativeQuestions = lambda num: 10 if num <= 0 else num
#Por defecto pondremos 10 preguntas
try:
    numPreguntas = args.num
    num = preventiveNegativeQuestions(numPreguntas)
except:
    num = 10

print(f"Num of questions: {num}")
while num != 0:
    try:
        clickable = driver.find_element(By.XPATH, "//*[@id='mainContent']/div/div/div[1]/div/div/div[1]/div/div[2]")
        ActionChains(driver)\
                .click(clickable)\
                .perform()
        time.sleep(1.2)

        driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/div/div/div/div/div[2]/div/div/div[1]/div/div/textarea").send_keys(request_question())
        time.sleep(2.2)
        #Le damos al boton de preguntar 
        driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div[2]/button[2]').click()
        time.sleep(3.2)
        driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/button').click()
        time.sleep(2.2)
        #Pulsamos el boton de continuar sin editar los temas
        driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div/div[3]/div[2]/button').click()
        time.sleep(4)
        
        #Solicitar respuestas
        for x in range(1, 22):
            driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[3]/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/div[3]/div[2]/div/div/div/div/div[1]/div[2]/div['+str(x)+']/div/div/div/div[3]/div/div/div').click()
            time.sleep(0.15)

        time.sleep(1)

        #Enviamos la pregunta
        driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[3]/div/div/div/div[2]/div/div/div[2]/div[2]/div/div[2]/button').click()
    except:
        pass
    time.sleep(1.5)
    driver.get("https://es.quora.com/")
    num -=1
    print(f"\rQuestions left: {num} ", end="")

time.sleep(5)
driver.close()
exit()
