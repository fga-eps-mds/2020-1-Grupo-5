import json, requests
from validate_email import validate_email


def eh_bissexto(ano):
    ano = int(ano)
    if ano % 4 == 0:
        
        if ano % 100 == 0:
            
            if  ano % 400 == 0:
                return True

            else:
                return False
        
        else:
            return True
    
    else:
        return False



def validaNome(nome):
    if len(nome) >= 8:
        return True

    return False



def validaSenha(senha):
    if len(senha) >= 8:
        return True

    return False

def validaEmail(email):

    if validate_email(email):
        return True

    return False


def validaMes(mes):
    try:
        if len(mes) == 2 and int(mes) > 0 and int(mes) < 13:
            return True
        
    except:
        return False

    return False


def validaAno(ano):

    try:
        if len(ano) == 4 and int(ano) > 1880 and int(ano) <= 2020:
            return True

    except:
        return False

    return False


def validaData(dia, mes, ano, user_data):
    if validaAno(ano):
        if eh_bissexto(ano):
            feb_days = 29

        else:
            feb_days = 28

    else:
        user_data.pop('Ano nascimento', None)
        return False

    if validaMes(mes):
        if mes == '02':
            max_days = feb_days
        
        elif mes in ['01', '03', '05', '07', '08', '10', '12']:
            max_days = 31

        else:
            max_days = 30

    else:

        user_data.pop("Mes nascimento")
        return False
    try:
        
        if len(dia) == 2 and int(dia) > 0 and int(dia) <= max_days:
            return True

        

    except:
        return False

    user_data.pop('Dia nascimento')
    return False


def validaGenero(genero):
    if genero in ['Homem Cis', 'Homem homossexual', 'Mulher Cis', 'Mulher Homossexual', 'Outros']:
        return True

    return False

def validaRaca(raca):
    if raca in ['Branco', 'Negro', 'Pardo', 'Indigena', 'Amarelo', 'Outro']:
        return True

    return False

def validaTrabalho(trabalho):
    if trabalho in ['Sim', 'Não']:
        return True

    return False

def validations(user_data, all_data):
    
    if "Username" in user_data:
        if not validaNome(user_data['Username']):
            user_data.pop("Username")
            all_data.add("Username")
            return False

    if "Email" in user_data:
        if not validaEmail(user_data['Email']):
            user_data.pop("Email")
            all_data.add("Email")
            return False
    
    if "Senha" in user_data:
        if not validaSenha(user_data['Senha']):
            user_data.pop("Senha")
            all_data.add("Senha")
            return False

    if "Dia nascimento"  in user_data and "Mes nascimento" in user_data and "Ano nascimento" in user_data:
        if not validaData(user_data['Dia nascimento'], user_data['Mes nascimento'], user_data['Ano nascimento'], user_data):
            if not "Dia nascimento" in user_data:
                all_data.add("Dia nascimento")

            if not "Mes nascimento" in user_data:
                all_data.add("Mes nascimento")

            if not "Ano nascimento" in  user_data:
                all_data.add("Ano nascimento")
            return False

    if "Genero sexual" in user_data:
        if not validaGenero(user_data['Genero sexual']):
            user_data.pop('Genero sexual')
            all_data.add("Genero sexual")
            return False

    if "Raça" in user_data:
        if not validaRaca(user_data['Raça']):
            user_data.pop('Raça')
            all_data.add("Raça")
            return False
    
    if "Trabalho" in user_data:
        if not validaTrabalho(user_data['Trabalho']):
            user_data.pop("Trabalho")
            all_data.add("Trabalho")
            return False


    return True