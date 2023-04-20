from selenium.webdriver.support.wait import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from constantes import *
from utils.notificar_resultados import *

#TODO:
#Deletar grupo após fim do teste, para evitar acumulo no banco de dados
#Enviar JSON de resultado para email e posteriormente registrar num banco de dados
#criar repositorio e explicar as etapas do fluxo no readme


def wait_to_send(element, Send):
    resultado = False
    try:
        WDW(navegador, 5).until(EC.presence_of_element_located(('xpath', element)))
        Enter_Data = navegador.find_element('xpath', element)
        Enter_Data.send_keys(Send)
        time.sleep(2)
        resultado = True
    except:
        return resultado

    return resultado


def wait_xpath(element):
    WDW(navegador, 5).until(EC.presence_of_element_located(('xpath', element)))


def wait_click(element):
    resultado = False
    try:
        WDW(navegador, 10).until(EC.element_to_be_clickable(('xpath', element)))
        element = navegador.find_element('xpath', element).click()
        time.sleep(5)
        resultado = True
    except:
        return resultado

    return resultado


def wait_click_class(element):
    resultado = False
    try:
        WDW(navegador, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, element)))
        element = navegador.find_element(By.CLASS_NAME, element).click()
        time.sleep(5)
        resultado = True
    except:
        return resultado

    return resultado


def focar_janela_google():
    qnt_tentativas = 3
    resultado = False
    while qnt_tentativas > 0 and not resultado:
        try:
            if qnt_tentativas < 3:
                wait_click(login_google)

            janelas_abertas = navegador.window_handles
            navegador.switch_to.window(janelas_abertas[1])
            resultado = True
        except:
            qnt_tentativas -= 1

    if not resultado:
        log = 'Falha na etapa: Focar janela de login Google.'
        atualizar_log(log, 'focar')
        navegador.quit()

    return resultado


def focar_janela_main():
    qnt_tentativas = 3
    resultado = False
    while qnt_tentativas > 0 and not resultado:
        janelas_abertas = navegador.window_handles
        try:
            navegador.switch_to.window(janelas_abertas[0])
            resultado = True
        except:
            qnt_tentativas -= 1

    if not resultado:
        log = 'Falha na etapa: Focar janela Principal. O login foi realizado mas houve uma falha ao tentar voltar o foco do bot para a tela principal'
        atualizar_log(log, 'focar')
        navegador.quit()
    return resultado


def criar_grupo():
    nome_grupo = f'{moment}//BOT-Teste'
    desc_grupo = 'BOT-desc test'
    try:
        wait_click_class(botao_add_grupo)
        wait_to_send(campo_nome_grupo, nome_grupo)
        wait_to_send(campo_desc_grupo, desc_grupo)
        wait_click(botao_criar_grupo)
        time.sleep(2)
        return nome_grupo
    except:
        log = 'Falha na etapa: Criar Grupo.'
        atualizar_log(log, 'criar grupo')
        navegador.quit()


def checar_grupo(nome_do_grupo):
    conteudo_pagina = navegador.find_element('xpath', '/html/body/main')
    if nome_do_grupo not in conteudo_pagina.text:
        log = 'Falha na etapa: Checar se grupo foi criado.'
        atualizar_log(log, 'checar grupo')
        print(log_resultado_testes)

print('inicio fora da main')

if __name__ == '__main__':
   
    navegador.get(link_frontend)
    print('cheguei aq')
    wait_click_class(login_google)

    # focar tela login google
    focar_janela_google()

    # inserir email
    time.sleep(5)
    digitar_email = wait_to_send(email_google, email)
    clicar_ok = wait_click(botao_ok)
    if not digitar_email or not clicar_ok:
        atualizar_log(False, 'inserir email')
        navegador.quit()

    # inserir senha
    digitar_senha = wait_to_send(senha_google, senha_email)
    clicar_ok = wait_click(botao_ok_senha)
    if not digitar_senha or not clicar_ok:
        atualizar_log(False, 'inserir senha')
        navegador.quit()

    focar_janela_main()
    grupo = criar_grupo()
    checar_grupo(grupo)
    print(log_resultado_testes)
    navegador.quit()
