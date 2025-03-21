from selenium import webdriver  # Importación del módulo webdriver de Selenium para controlar el navegador.
from selenium.webdriver.chrome.service import Service  # Importación del módulo Service para configurar el servicio de ChromeDriver.
from selenium.webdriver.common.by import By  # Importación de By para ubicar elementos en la página web mediante sus selectores.
from selenium.webdriver.chrome.options import Options  # Importación de Options para configurar las opciones del navegador (por ejemplo, ejecutar en modo headless).
from selenium.webdriver.support.ui import WebDriverWait  # Importación de WebDriverWait para esperar explícitamente hasta que un elemento esté presente en la página.
from selenium.webdriver.support import expected_conditions as EC  # Importación de expected_conditions (EC) para usar condiciones predefinidas como la presencia de un elemento.
from selenium.common.exceptions import TimeoutException  # Importar la excepción

def encontrarProducto(p):
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Ejecutar en modo sin interfaz gráfica

    service = Service("C:/Users/canle/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")  # Especifica el path de tu WebDriver
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get(f'https://www.guatemaladigital.com/Producto/{p}')

    try:
        # Esperar a que el nombre del producto esté presente
        nombreProducto = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "h3.product-title.font-weight-bold.text-justify.px-0"))
        )
        nombre = nombreProducto.text

        # Buscar la descripción del producto
        try:
            descripcionProducto = driver.find_element(By.CSS_SELECTOR, "div.product-description")
            descripcion = descripcionProducto.text.strip() if descripcionProducto.text else "Descripción no disponible"
        except:
            descripcion = "Descripción no encontrada"

        # Buscar el precio del producto
        try:
            precioProducto = driver.find_element(By.CSS_SELECTOR, "span.naranja-text.span-text-producto.font-weight-bold")
            precio = precioProducto.text.strip() if precioProducto.text else "Precio no disponible"
        except:
            precio = "Precio no encontrado"

        return {"nombre": nombre, "descripcion": descripcion, "precio": precio}
    except TimeoutException:
        return {"error": f"Producto con ID {p} no encontrado."}
    finally:
        driver.quit()

producto = encontrarProducto(17850375)
producto2 = encontrarProducto(17421926)

def imprimirProducto(id, producto):
    if "error" in producto:
        print(producto["error"])
    else:
        print(f"ID: {id}")
        print(f"Nombre: {producto['nombre']}")
        print(f"Descripción: {producto['descripcion']}")
        print(f"Precio: {producto['precio']}")
        print()

imprimirProducto(17850375, producto)
imprimirProducto(17421926, producto2)
