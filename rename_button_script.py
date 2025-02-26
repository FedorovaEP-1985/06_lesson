from selenium import webdriver
from selenium.webdriver.common.by import By

# Инициализация драйвера
driver = webdriver.Chrome()

try:
    driver.get("http://uitestingplayground.com/textinput")

    # Ввод текста в поле ввода
    input_field = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
    input_field.send_keys("SkyPro")
    print("Текст введен")

    # Нажатие на синюю кнопку
    blue_button = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
    blue_button.click()
    print("Кнопка нажата")

    # Получение текста кнопки
    button_text = blue_button.text
    print(button_text)

finally:
    driver.quit()
    print("Драйвер закрыт")
