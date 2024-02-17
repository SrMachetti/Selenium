from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep
import random


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

def digitar_naturalmente(texto, elemento):
    multiplicador = 2
    for letra in texto:
        elemento.send_keys(letra)
        if letra == ' ':
            sleep(random.randint(8, 13)/(50*multiplicador))
        else:
            sleep(random.randint(1, 5)/(120*multiplicador))


driver.get('https://cursoautomacao.netlify.app/desafios.html')

botao1 = driver.find_element(By.ID, 'btn1')
botao2 = driver.find_element(By.CLASS_NAME, 'btn2.btn.btn-dark')
botao3 = driver.find_element(By.CLASS_NAME, 'btn2.btn.btn-warning')


if botao1.is_enabled():
    print('Botão 1 habilitado')
else:
    print('Botão 1 desabilitado')

if botao2.is_enabled():
    print('Botão 2 habilitado')
else:
    print('Botão 2 desabilitado')

if botao3.is_enabled():
    print('Botão 3 habilitado')
else:
    print('Botão 3 desabilitado')

print('Desafio scroll')
# Rolar até o fim da página
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(1)
# Rolar até o topo da página
driver.execute_script("window.scrollTo(0, document.body.scrollTop)")
sleep(1)

#input('')

print('Desafio 2')
campo_nome = driver.find_element(By.ID, 'dadosusuario')
campo_nome.location_once_scrolled_into_view
sleep(1)
#campo_nome.send_keys('Sérgio')
digitar_naturalmente('Sérgio Marchetti',campo_nome)
sleep(1)

btn_nome = driver.find_element(By.ID, 'desafio2')
btn_nome.location_once_scrolled_into_view
sleep(1)
btn_nome.click()
sleep(1)

Campo_escondido = driver.find_element(By.ID, 'escondido')
Campo_escondido.location_once_scrolled_into_view
sleep(1)
#Campo_escondido.send_keys('Sérgio Marchetti')
digitar_naturalmente('Sérgio Marchetti',Campo_escondido)
sleep(1)

btn_validacao = driver.find_element(By.ID, 'validarDesafio2')
btn_validacao.click()

desafio3 = driver.find_element(By.CLASS_NAME, 'jumbotron.desafios3')
desafio3.location_once_scrolled_into_view
sleep(.5)

chk_conversivel = driver.find_element(By.ID, 'conversivelcheckbox')
chk_offRoad = driver.find_element(By.ID,'offroadcheckbox')
chk_conversivel.click()
chk_offRoad.click()
sleep(.5)

#desafio 4
texto = """Aqui recomendo que você sempre tenha essa história pronta para contar de uma forma que saliente o seu interesse por a área. Isso porque caso você realmente esteja interessado na vaga, desta maneira você irá mostrar a quem estiver te analisando que você tem uma grande probabilidade de ser um profissional mais engajado com as tarefas da empresa. Capriche nessa história.Muitos aqui iram dizer coisas como: porque vocês são uma ótima empresa, porque todos falam bem de você. Mas alerto: seja autêntico na sua resposta  as empresas querem aqui saber se você pesquisou sobre a empresa e como o seu skillset (seu conhecimento) pode agregar para a empresa, então use essa oportunidade para falar como a EMPRESA vai ganhar contratando você. Não diga coisas como: sempre foi meu sonho trabalhar aqui! As empresas não ganham nada com seu sonho de querer trabalhar lá (triste, mas é a realidade), então mostre o que você tem de melhor para ajudar a empresa crescer. No meu caso a resposta que dei foi a seguinte: “Amo aprender e ensinar e estou constantemente me atualizando, além de gostar muito de ensinar e aprender com os outros integrantes da equipe, percebi que vocês em uma cultura internacional e isso me chamou muita atenção, seria ótimo poder trabalhar com vocês!”. """
desafio4 = driver.find_element(By.CLASS_NAME, 'jumbotron.desafios4')
desafio4.location_once_scrolled_into_view
sleep(.7)
paragrafo = driver.find_element(By.ID, 'campoparagrafo')
digitar_naturalmente(texto, paragrafo)
sleep(1)

#desafio 5
desafio5 = driver.find_element(By.CLASS_NAME, 'jumbotron.desafios5')
desafio5.location_once_scrolled_into_view
sleep(.8)
chk_carros = driver.find_elements(By.XPATH, "//input[@name='carros']")
chk_carros[1].click()
sleep(1)
chk_carros[3].click()
sleep(1)
chk_carros[4].click()
sleep(.5)

driver.execute_script("window.scrollBy(0, 200);")
sleep(2)
#posiciona_moto = driver.find_element(By.XPATH, "//*[contains(text(),'2. Marque todos')]")
#posiciona_moto.location_once_scrolled_into_view
chk_motos = driver.find_elements(By.XPATH, "//input[@name='motos']")
#chk_motos[8].location_once_scrolled_into_view
for moto in chk_motos:
    moto.click()
    sleep(.6)

#desafio6
desafio6 = driver.find_element(By.CLASS_NAME, 'jumbotron.desafios6')
desafio6.location_once_scrolled_into_view

drop = driver.find_element(By.ID, 'paisesselect')
opcoes = Select(drop)
opcoes.select_by_visible_text('Estados Unidos')
sleep(2)
opcoes.select_by_visible_text('Africa')
sleep(2)
opcoes.select_by_visible_text('Chille')
sleep(2)

#desafio 7
print('Desafio 7')
janela_Inicial = driver.current_window_handle
sleep(1)
desafio7 = driver.find_element(By.CLASS_NAME, 'jumbotron.desafios7')
desafio7.location_once_scrolled_into_view
sleep(.4)

btn_novaJanela = driver.find_element(By.XPATH, "//button[text()='Abrir nova janela']")
driver.execute_script('arguments[0].click()', btn_novaJanela)
sleep(1.3)

janelas = driver.window_handles
for janela in janelas:
    if janela not in janela_Inicial:
        driver.switch_to.window(janela)
        sleep(2)
        campo_opiniao = driver.find_element(By.ID, 'opiniao_sobre_curso')
        campo_opiniao.click()
        opiniao = '''O curso de automação é bem interessante da para fazer muita coisa legal automatizar praticamente qualquer site e via RPA qualquer software.'''
        digitar_naturalmente(opiniao, campo_opiniao)
        pesquisar = driver.find_element(By.ID, 'fazer_pesquisa')
        driver.execute_script('arguments[0].click()', pesquisar)
        sleep(2)
        driver.close()
        sleep(.7)

driver.switch_to.window(janela_Inicial)
sleep(2)
texto_D7 = '''Vamos fazer a última digitação'''
campo_D7 = driver.find_element(By.ID, 'campo_desafio7')
campo_D7.click()
sleep(0.4)
digitar_naturalmente(texto_D7, campo_D7)



input('digite algo para fechar... ')
driver.close()