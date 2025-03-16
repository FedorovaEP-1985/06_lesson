from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация драйвера
driver = webdriver.Chrome()

try:
    driver.get("http://uitestingplayground.com/ajax")
    print("Страница загружена")

    # Нажатие на синюю кнопку
    ajax_button = driver.find_element(By.CSS_SELECTOR, "#ajaxButton")
    ajax_button.click()
    print("Кнопка нажата")

    # Ожидание появления зеленой плашки
    # и получение текста
    green_banner = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".bg-success"))
    )
    print("Зеленая плашка найдена")
    text = green_banner.text
    print(text)  # Вывод текста в консоль

finally:
    driver.quit()
    print("Драйвер закрыт")
