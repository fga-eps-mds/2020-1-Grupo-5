# DoctorS Bot
<p align = "center"> &emsp;&emsp; <img src="https://github.com/fga-eps-mds/2020-1-DoctorS-Bot/blob/master/assets/DoctorS.png" width="200" height="200"/> </p>

[![Percentage of issues still open](http://isitmaintained.com/badge/open/fga-eps-mds/2020.1-DoctorS-Bot.svg)](http://isitmaintained.com/project/fga-eps-mds/2020-1-DoctorS-Bot "Percentage of issues still open")

[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

## Links R1

- Apresentação: https://youtu.be/RGD5kv_4Os0
- Slides utilizados: https://docs.google.com/presentation/d/1Db5Fj-vUUeLpbQa2ymwLiOIqcltN1ZVqh7aEw6ncQ44/edit#slide=id.g1f87997393_0_782

## Links R2

- Apresentação: https://youtu.be/mgH-CXVySNU
- Slides utilizados: https://docs.google.com/presentation/d/1XKIUHvqZNFerVvmGSPR6QmDFBMApbzzXzV6H7tIyAiA/edit?usp=sharing

## Apresentação

O Projeto do DoctorS Bot busca ajudar toda a sociedade a combater o contágio do novo Coronavírus (Sars-CoV-2). O projeto trás uma integração com o aplicativo [Guardiões da Saúde](https://github.com/proepidesenvolvimento/guardioes-app) por meio de um Bot no Telegram (@DoctorS_bot) e busca trazer maior acessibilidade e facilidade no uso da aplicação.

<br>

O repositório é mantido e gerenciado por alunos da Universidade de Brasília, no curso de Engenharia de Software (FGA - Gama). Caso possua dúvidas ou sugestões, [entre em contato pelo email](mailto:bot.doctors@gmail.com).

## Utilização

Para utilizar o DoctorS, basta procurar o contato [@DoctorS_bot](https://t.me/DoctorS_bot) no Telegram e clicar em começar.


## Instalação
Caso queira executar uma instância do nosso projeto:

* Consiga um [Telegram TOKEN](https://telegram.me/BotFather)

* Crie um arquivo com nome de "token.txt" na pasta config

* Insira o TOKEN no arquivo

* Instale a [API do Guardiões da Saúde](https://github.com/proepidesenvolvimento/guardioes-api) e execute-a

* Instale todos as bibliotecas necessárias(preferencialmente num [Ambiente Virtual](https://virtualenv.pypa.io/en/latest/)):\
```python3 -m pip install -r requirements.txt```

* Quando a API do Guardiões estiver sendo executata, basta executar o DoctorS.py:\
 ```python3 DoctorS.py```
 
### Erros comuns
* Erro na biblioteca python-telegram-bot:

    ```ImportError: cannot import name 'Bot' from 'telegram'```

    Basta executar manualmente:
    
    ```python3 -m pip uninstall python-telegram-bot```
    
    logo após, execute:
    
    ```python3 -m pip install python-telegram-bot```

## Integrantes

 O projeto é executado por 6 alunos da Universidade de Brasília, sobre supervisão da professora [Carla Rocha](https://github.com/RochaCarla).
 
 
 * [João Alves](https://github.com/Joaoaalves)
 * [Kevin Batista](https://github.com/k3vin-batista)
 * [Marcos Adriano Nery](https://github.com/marcosadrianonery)
 * [Lucas Rodrigues](https://github.com/lucas229)
 * [Gabriel Batalha](https://github.com/Gabriel-Azevedo-Batalha)
 * [João Pedro Moura](https://github.com/Joao-Pedro-Moura)
 
### Contato

email : bot.doctors@gmail.com
