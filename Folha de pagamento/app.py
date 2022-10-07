from interface_grafica import *
from consulta_cep import *
tela_inicial()
while True:
    window, event, values = sg.read_all_windows()
    
    if event == sg.WIN_CLOSED:
        break

    if event == 'Calcular':
        try:
            sb = calculo(values['folha'])['sb']
            bairro = calculo(values['cep'])['bairro']
            localidade = calculo(values['cep'])['localidade']
            uf = calculo(values['cep'])['uf']
            ibge = calculo(values['cep'])['ibge']
            ddd = calculo(values['cep'])['ddd']

            window['sb'].update(sb)
          

        except:
            sg.Popup('Verifique se os campos foram preenchidos corretamente')