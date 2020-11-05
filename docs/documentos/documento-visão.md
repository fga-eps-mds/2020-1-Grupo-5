# Histórico de Versões

Data|Versão|Descrição|Autor
-|-|-|-
03/09|0.1.0|Adição do template do documento| Kevin Luis |
07/09|0.1.1|Adição dos subitens do item 3| Marcos Adriano|
08/09|0.1.2|Adição dos subitens do item 5| João Alves|
08/09|0.1.3|Adição dos subitens do item 6| Lucas Rodrigues|
08/09|0.1.4|Adição dos subitens 2 e 3 do item 4| Gabriel Batalha|
08/09|0.1.5|Adição do subitem 1 do item 4| Lucas Rodrigues|
08/09|0.1.6|Adição dos subitens do item 2| João Pedro|
09/09|0.1.7|Adição dos subitens do item 1| Kevin Luis|
10/09|0.1.8|Revisão ortográfica| Lucas Rodrigues|

## **1. Introdução**

### 1.1 Propósito

Este documento tem o objetivo de apresentar uma visão geral sobre o ChatBot DoctorS, mostrando suas características e seu objetivo.

### 1.2 Escopo

O ChatBot DoctorS é um sistema desenvolvido para coletar informações do estado de saúde diariamente dos usuários.

### 1.3 Definições, acrônimos e abreviações

- DoctorS: O nome do ChatBot
- ChatBot: <i>Software</i> que através de inteligência artificial conduz uma conversa para automatizar os processos
- FGA: Faculdade do Gama
- MDS: Equipe de Métodos de Desenvolvimento de <i>Software</i>
- <i>Telegram</i>: Aplicativo de mensagens instantâneas 
- UnB: Universidade de Brasília

### 1.4 Referências

- IBM Knowledge Center - Documento de Visão: A estrutura de tópicos do documento de visão. Disponível em https://www.ibm.com/support/knowledgecenter/pt-br/SSWMEQ_4.0.6/com.ibm.rational.rrm.help.doc/topics/r_vision_doc.html. Acesso em 01 set. 2020;
- Disponível em https://github.com/fga-eps-mds/2018.1_Gerencia_mais/blob/master/docs/documentos/Mds/Documento_de_Visao.md#1. Acesso em 01 set. 2020.
- Disponível em https://fga-eps-mds.github.io/2019.1-ADA/#/docs/product/vision_document. Acesso em 01 set. 2020.

### 1.5 Visão Geral

Esse é um documento informativo sobre o ChatBot DoctorS em que estão descritos os detalhes do <i>software</i>.
Ele está organizado no formato de tópicos e subtópicos sequenciais numerados. A ordem desses tópicos é: Introdução; Posicionamento; Descrições da Parte Interessada e do Usuário; Visão Geral do Produto; Recursos do Produto; Restrições; Outros Requisitos do Produto.

## **2. Posicionamento**

### 2.1 Oportunidade de Negócios

O aplicativo Guardiões da Saúde é de extrema importância para obter informações de como está a saúde das pessoas em nossa comunidade neste tempo de pandemia. O nosso projeto pretende facilitar e expandir essa comunicação ao maior número de pessoas possível, utilizando uma rede social que é de comum uso entre os membros da nossa comunidade.

### 2.2 Descrição do problema

|**O problema é**|Pouco acesso ao aplicativo Guardiões da Saúde.|
|:---:|:---:|
|**afeta**|Órgãos que utilizam os dados obtidos pelo app.|
|**cujo impacto é**|Dificuldade, por meio das autoridades públicas, no planejamento do combate a pandemia.|
|**uma boa solução seria**|O uso do ChatBot para facilitar a comunicação e obtenção de dados.|

### 2.3 Instrução de Posição do Produto

|**Para** |Usuários do app <i>Telegram</i>.|
|:---:|:---:|
|**Que** |Querem receber relatórios diários sobre seu estado de saúde|
|**O DoctorS_bot é**| Um ChatBot integrado ao <i>Telegram</i>.|
|**Que**| Obtém dados dos usuários.|
|**Diferente de**|Precisar se deslocar a um médico, em qualquer sinal de sintoma da Covid-19.|
|**Nosso produto**|Facilita a comunicação e informa ao usuário, caso esteja com algum sintoma da Covid-19, se necessário ir ao hospital.|

## **3. Descrições da Parte Interessada e do Usuário**

Nome|Descrição|Responsabilidade
:--:|:--:|:--:
Equipe de Desenvolvimento | Estudantes da disciplina Métodos de Desenvolvimento de <i>Software</i> da Universidade de Brasília Campus Gama | Desenvolvimento, documentação, implementação e testes do <i>software</i> solicitado.
Professor e Professora | Professor da disciplina de Métodos de Desenvolvimento de <i>Software</i> e a professora da disciplina de Engenharia de Produto de <i>Software</i>, ambos da Universidade de Brasília Campus Gama | Avaliar e orientar os estudantes de ambas as disciplinas respectivamente.


### 3.1 Resumo dos Usuários

Nome|Descrição
:-:|:-:
Monitorado | Usuário que está tendo a saúde monitorada continuamente.

### 3.2 Ambiente do Usuário

A aplicação será utilizada no mensageiro <i>Telegram</i>, que atende as plataformas <i>mobile</i> e <i>web</i>.

### 3.3 Perfis dos Envolvidos

#### 3.3.1 Equipe de Desenvolvimento

Representante|Gabriel Batalha, João Alves, João Pedro, Kevin, Lucas, Marcos Adriano.
:-:|:-:
**Descrição**|Desenvolvedores.
**Tipo**|Estudantes da Universidade de Brasília, cursando a disciplina de Métodos de Desenvolvimento de Software.
**Responsabilidade**|Desenvolvimento, Testes, Documentação e Implementação do <i>software</i>.
**Critérios de Sucesso**|Finalizar o desenvolvimento e realizar a entrega do <i>software</i> dentro dos prazos.
**Envolvimento**|Alto.
**Problemas/Comentários**|Alguns integrantes da equipe são inexperientes nas linguagens de programação utilizadas no desenvolvimento, no padrão arquitetural e nas metodologias de desenvolvimento.


### 3.4 Perfis dos Usuários

#### 3.4.1 Monitorado
Representante|Monitorado
:-:|:-
**Descrição**|Monitoramento da saúde de pessoas, sobretudo durante a pandemia.
**Tipo**|Monitorado.
**Responsabilidade**| Utilizar o aparelho para o propósito.
**Critérios de Sucesso**| Permanência da saúde.
**Envolvimento**|Médio.
**Problemas/Comentários**| - 


### 3.5 Principais Necessidades dos Usuários ou dos Envolvidos

Necessidade|Prioridade|Interesse|Solução Atual|Solução Proposta
:-:|:-:|:-:|:-:|:-:
Auxiliar na manutenção da saúde do usuário.|Alta|Tornar a manutenção da saúde mais fácil e dinâmica.|Monitoramento contínuo.|Aplicação que, por meio de um mensageiro, fará o report diário da saúde do usuário.

### 3.6 Alternativas e Concorrência

A proposta é justamente garantir as funcionalidades de um aplicativo que já se encontra no mercado, e é justificada por associar que os usuários em geral terão uma maior aceitação da ideia se este já estiver inserido no contexto dos mesmos, que no caso é o mensageiro <i>Telegram</i>.

## **4. Visão Geral do Produto**

### 4.1 Perspectiva do Produto
O produto tem como objetivo estender para o <i>Telegram</i> as funcionalidades do aplicativo <i>mobile</i> Guardiões da Saúde, utilizando um ChatBot. Os usuários cadastrados devem informar diariamente sobre o aparecimento ou não de sintomas relacionados ao COVID-19. Com as informações coletadas são gerados relatórios contendo estatísticas e dados relacionados a esse problema. Dessa forma, ele pode auxiliar no combate à doença.

 ### 4.2 Resumo das Capacidades
 
 | **Benefícios para o Cliente**                                 | **Recursos de suporte**                    |
 |---------------------------------------------------------------|--------------------------------------------|
 | Acesso às próprias informações                                | Criação de usuário                         |
 | Capacidade de oferecer informações para o mapeamento de saúde | Informe de estado físico diário               |
 | Acesso a relatórios de saúde                                  | Envio de relatórios produzidos pelo ChatBot    |
 | Acesso à dicas para cuidar da saúde                           | Dicas e práticas saudáveis                 |
 
 ### 4.3 Suposições e Dependências
 - O usuário deve ter em alcance o aplicativo <i>Telegram</i>
 - O usuário deve estar conectado à Internet

## **5. Recursos do Produto**

O produto possuirá o sistema de login, armazenando os usuários e informações únicas com o intuito de armazenar e gerar relatórios quanto aos infectados em cada região.

### 5.1 Recursos de usuário
 
 * Cadastrar usuário
 * Informe físico diário (quanto aos sintomas)
 * Armazenar informações

### 5.2 Recursos de relatório

 * Armazenar relatórios de usuário
 * Fornecer relatórios ao usuário

### 5.3 Recursos adicionais

 * Fornecer informações relevantes para o cuidado da saúde
 
## **6. Restrições**

### 6.1 Restrições de Implementação

O ChatBot será desenvolvido utilizando a linguagem de programação Python e implementado com a API disponibilizada para o <i>Telegram</i>.
 
### 6.2 Restrições de Design

A interação com o ChatBot se dá de forma simples, espontânea e de fácil entendimento, dentro da interface do aplicativo ou site do <i>Telegram</i>.
 
### 6.3 Restrições de Uso

Para interagir com o ChatBot se faz necessário utilizar um dispositivo que tenha conexão com a Internet, além de acesso ao <i>Telegram</i>
 
### 6.4 Restrições Externas

Falta de conhecimento e de experiência em relação à API de ChatBot do <i>Telegram</i> e possíveis complicações relacionadas ao trabalho em equipe.
 
### 6.5 Restrições de Confiabilidade

Cada uma das funcionalidades implementadas deve passar por testes que garantam o funcionamento correto e a estabilidade da mesma.
