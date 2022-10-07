import PySimpleGUI as sg

def tela_inicial():
    sg.theme('Dark2')
    
    folha = [
        [sg.Text('Informe as horas trabalhadas:', font='arial 12', pad=(0,0))],
        [sg.Input(size=(20, 0), font='arial 12', pad=(0,0), key='tempo')],
        [sg.Text('Informe o valor das horas:', font='arial 12', pad=(0,0))],
        [sg.Input(size=(20, 0), font='arial 12', pad=(0,0), key='hora')],
    ]
    
    coluna1 = [
        [sg.Text( 'Salário Bruto', font='arial 12')],
        [sg.Text( 'INSS', font='arial 12')],
        [sg.Text( 'IRRF', font='arial 12')],
        [sg.Text( 'Vale Transporte', font='arial 12')],
        [sg.Text( 'FGTS', font='arial 12')],
        [sg.Text( 'Total de Descontos', font='arial 12')],
        [sg.Text( 'Salário Líquido', font='arial 12')]
    ]
    
    coluna2 = [
        [sg.Input(font='arial 12 bold', key='sb', size=(5,1))],
        [sg.Input(font='arial 12 bold', key='inss', size=(5,1))],
        [sg.Input(font='arial 12 bold', key='irrf', size=(5,1))],
        [sg.Input(font='arial 12 bold', key='vt', size=(5,1))],
        [sg.Input(font='arial 12 bold', key='fgts', size=(5,1))],
        [sg.Input(font='arial 12 bold', key='total_descontos', size=(5,1))],
        [sg.Input(font='arial 12 bold', key='salario_liquido', size=(5,1))]
    ]
    
    botoes = [
        [sg.Button('Calcular', font='arial 12', size=(10,1), pad=((0,15),0)),
         sg.CButton('Sair',font='arial 12',size=(8,1))]
    ]
    
    layout = [
        [sg.Text('Calcule sua folha', font='arial 18 bold', justification='center')],
        [sg.Column(folha, justification='center', element_justification='center')],
        [sg.Column(coluna1, pad=((0,20),0)),
         sg.Column(coluna2)],
        [sg.Column(botoes, justification='center')]
    ]
    
    telaprin = sg.Window('Cálculo de Folha de Pagamento', element_padding=(0,10), layout=layout, size=(600,700), finalize=True)