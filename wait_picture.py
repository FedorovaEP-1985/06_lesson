from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация драйвера
driver = webdriver.Chrome()

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
print("Страница загружена")

# Ожидание загрузки всех картинок
WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located(
    (By.CSS_SELECTOR,"#image-container img:nth-child(4)"))
    )

# Поиск всех элементов <img> внутри контейнера
images = driver.find_elements(By.CSS_SELECTOR,"#image-container img")
print(images)

# Получение значения атрибута src у 3-й картинки
third_image = driver.find_element(
    By.CSS_SELECTOR,"#image-container img:nth-child(3)")
src_value = third_image.get_attribute("src")
print("Значение атрибута src у 3-й картинки:", src_value)


driver.quit()
print("Драйвер закрыт")
