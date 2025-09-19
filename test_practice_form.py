from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service as EdgeService
import time
import os

def test_practice_form():
    service = EdgeService(r"C:\Users\Lenovo\Desktop\drivers-kessy\msedgedriver.exe")
    driver = webdriver.Edge(service=service)
    driver.maximize_window()
    
    try:
        # 1 - Acessar o site demoqa
        driver.get("https://demoqa.com/")
        time.sleep(2)
        
        # 2 - Escolher a opção "Forms" na página inicial
        driver.find_element(By.XPATH, '//h5[text()="Forms"]').click()
        time.sleep(1)
        
        # 3 - Clicar no submenu "Practice Form"
        driver.find_element(By.XPATH, '//span[text()="Practice Form"]').click()
        time.sleep(2)
        
        # 4 - Preencher o formulário com dados aleatórios
        driver.find_element(By.ID, 'firstName').send_keys("Kessy")
        driver.find_element(By.ID, 'lastName').send_keys("Automacao")
        driver.find_element(By.ID, 'userEmail').send_keys("teste@demo.com")

        # 4.1 - Fechar anúncio se presente
        try:
            close_ads = driver.find_element(By.ID, "close-fixedban")
            close_ads.click()
            time.sleep(1)
        except Exception:
            pass

        # 4.2 - Scroll na página
        driver.execute_script("window.scrollBy(0, 300);")
        time.sleep(1)
        
        # 4.3 Seleciona o gênero 'Female'
        driver.find_element(By.XPATH, '//label[text()="Female"]').click()
        
        driver.find_element(By.ID, 'userNumber').send_keys("1234567890")
        
        # 4.4 Data de nascimento - campo input
        dob = driver.find_element(By.ID, 'dateOfBirthInput')
        dob.click()
        dob.send_keys(Keys.CONTROL + "a")
        dob.send_keys("30 Ago 2000")
        dob.send_keys(Keys.ENTER)
        
        # 4.5 Upload do arquivo .txt
        upload_input = driver.find_element(By.ID, 'uploadPicture')
        file_path = os.path.abspath("file.txt")
        upload_input.send_keys(file_path)
        
        # 5 - Submeter o formulário
        driver.find_element(By.ID, 'submit').click()
        time.sleep(3)
        
        # 6 - Verificar popup
        modal = driver.find_element(By.ID, 'example-modal-sizes-title-lg')
        assert modal.is_displayed()
        print("Popup aberto com título:", modal.text)
        
        # 7 - Fecha o popup
        driver.find_element(By.ID, 'closeLargeModal').click()
        time.sleep(1)

    finally:
        driver.quit()

if __name__ == "__main__":
    test_practice_form()
