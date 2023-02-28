'''
Code projeto visto em vídeos na internet
necessario instalar pip install selenium e  webdriver do Google Chrome https://sites.google.com/a/chromium.org/chromedriver/downloads 

'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Configurando o webdriver do Chrome
driver = webdriver.Chrome('/path/to/chromedriver')

# Abrindo o navegador e acessando o site desejado
driver.get('https://www.youtube.com')

# Buscando pela barra de pesquisa do YouTube
search_box = driver.find_element_by_name('search_query')

# Inserindo o termo de busca e enviando a pesquisa
search_box.send_keys('Nome da música')
search_box.send_keys(Keys.RETURN)

# Esperando o resultado da pesquisa carregar
driver.implicitly_wait(10)

# Encontrando o link do primeiro resultado da pesquisa
link = driver.find_element_by_css_selector('#contents > ytd-video-renderer:nth-child(1) > #dismissible > #thumbnail')

# Navegando para a página do vídeo
link.click()

# Fechando o navegador
driver.quit()
