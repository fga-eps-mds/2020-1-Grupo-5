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
08/12|0.2.0|Revisão do documento|Lucas Rodrigues|

## **1. Introdução**

### 1.1 Propósito

Este documento tem o objetivo de apresentar uma visão geral sobre o Chatbot DoctorS, mostrando suas características e seu objetivo. Dessa forma, pretende-se esclarecer ao leitor diversos aspectos e detalhes sobre o projeto.

### 1.2 Escopo

O Chatbot DoctorS é um sistema desenvolvido para coletar informações do estado de saúde diariamente dos usuários. Assim, serve como outra plataforma para o usuário do aplicativo Guardiões da Saúde informar esses dados. Além disso, podem ser encontradas outras funcionaliades também presentes no aplicativo, como uma seção de dicas e notícias de saúde e histórico de relatos de saúde.

### 1.3 Definições, acrônimos e abreviações

- DoctorS: O nome do Chatbot
- Chatbot: <i>Software</i> que através de inteligência artificial conduz uma conversa para automatizar os processos
- FGA: Faculdade do Gama
- MDS: Equipe de Métodos de Desenvolvimento de <i>Software</i>
- <i>Telegram</i>: Aplicativo de mensagens instantâneas 
- UnB: Universidade de Brasília

### 1.4 Referências

- IBM Knowledge Center - Documento de Visão: A estrutura de tópicos do documento de visão. Disponível em https://www.ibm.com/support/knowledgecenter/pt-br/SSWMEQ_4.0.6/com.ibm.rational.rrm.help.doc/topics/r_vision_doc.html. Acesso em 01 set. 2020;
- Disponível em https://github.com/fga-eps-mds/2018.1_Gerencia_mais/blob/master/docs/documentos/Mds/Documento_de_Visao.md#1. Acesso em 01 set. 2020.
- Disponível em https://fga-eps-mds.github.io/2019.1-ADA/#/docs/product/vision_document. Acesso em 01 set. 2020.

### 1.5 Visão Geral

Esse é um documento informativo sobre o Chatbot DoctorS em que estão descritos os detalhes do <i>software</i>, explicando a razão de sua existência e descrevendo seus usuários.
Ele está organizado no formato de tópicos e subtópicos sequenciais numerados. A ordem desses tópicos é: Introdução; Posicionamento; Descrições da Parte Interessada e do Usuário; Visão Geral do Produto; Recursos do Produto; Restrições; Outros Requisitos do Produto.

## **2. Posicionamento**

### 2.1 Oportunidade de Negócios

O aplicativo Guardiões da Saúde é de extrema importância para a obtenção de informações sobre como está a saúde das pessoas nesse tempo de pandemia. O nosso projeto pretende facilitar e expandir essa comunicação já presente no aplicativo Guardiões da Saúde ao maior número de pessoas possível, utilizando o Telegram, uma rede social que é de comum uso também entre os membros da nossa comunidade. Além disso, expandindo suas funcionalidades para o *Telegram*, é possível reduzir a quantidade de dias que a pessoa esquece de fornecer seu relato de saúde e deixar a interação desse usuário com o serviço mais amigável.

### 2.2 Descrição do problema

|**O problema é**|Falta de acesso ao aplicativo Guardiões da Saúde.|
|:---:|:---:|
|**afeta**|Instituições que utilizam os dados obtidos pelo app.|
|**cujo impacto é**|Dificuldade, por meio das autoridades públicas, no planejamento do combate a pandemia.|
|**uma boa solução seria**|O uso do Chatbot para facilitar a comunicação e obtenção de dados.|

### 2.3 Instrução de Posição do Produto

|**Para** |Usuários do app <i>Telegram</i>.|
|:---:|:---:|
|**Que** |Querem relatar e receber relatórios sobre saúde|
|**O DoctorS_bot é**| Um Chatbot integrado ao <i>Telegram</i>.|
|**Que**| Obtém relatos de saúde dos usuários.|
|**Diferente de**|Precisar utilizar o aplicativo Guardiões da Saúde.|
|**Nosso produto**|Utiliza o <i>Telegram</i> para que seja feito o relato de saúde do usuário.|

## **3. Descrições da Parte Interessada e do Usuário**

Nome|Descrição|Responsabilidade
|:--:|:--:|:--:|
| Equipe de Desenvolvimento | Estudantes da disciplina Métodos de Desenvolvimento de <i>Software</i> da Universidade de Brasília Campus Gama | Desenvolvimento, documentação, implementação e testes do <i>software</i> solicitado. |
| Professor e Professora | Professor da disciplina de Métodos de Desenvolvimento de <i>Software</i> e a professora da disciplina de Engenharia de Produto de <i>Software</i>, ambos da Universidade de Brasília Campus Gama | Avaliar e orientar os estudantes de ambas as disciplinas respectivamente. |


### 3.1 Resumo dos Usuários

Nome|Descrição
|:-:|:-:|
| Monitorado | Usuário que quer relatar o seu estado de saúde para contribuir com os relatórios. |

### 3.2 Ambiente do Usuário

A aplicação será utilizada no mensageiro <i>Telegram</i>, que atende as plataformas <i>mobile</i> e <i>web</i>.

### 3.3 Perfis dos Envolvidos

#### 3.3.1 Equipe de Desenvolvimento

Representante|Gabriel Batalha, João Alves, João Pedro, Kevin, Lucas, Marcos Adriano.
|:-:|:-:|
|**Descrição**|Desenvolvedores.|
|**Tipo**|Estudantes da Universidade de Brasília, cursando a disciplina de Métodos de Desenvolvimento de Software.|
|**Responsabilidade**|Desenvolvimento, Testes, Documentação e Implementação do <i>software</i>.|
|**Critérios de Sucesso**|Finalizar o desenvolvimento e realizar a entrega do <i>software</i> dentro dos prazos.|
|**Envolvimento**|Alto.|
|**Problemas/Comentários**|Alguns integrantes da equipe são inexperientes nas linguagens de programação utilizadas no desenvolvimento, no padrão arquitetural e nas metodologias de desenvolvimento.|


### 3.4 Perfis dos Usuários

#### 3.4.1 Monitorado
Representante|Monitorado
|:-:|:-:|
|**Descrição**|Monitoramento da saúde de pessoas, sobretudo durante a pandemia.|
|**Tipo**|Monitorado.|
|**Responsabilidade**| Utilizar o aparelho para o propósito.|
|**Critérios de Sucesso**| Permanência da saúde.|
|**Envolvimento**|Médio.|
|**Problemas/Comentários**| - |


### 3.5 Principais Necessidades dos Usuários ou dos Envolvidos

Necessidade|Prioridade|Interesse|Solução Atual|Solução Proposta
|:-:|:-:|:-:|:-:|:-:|
|Auxiliar no relato da saúde do usuário.|Alta|Tornar a coleta de estado de saúde dos usuários mais fácil e dinâmica.|Monitoramento contínuo.|Aplicação que, por meio de um mensageiro, fará o report diário da saúde do usuário.|

### 3.6 Alternativas e Concorrência

A proposta é garantir as funcionalidades de um aplicativo que já se encontra no mercado, e é justificada por associar que os usuários em geral terão uma maior aceitação da ideia se este já estiver inserido no contexto dos mesmos, que no caso é o mensageiro <i>Telegram</i>.

## **4. Visão Geral do Produto**

### 4.1 Perspectiva do Produto
O produto tem como objetivo estender para o <i>Telegram</i> as funcionalidades do aplicativo <i>mobile</i> Guardiões da Saúde, utilizando um Chatbot. Os usuários cadastrados devem responder diariamente à uma pergunta sobre o aparecimento ou não de sintomas relacionados ao COVID-19. A integração com o aplicativo Guardiões da Saúde poderá ajudar na geração dos relatórios contendo estatísticas e dados relacionados a esse problema. Dessa forma, ele pode auxiliar no combate à doença e expandir o alcance e o acesso ao Guardiões da Saúde.

 ### 4.2 Resumo das Capacidades
 
 | **Benefícios para o Cliente**                                 | **Recursos de suporte**                    |
 |---------------------------------------------------------------|--------------------------------------------|
 | Acesso às próprias informações                                | Criação de usuário                         |
 | Capacidade de oferecer informações para o mapeamento de saúde | Informe de estado físico diário               |
 | Acesso à notícias sobre saúde                                 | Informações sobre a pandemia |
 | Acesso à dicas para cuidar da saúde                           | Dicas e práticas saudáveis                 |
 
 ### 4.3 Suposições e Dependências
 - O usuário deve ter em alcance o aplicativo <i>Telegram</i>
 - O usuário deve estar conectado à internet

## **5. Recursos do Produto**

O produto possuirá o sistema de cadastro e login, armazenando os usuários e aceitando os relatos de saúde dos usuários com o intuito de facilitar o acesso ao Guardiões da Saúde.

### 5.1 Recursos de usuário
 
 * Cadastro e login de usuário
 * Informe de estado físico diário (quanto aos sintomas)
 * Acesso ao histórico de relatos
 * Acesso à dicas de saúde
 * Acesso à notícias sobre a pandemia

### 5.2 Recursos de relatório

 * Coleta de relatórios de saúde do usuário

### 5.3 Recursos adicionais

 * Fornecer informações relevantes para o cuidado da saúde por meio de dicas e notícias
 
## **6. Restrições**

### 6.1 Restrições de Implementação

O Chatbot será desenvolvido utilizando a linguagem de programação Python e implementado com a API disponibilizada para o <i>Telegram</i>.
 
### 6.2 Restrições de Design

A interação com o Chatbot se dá de forma simples, espontânea e de fácil entendimento, dentro da interface do aplicativo ou site do <i>Telegram</i>.
 
### 6.3 Restrições de Uso

Para interagir com o Chatbot se faz necessário utilizar um dispositivo que tenha conexão com a internet, além de acesso ao <i>Telegram</i>
 
### 6.4 Restrições Externas

Falta de conhecimento e de experiência em relação à API de Chatbot do <i>Telegram</i> e possíveis complicações relacionadas ao trabalho em equipe.
 
### 6.5 Restrições de Confiabilidade

Cada uma das funcionalidades implementadas deve passar por testes que garantam o funcionamento correto e a estabilidade da mesma.
