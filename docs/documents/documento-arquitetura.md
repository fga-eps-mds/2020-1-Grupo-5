# Documento de Arquitetura

|Data|Versão|Descrição|Autor|
|:--:|:----:|:----:|:--:|
|11/09|0.1|Adicionando subitem 1.1|Kevin Luis|
|13/09|0.2|Adicionando subitem 3.1|Gabriel Batalha|
|13/09|0.3|Adicionando subitem 3.2|Lucas Rodrigues|
|14/09|0.4|Adicionando subitem 1.2|Marcos Adriano|
|14/09|0.5|Adcionado item 2, subitem 2.1 2.2| João Alves|

## 1. Introdução

### 1.1 Finalidade 

<p align="justify"> Esse documento tem como finalidade apresentar a arquitetura do projeto de software DoctorS. Mostrando as funcionalidades como um todo e ajudando os desenvolvedores e gestores com informações ao longo do período de desenvolvimento. </p>

### 1.2 Escopo

<p align="justify"> Por meio desse documento, pretende-se apresentar de forma estruturada a construção da arquitetura do projeto, permitindo assim um melhor entendimento ao leitor, e a compreensão do funcionamento do sistema e suas partes, além de apresentar as métricas, restrições, abordagens e demais parâmetros concernentes a arquitetura em desenvolvimento. </p>

## 2. Representação arquitetural

### 2.1 Padrão arquitetural

O projeto será desenvolvido utilizando o padrão MVC(Model-View-Controller), por meio da utilização da linguagem Python. Esse modelo foi escolhido por:

 * Facilitar o reaproveitamento de código
 * Melhorar na manutenibilidade
 * Facilitar a implementação de todas as API's que utilizaremos
 * Melhorar na interação/integração da equipe

<p align="center">
  <img src="https://github.com/fga-eps-mds/2020-1-Grupo-5/blob/develop/assets/doc_arquitetura/modeloMVC.png" />
</p>

---

**Model** é a camada responsável pela lógica do software, gerenciamento e uso de dados de toda a aplicação, nesse caso, a camada está bastante presente na [API do Guardiões da Saúde](https://github.com/proepidesenvolvimento/guardioes-api), pois a API é responsável pelo gerenciamento e uso do banco de dados. Geralmente essa camada também possui se não todas, a maioria das regras de negócios da aplicação.

**View** é qualquer saída e apresentação dos dados e/ou informações contidas na aplicação, no caso do **DoctorS Bot** a interface do Telegram é basicamente toda a camada de View do software.

**Controller** é a camada que media as duas outros camadas(View e Model) e é responsável pelo controle de entrada e saída de dados no sistema. No **DoctorS Bot** essa camada é praticamente representada pelo Python junto da [Python-Telegram-Bot](https://github.com/python-telegram-bot/python-telegram-bot)(Biblioteca presente no Python), no qual esses fazem requisições tanto para a [API do Telegram](https://core.telegram.org/bots/api) quanto para a do Guardiões da Saúde sempre que necessário.

### 2.2 Tecnologias


<p align="center">
  <img src="https://github.com/fga-eps-mds/2020-1-Grupo-5/blob/develop/assets/doc_arquitetura/python.png" />
</p>

O projeto em sua maior parte será feito na linguagem [Python](https://www.python.org), esta que será predominante na camada de Controller, ocorrendo a validação de entradas, também fará toda a comunicação entre a API responsável pelo armazenamento de dados e a API responsável pela entrada de dados.

<br>
<p align="center">
  <img src="https://github.com/fga-eps-mds/2020-1-Grupo-5/blob/develop/assets/doc_arquitetura/telegram.png" />
</p>

A entrada de dados ocorre somente por meio do Telegram, no qual o Telegram fornece uma API que envia todas as mensagens(dados) recebidas para nossa API do python e lá ocorre a validação de dados, reconhecimento de comandos e mensagens recebidas.

<br>
<p align="center">
  <img src="https://github.com/fga-eps-mds/2020-1-Grupo-5/blob/develop/assets/doc_arquitetura/GuardioesLogo.png" />
</p>

A partir do momento que for solicitado algum acesso ao nosso banco de dados, nossa API fará uma request para a API do Guardiões da Saúde, pedindo ou inserindo todos os dados requisitados caso seja um pedido válido.

E as [Tecnologias da API do Guardiões](https://github.com/proepidesenvolvimento/guardioes-api#tecnologias) podem ser encontradas clicando no link.

## 3. Metas e restrições da arquitetura

### 3.1 Metas do software DoctorS
Os objetivos do DoctorS são :
- Oferecer uma alternativa no uso do Guardiões da Saúde em um mensageiro de uso cotidiano
- Permitir o usuário utilizar as principais funções do aplicativo através de diálogo
- Tornar fácil a compreensão e o uso das funcionalidades.  
- Ampliar o fornecimento de informações relevantes sobre a saúde para a população 

### 3.2 Restrições da arquitetura
- Possuir conexão com a Internet
- Ter um dispositivo com acesso ao Telegram
- O ChatBot será desenvolvido em Python e será utilizada a API do Guardiões da Saúde
- A interação com o ChatBot deve ser intuitiva
- O código deve ter boa qualidade, sendo consistente, fácil de entender, ler, estudar e realizar manutenção
