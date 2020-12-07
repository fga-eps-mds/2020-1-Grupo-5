# Documento de Arquitetura

|Data|Versão|Descrição|Autor|
|:--:|:----:|:----:|:--:|
|11/09|0.1|Adicionando subitem 1.1|Kevin Luis|
|13/09|0.2|Adicionando subitem 3.1|Gabriel Batalha|
|13/09|0.3|Adicionando subitem 3.2|Lucas Rodrigues|
|14/09|0.4|Adicionando subitem 1.2|Marcos Adriano|
|14/09|0.5|Adicionando subitens 2.1 e 2.2|João Alves|
|16/09|0.6|Adicionando subitem 4.1 |João Pedro|
|17/09|0.7|Revisão ortográfica|Lucas Rodrigues|
|23/09|0.8|Corrigido subitens 2.1 e 2.2|João Alves|
|10/11|0.9|Adicionando diagrama de casos de uso|Kevin Luis|

## 1. Introdução

### 1.1 Finalidade 

Esse documento tem como finalidade apresentar a arquitetura do projeto de software DoctorS. Ele mostra as funcionalidades como um todo e ajuda os desenvolvedores e gestores com informações ao longo do período de desenvolvimento.

### 1.2 Escopo

Por meio desse documento pretende-se apresentar de forma estruturada a construção da arquitetura do projeto, permitindo assim um melhor entendimento ao leitor e a compreensão do funcionamento do sistema e suas partes. Além disso, são apresentadas as métricas, restrições, abordagens e demais parâmetros concernentes à arquitetura em desenvolvimento.

## 2. Representação arquitetural

### 2.1 Diagrama de relações

![](https://i.ibb.co/6wZ9dGF/Diagrama-de-Rela-es.png)

### 2.1.1 Front-End

O front-end é a parte responsável pela troca de mensagens, ou seja, o Telegram é basicamente todo o front-end do produto. Parte essa que fica responsável por transportar a mensagem do usuário para o bot do DoctorS e vice-versa.

### 2.1.2 Back-End

O back-end é reponsável por interpretar a mensagem do usuário, e responder da melhor forma, caso seja requisitado alguma função que envolva entrada de dados do usuário(Login, informe diário e etc), ele fará o registro, transportará os dados para a API do Guardiões e também para o banco de dados do próprio bot.

### 2.2 Diagrama de casos de uso

![](https://i.ibb.co/p4DkQVK/diagrama-casos-de-uso.png)

### 2.3 Tecnologias

<p align = "center"> &emsp;&emsp; <img src="https://i.ibb.co/M6wZRbb/python.png" width="150" height="150"/> </p> 

O projeto em sua maior parte será feito na linguagem [Python](https://www.python.org). Este software ficará responsável por interpretar as mensagens recebidas, respondelas e quando necessário ela também fará toda a comunicação entre a API responsável pelo armazenamento de dados(Guardiões da Saúde) e a API responsável pela entrada de dados(Telegram Bot API).

<br>
<p align = "center"> &emsp;&emsp; <img src="https://i.ibb.co/ZJV4pXM/telegram.png" width="150" height="150"/> </p>  

A entrada de dados ocorre somente por meio do Telegram, que fornece uma API que envia todas as mensagens (dados) recebidas para o codigo do DoctorS, onde ocorre a validação de dados, reconhecimento de comandos e mensagens recebidas.

<br>
<p align = "center"> &emsp;&emsp; <img src="https://i.ibb.co/RjyfJ6T/Guardioes-Logo.png" width="150" height="150"/> </p>  

A partir do momento que for solicitado algum acesso ao nosso banco de dados, nossa API fará uma request para a API do Guardiões da Saúde pedindo ou inserindo todos os dados requisitados caso o pedido seja válido.

As [Tecnologias da API do Guardiões](https://github.com/proepidesenvolvimento/guardioes-api#tecnologias) podem ser encontradas clicando no link.

## 3. Metas e restrições da arquitetura

### 3.1 Metas do software DoctorS
Os objetivos do DoctorS são :
- Oferecer uma alternativa ao uso do Guardiões da Saúde em um mensageiro de uso cotidiano
- Permitir ao usuário utilizar as principais funções do aplicativo através de diálogo
- Tornar fácil a compreensão e o uso das funcionalidades
- Ampliar o fornecimento de informações relevantes sobre a saúde para a população

### 3.2 Restrições da arquitetura
- Possuir conexão com a Internet
- Ter um dispositivo com acesso ao Telegram
- O ChatBot será desenvolvido em Python e será utilizada a API do Guardiões da Saúde
- A interação com o ChatBot deve ser intuitiva
- O código deve ter boa qualidade, sendo consistente, fácil de entender, ler, estudar e realizar manutenção

## 4. Visão Lógica

### 4.1 Diagrama de Pacotes

Os diagramas de pacotes mostram a interação entre as relações das pastas e seus arquivos.

![](https://i.ibb.co/ZzHbXxz/Diagrama-Telegram.png)

Imagem 5 - Diagrama de pacotes do Microsserviço Conexão com o Telegram.

![](https://i.ibb.co/YP3YVMf/Diagrama-Guardi-es.png)

Imagem 6 - Diagrama de pacotes do Microsserviço Conexão com Guardiões da Saúde.

![](https://i.ibb.co/r5GsBTD/Diagrama-Python.png)

Imagem 7 - Diagrama de pacotes do Microsserviço Bot em python.

![](https://i.ibb.co/wMLSnx6/Diagrama-Geral.png)

Imagem 8 - Diagrama de pacotes geral dos Microsserviços.
