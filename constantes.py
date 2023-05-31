# -*- coding: utf-8 -*-
import os
import undetected_chromedriver as uc
import datetime
from dotenv import load_dotenv
load_dotenv()


#configuracao  do selenium

#caso seu chrome esteja desatualizado especifique a versao dele aqui
#navegador = uc.Chrome(version_main=100)

navegador = uc.Chrome()
link_frontend = "https://cerberus-front.vercel.app"

# credentials
user_id = '-NRplxUo09agV0nxT3Q7'
authorization = 'dccc54bb-6444-447d-b258-091dc2e1bf7e'

header = {'user_id': f'{user_id}',
          'authorization': f'{authorization}'
          }

email = os.environ["email"]
senha_email = os.environ["senha_email"]


# data-hora para ser usado nos logs
moment = datetime.datetime.now().strftime("%A %d %B %y %I:%M")
moment = str(datetime.datetime.now().strptime(moment, "%A %d %B %y %I:%M")).replace(':', '-')

# BOTOES LOGIN GOOGLE
login_google = 'LoginButton_loginSession__Cfhim' # BY.CLASSNAME
email_google = '//*[@id="identifierId"]'
senha_google = '//*[@id="password"]/div[1]/div/div[1]/input'
botao_ok = '//*[@id="identifierNext"]/div/button/span'
botao_ok_senha = '//*[@id="passwordNext"]/div/button/span'

# BOTOES GRUPO
botao_add_grupo = 'AddButton_homeTopButton__AmRze'  # BY.CLASSNAME
campo_nome_grupo = '/html/body/section/div/form/label[1]/input'        # xpath
campo_desc_grupo = '/html/body/section/div/form/label[2]/input'        # xpath
botao_criar_grupo = 'Modal_submitButton__jCeap'     # BY.CLASSNAME
