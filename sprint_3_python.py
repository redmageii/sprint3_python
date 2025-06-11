medicamentos = {
    'Paracetamol 500mg': {'quantidade': 50, 'dosagem': '500mg', 'peso_unitario(mg)': 800, 'classe': 'analgésico',
                          'localização': 'A1'},
    'Dipirona 1g': {'quantidade': 27, 'dosagem': '1g', 'peso_unitario(mg)': 1200, 'classe': 'analgésico',
                    'localização': 'A2'},
    'Ciprofloxacino 500mg': {'quantidade': 6, 'dosagem': '500mg', 'peso_unitario(mg)': 700, 'classe': 'antibiótico',
                             'localização': 'B1'}
}

classes = ['antibiótico', 'analgésico', 'antipirético', 'antidepressivo', 'antialérgico', 'antivirótico',
           'antidiabético', 'cardiovascular']

gavetas = {
    'antibiótico': 'A1',
    'analgésico': 'A2',
    'antipirético': 'A3',
    'antidepressivo': 'B1',
    'antialérgico': 'B2',
    'antivirótico': 'B3',
    'antidiabético': 'C1',
    'cardiovascular': 'C2'
}

unidades = ['ml', 'mg', 'g']

usuarios = {
    'admin': ['admin', 'Administrador'],
    'password': ['password', 'Administrador'],
    'tiffany': ['tiffy456', 'Tiffany'],
    'carlos': ['ca123456rlos', 'Carlos']
}

def forca_opcao(lista, msg, msg_erro):
    opt = input(msg)
    print(opt)
    if opt in lista:
        return opt
    else:
        print(msg_erro)
        return forca_opcao(lista, msg, msg_erro)

def check_num(msg, msg_erro):
    try:
        opt=int(input(msg))
    except:
        print(msg_erro)
        return check_num(msg, msg_erro)

def cadastrar_usuario():
    username = input('Insira seu nome de usuário: ').lower()
    if username in usuarios:
        print('Usuário já existente. Selecione a opção de login.')
        return
    # confirmação de senha
    while True:
        senha = input('Digite sua senha: ')
        if input('Confirme sua senha') == senha:
            break
        else:
            print('Senhas incompatíveis. Insira os campos novamente.')
    nome = input('Insira seu nome: ').title()
    # adição à lista de usuários
    usuarios[username] = [senha, nome]
    print(f'Seja bem-vindo(a), {nome}!')
    return nome

def autenticar_usuario():
    erro = 'Nome ou senha incorretos.'
    username = input('Insira seu nome de usuário: ').lower()
    pwd = input('Insira sua senha: ')
    if username in usuarios:
        if usuarios[username][0] == pwd:
            print(f'Bem-vindo(a), {usuarios[username][1]}!')
        else:
            print(erro)
            return autenticar_usuario()
    else:
        print(erro)
        return autenticar_usuario()
    return usuarios[username][1]

def status():
    for key in medicamentos.keys():
        print(f'=========={key}==========')
        for subkey in medicamentos[key]:
            print(f"{subkey.capitalize().replace('_', ' ')}: {medicamentos[key][subkey]}")
        peso_total = medicamentos[key]['quantidade'] * medicamentos[key]['peso_unitario(mg)']
        print(f'Peso total: {peso_total / 1000:.2f}g')
        if medicamentos[key]['quantidade'] < 10:
            print('STATUS: ALERTA - MEDICAMENTO EM QUANTIDADE BAIXA')
        else:
            print('STATUS: OK')
        print('\n')
    return

def cadastrar_item():
    while True:
        medicamento = input('Insira o nome do medicamento (apenas nome): ').capitalize()
        dosagem = str(check_num('Insira a dosagem em convenção adequada (apenas número): ', 'Valor incorreto'))
        und = forca_opcao(unidades, 'Insira a unidade da dosagem (ml, mg ou g)', 'Unidade incorreta.')
        medicamento += f' {dosagem + und}'
        medicamentos[medicamento] = {}
        medicamentos[medicamento]['quantidade'] = check_num('Insira a quantidade: ', 'Valor inválido.')
        medicamentos[medicamento]['dosagem'] = dosagem
        medicamentos[medicamento]['peso_unitario(mg)'] = (check_num('Insira o peso unitário (mg): ', 'Valor inválido'))
        joined_classes='\n'.join(classes)
        print(f'==========CLASSES==========\n{joined_classes}')
        classe = forca_opcao(classes, 'Selecione a classe do medicamento: ', 'Classe inválida.')
        medicamentos[medicamento]['classe'] = classe
        medicamentos[medicamento]['localização'] = gavetas[classe]
        break
    return medicamento

def remover_item():
    if len(medicamentos.keys()) > 0:
        print('\n'.join(medicamentos.keys()))
        item = forca_opcao(medicamentos.keys(),
                           'Qual medicamento deseja remover? (especificar o nome seguido de dosagem): ', 'Nome inválido')
        del medicamentos[item]
        return print(f'{item} removido')
    else:
        print('Lista vazia.\nRetornando...')

def alterar_item():
    joined_medicamentos='\n'.join(medicamentos.keys())
    print(f'============================\n{joined_medicamentos}')
    item = forca_opcao(medicamentos.keys(), 'Qual medicamento deseja alterar? (especificar o nome seguido de dosagem)',
                       'Nome inválido')
    joined_itens='\n'.join(medicamentos[item].keys())
    print(f'============================\n{joined_itens}')
    categoria = forca_opcao(medicamentos[item].keys(), 'Selecione uma categoria para alterar: ', 'Categoria inválida.')
    if categoria == 'classe':
        inpt = forca_opcao(classes, 'Selecione a classe do medicamento: ', 'Classe inválida.')
        medicamentos[item][categoria] = inpt
        medicamentos[item]['localização'] = gavetas[inpt]
    else:
        inpt = input(f'Insira um novo valor para {categoria}: ')
        if inpt.isnumeric():
            medicamentos[item][categoria] = int(inpt)
    return

opcoes_login = {
    '1': autenticar_usuario,
    '2': cadastrar_usuario
}

opcoes_estoque = {
    '1': status,
    '2': cadastrar_item,
    '3': alterar_item,
    '4': remover_item
}

print('(c) OmniSystem. Todos os direitos reservados.\nBem-vindo ao sistema OmniStock ver. 1.123581321.\nPor favor, insira suas informações para login ou cadastre um usuário.')
print('1 - Autenticar usuário\n2 - Cadastrar usuário')
nome = opcoes_login[forca_opcao(opcoes_login.keys(), 'Selecione uma opção:', 'Opção inválida.')]()
while True:
    print(f'Usuário ativo: {nome}')
    print(
        f'=================================\n1 - Status do estoque\n2 - Cadastro de medicamentos\n3 - Alterar item\n4 - Remover item\n5 - Sair')
    opt = forca_opcao(['1', '2', '3', '4', '5'], 'Selecione uma opção: ', 'Opção inválida.')
    if opt in opcoes_estoque.keys():
        opcoes_estoque[opt]()
    else:
        print('Encerrando...')
        break