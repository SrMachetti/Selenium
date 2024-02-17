from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By



def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=800,600', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,

    })
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()), options=chrome_options)

    return driver


driver = iniciar_driver()
driver.get('https://cursoautomacao.netlify.app/')

botao = driver.find_element(By.ID, 'buttonalerta')
botoes = driver.find_elements(By.ID, 'buttonalerta')

if botao is not None:
    print('botão foi encontrado')
    #print(botao)

if botoes is not None:
    print('Botões foram encontrados')
    #print(botoes)

campo_nome = driver.find_element(By.NAME, 'seu-nome')
radio_buttons = driver.find_elements(By.NAME, 'exampleRadios')

if campo_nome is not None:
    print('seu-nome encontrado')
if radio_buttons is not None:
    print('radio_buttons encontrados')

logo = driver.find_element(By.CLASS_NAME, 'navbar-brand')
link_menu = driver.find_elements(By.CLASS_NAME, 'nav-link')

if logo is not None:
    print('logo encontrado')
if link_menu is not None:
    print('Link_menu encontrado')

link_home = driver.find_element(By.LINK_TEXT, 'Home')
link_desafio = driver.find_elements(By.PARTIAL_LINK_TEXT, 'Des')

if link_home:
    print('encontrou link Home')
if link_desafio:
    print('link desafio encontrado')

titulo = driver.find_element(By.XPATH, '//*[text()="ZONA DE TESTES"]')

if titulo:
    print('Título encontrado')
    print(titulo.text)

titulo_do_site = driver.find_element(By.TAG_NAME, 'h1')
elementos_h4 = driver.find_elements(By.TAG_NAME, 'h4')

if titulo_do_site:
    print('Encontrou Título h1')

if elementos_h4:
    print('Encontrou h4')


input('digite algo para fechar... ')