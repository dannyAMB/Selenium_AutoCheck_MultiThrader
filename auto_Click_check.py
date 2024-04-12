from socket import timeout
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
correo = "danny.marmol@iudigital.edu.co"
contrasena = "edotensei1*"
curso = '15653'
url = "https://iudigital.instructure.com/"



driver = webdriver.Chrome()

driver.get(''+url+'courses/'+curso+'/modules')

# Login

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID,"pseudonym_session_unique_id"))).send_keys(correo)


WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID,"pseudonym_session_password"))).send_keys(contrasena)



# Click login

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "Button--login"))).click()  



def do_():

   try:
    for i in range(1000):
     WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH , "(//span[@class='lock-icon btn-unlocked'])[3]"))).click()  
     WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH , "(//span[@class='lock-icon btn-unlocked'])[3]"))).click()  

   except:
     do_()

do_()
 


print("FIN")

driver.quit()