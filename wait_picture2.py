from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

url = (
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
)
driver.get(url)
third_image = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
                (By.CSS_SELECTOR, "#image-container img:nth-child(3)"))
)
print("Третья картинка найдена")
src_value = third_image.get_attribute("src")
print("Значение атрибута src у 3-й картинки:", src_value)

driver.quit()
