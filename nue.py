from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException  # Importar la excepción

def encontrarProducto(p):
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Ejecutar en modo sin interfaz gráfica

    service = Service("C:/Users/canle/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")  # Especifica el path de tu WebDriver
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get(f'https://www.guatemaladigital.com/Producto/{p}')

    try:
        # Esperar a que el elemento esté presente
        nombreProducto = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "h3.product-title.font-weight-bold.text-justify.px-0"))
        )
        find = nombreProducto.text
        return find
    except TimeoutException:
        error = print(f"Producto con ID {p} no encontrado.")
        return error
    finally:
        driver.quit()

# Pruebas con productos
producto = encontrarProducto(17850375)
producto2 = encontrarProducto(17421926)
print(producto)
print(producto2)
