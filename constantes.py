# -*- coding: utf-8 -*-
import undetected_chromedriver as uc
import datetime


moment = datetime.datetime.now().strftime("%A %d %B %y %I:%M")
moment = str(datetime.datetime.now().strptime(moment, "%A %d %B %y %I:%M")).replace(':', '-')

navegador = uc.Chrome()
link_frontend = "https://cerberus-front.vercel.app"

# credentials
user_id = ''
authorization = ''

header = {'user_id': f'{user_id}',
          'authorization': f'{authorization}'
          }

email = ""
senha_email = ""

# BOTOES LOGIN GOOGLE
login_google = 'LoginButton_loginSession__Cfhim' # BY.CLASSNAME
email_google = '//*[@id="identifierId"]'
senha_google = '//*[@id="password"]/div[1]/div/div[1]/input'
botao_ok = '//*[@id="identifierNext"]/div/button/span'
botao_ok_senha = '//*[@id="passwordNext"]/div/button/span'

# BOTOES GRUPO
botao_add_grupo = 'AddButton_homeTopButton__AmRze'  # BY.CLASSNAME
campo_nome_grupo = '/html/body/main/section[3]/div/form/label[1]/input'
campo_desc_grupo = '/html/body/main/section[3]/div/form/label[2]/input'
botao_criar_grupo = '/html/body/main/section[3]/div/form/button'
