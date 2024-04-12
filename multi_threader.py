import time
from selenium import webdriver 
from threading import Thread, Barrier
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

correo = "danny.marmol@iudigital.edu.co"
contrasena = "edotensei1*"

enlace = "https://iudigital.instructure.com/"


def drive(curso):
	driver = webdriver.Chrome()
	driver.get(''+enlace+'courses/'+curso+'/modules')
	return driver
	
	
def login(driver):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID,"pseudonym_session_unique_id"))).send_keys(correo)

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID,"pseudonym_session_password"))).send_keys(contrasena)

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "Button--login"))).click() 


def clic_check(driver):  
    try:
      for i in range(1000):
       WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH , "(//span[@class='lock-icon btn-unlocked'])[3]"))).click()  
       WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH , "(//span[@class='lock-icon btn-unlocked'])[3]"))).click()  

    except:
       clic_check(driver)

	#click check

def func(threads):
    driver =  drive("15753")
    login(driver) 
    clic_check(driver)

    threads.wait()
"""
def func2(threads):
    driver =  drive("15869")
    login(driver) 	
    clic_check(driver)


    threads.wait()

def func3(threads):
    driver =  drive("15840")
    login(driver) 	
    clic_check(driver)


    threads.wait()
    
def func4(threads):
    driver =  drive("15841")
    login(driver) 	
    clic_check(driver)


    threads.wait()
    
def func5(threads):
    driver =  drive("15773")
    login(driver) 	
    clic_check(driver)


    threads.wait()
    
def func6(threads):
    driver =  drive("15774")
    login(driver) 	
    clic_check(driver)


    threads.wait()"""
    
numero_multitareas = 1

barrier = Barrier(numero_multitareas)

threads = []

def start_thread(i):
    i.start()
    threads.append(i)
    
""" for _ in range(numero_multitareas):
	i = Thread(target=func, args=(barrier,))
	start_thread(i)

	i = Thread(target=func2, args=(barrier,))
	start_thread(i)
    """


i = Thread(target=func, args=(barrier,))
start_thread(i)
"""
i = Thread(target=func2, args=(barrier,))
start_thread(i)
     
i = Thread(target=func3, args=(barrier,))
start_thread(i)

i = Thread(target=func4, args=(barrier,))
start_thread(i)

i = Thread(target=func5, args=(barrier,))
start_thread(i)


i = Thread(target=func6, args=(barrier,))
start_thread(i)"""

for i in threads:
	i.join()