import json, requests
from validate_email import validate_email


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

def validaGenero(genero):
    if str(genero).lower() in ['homem cis', 'homem homossexual', 'mulher cis', 'mulher homossexual', 'outro']:
        return True

    return False

def validaRaca(raca):
    if str(raca).lower() in ['branco', 'negro', 'pardo', 'indigena', 'amarelo', 'outro']:
        return True

    return False

def validaTrabalho(trabalho):
    if str(trabalho).lower() in ['sim', 'não', 'nao']:
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