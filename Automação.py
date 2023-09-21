from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Inicializa o navegador (certifique-se de que o ChromeDriver está no seu PATH)
driver = webdriver.Chrome()

# Abre o Google.com.br
driver.get("https://www.google.com.br")

# Localiza o campo de pesquisa e insere uma consulta
search_box = driver.find_element_by_name("Pesquise no Google ou digite um URL")
search_box.send_keys("tradução de churasco")

# Pressiona Enter para realizar a pesquisa
search_box.send_keys(Keys.RETURN)

# Espera alguns segundos (você pode ajustar o tempo)
import time
time.sleep(5)

# Fecha o navegador
driver.quit()
