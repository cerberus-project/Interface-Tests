from constantes import moment

log_resultado_testes = {'hora_execucao': moment,
                            'funcionalidade': f'criar grupo',
                            'concluido': True,
                            'log_erro': ''
                            }

def atualizar_log(resultado, acao):
    log_resultado_testes['concluido'] = False
    if acao == 'focar':
        log_resultado_testes['log_erro'] = resultado

    elif acao == 'inserir email':
        log_resultado_testes['log_erro'] = 'Falha na etapa: Login - Inserir Email'

    elif acao == 'inserir senha':
        log_resultado_testes['log_erro'] = 'Falha na etapa: Login - Inserir Senha'

    elif acao == 'criar grupo':
        log_resultado_testes['log_erro'] = resultado

    elif acao == 'checar grupo':
        log_resultado_testes['log_erro'] = resultado

