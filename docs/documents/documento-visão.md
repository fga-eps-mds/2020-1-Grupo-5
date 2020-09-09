# Histórico de Versões

Data|Versão|Descrição|Autor
-|-|-|-
x/08|0.1.0|Adição do template do Documento| X |
07/09|0.1.1|Adição dos subitens do item 3| Marcos Adriano|
08/09|0.1.2|Adição dos subitens do item 5| João Alves|
08/09|0.1.3|Adição dos subitens do item 6| Lucas Rodrigues|
08/09|0.1.4|Adição dos subitens 2 e 3 do item 4| Gabriel Batalha|
08/09|0.1.5|Adição do subitem 1 do item 4| Lucas Rodrigues|
08/09|0.1.6|Adição dos subitens do item 2| João Pedro|

## **1. Introdução**

 - Propósito:
 - Escopo:
 - Definições, acrônimos e abreviações:
 - Referências: 
 - Visão geral:

## **2. Posicionando**

##### 2.1 <a name="2_1">Oportunidade de Negócio</a>

<p align="justify">&emsp;&emsp; O aplicativo Guardiões da Saúde é de extrema importância para obter informações de como está a saúde das pessoas em nossa comunidade neste tempo de pandemia. O nosso projeto pretende facilitar e expandir essa comunicação ao maior número de pessoas possível, utilizando de uma rede social que é de comum uso entre os membros da nossa comunidade. </p>

##### 2.2 <a name="2_2">Descrição do problema</a>

|**O problema é**|Pouco acesso ao aplicativo Guardiões da Saúde.|
|:---:|:---:|
|**afeta**|Orgãos que utilizam dos dados obtidos pelo app.|
|**cujo impacto é**|Dificuldade, por meio das autoridades públicas, no planejamento do combate a pandemia.|
|**uma boa solução seria**|O uso do ChatBot para facilitar a comunicação e obtenção de dados.|

##### 2.3 <a name="2_3">Instrução de Posição do Produto</a>

|**Para** |Usuários do app <i>Telegram</i>.|
|:---:|:---:|
|**Que** ||
|**O DoctorS_bot é**| Um ChatBot integrado ao <i>Telegram</i>.|
|**Que**| Obtém dados dos usuários.|
|**Diferente de**||
|**Nosso produto**||

## **3. Descrições da Parte Interessada e do Usuário**

Nome|Descrição|Responsabilidade
|:--:|:--:|:--:|
| Equipe de Desenvolvimento | Estudantes da disciplina Métodos de Desenvolvimento de *Software* da Universidade de Brasília Campus Gama | Desenvolvimento, documentação, implementação e testes do *Software* solicitado. |
| Professor e Professora | Professor da disciplina de Métodos de Desenvolvimento de *Software* e a professora da disciplina de Engenharia de Produto de *Software* ambos da Universidade de Brasília Campus Gama | Avaliar e orientar os estudantes de ambas as disciplinas respectivamente. |


##### 3.1 <a name="3_1">Resumo dos Usuários</a>

Nome|Descrição
|:-:|:-:|
| Monitorado | <p align = "justify">Usuario que está tendo a saúde monitorada continuamente.</p> |

##### 3.2 <a name="3_2">Ambiente do Usuário</a>

<p align = "justify">A aplicação será utilizada no mensageiro Telegram, o mesmo atende as plataformas <i>mobile</i> e <i>web</i>.</p>

##### 3.3 <a name="3_3">Perfis dos Envolvidos</a>

###### 3.3.1 <a name="3_3_1">Equipe de Desenvolvimento</a>

Representante|<p align = "justify">Gabriel Batalha, João Alves, João Pedro, Kevin, Lucas, Marcos Adriano.</p>
|:-:|:-:|
|**Descrição**|Desenvolvedores.|
|**Tipo**|Estudantes da Universidade de Brasília, cursando a disciplina de Métodos de Desenvolvimento de Software.|
|**Responsabilidade**|Desenvolvimento, Testes, Documentação e Implementação do *software*.|
|**Critérios de Sucesso**|Finalizar o desenvolvimento e realizar a entrega do *software* dentro dos prazos.|
|**Envolvimento**|Alto.|
|**Problemas/Comentários**|Alguns integrantes da equipe são inexperientes nas linguagens de programação utilizadas no desenvolvimento, no padrão arquitetural e nas metodologias de desenvolvimento.|


##### 3.4 <a name="3_4">Perfis dos Usuários</a>

###### 3.4.1 <a name="3_5"> Monitorado </a>
Representante|Monitorado
|:-:|:-:|
|**Descrição**|Monitoramento da saúde de pessoas, sobretudo durante a pandemia.|
|**Tipo**|Monitorado.|
|**Responsabilidade**| Utilizar o aparelho para o propósito.|
|**Critérios de Sucesso**| Permanencia da saúde.|
|**Envolvimento**|Médio.|
|**Problemas/Comentários**| - |


##### 3.5 <a name="3_5">Principais Necessidades dos Usuários ou dos Envolvidos</a>

Necessidade|Prioridade|Interesse|Solução Atual|Solução Proposta
|:-:|:-:|:-:|:-:|:-:|
|Auxiliar na manutenção da saúde do usuario.|Alta|Tornar a manutenção da saúde mais fácil e dinâmica.|Monitoramento continuo.|Aplicação que, por meio de um mensageiro, fará o report diario da saúde do usuario.|

##### 3.6 <a name="3_6">Alternativas e Concorrência</a>

<p align = "justify"> &emsp;&emsp; A proposta é justamente garantir as funcionalidades de um aplicativo que já se encontra no mercado. E é justificada por associar que os usuarios em geral terão uma maior aceitação da ideia se este já estiver inserido no contexto dos mesmos, que no caso é o mensageiro <i>Telegram</i>.</p>

## **4. Visão Geral do Produto**

### 4.1 Perspectiva do Produto
O produto tem como objetivo estender para o Telegram as funcionalidades do aplicativo mobile Guardiões da Saúde, utilizando um chatbot. Os usuários cadastrados devem informar diariamente sobre o aparecimento ou não de sintomas relacionados ao COVID-19. Com as informações coletadas são gerados relatórios contendo estatísticas e dados relacionados a esse problema. Dessa forma, ele pode auxiliar no combate à doença.

 ### 4.2 Resumo das Capacidades
 
 | **Benefícios para o Cliente**                                 | **Recursos de suporte**                    |
 |---------------------------------------------------------------|--------------------------------------------|
 | Acesso às próprias informações                                | Criação de Usuário                         |
 | Capacidade de oferecer informações para o mapeamento de saúde | Informe estado físico diário               |
 | Acesso a relatórios de saúde                                  | Envio de relatórios produzidos pelo Bot    |
 | Acesso a dicas para cuidar da saúde                           | Dicas e práticas saudáveis                 |
 
 ### 4.3 Suposições e Dependências
 - O usuário deve ter em alcance o aplicativo **Telegram**
 - O usuário deve estar conectado à Internet



## **5. Recursos do Produto**

O produto possuirá o sistema de login, armazenando os usuários e informações únicas com o intuíto de armazenar e gerar relatórios quanto aos infectados em cada região.

### 5.1 Recursos de usuário
 
 * Cadastrar usário
 * Informe físico diário (Quanto aos sintomas)
 * Armazenar informações

### 5.2 Recursos de relatório

 * Armazenar relatórios de usuário
 * Fornecer relatórios ao usuário

### 5.3 Recursos adcionais

 * Fornecer informações relevantes para o cuidado da saúde
 
## **6. Restrições**

### 6.1 Restrições de Implementação
O chatbot será desenvolvido utilizando a linguagem de programação Python e implementado com a API disponibilizada para o Telegram.
 
### 6.2 Restrições de Design
A interação com o chatbot se dá de forma simples, espontânea e de fácil entendimento, dentro da interface do aplicativo ou site do Telegram.
 
### 6.3 Restrições de Uso
Para interagir com o chatbot se faz necessário utilizar um dispositivo que tenha conexão com a internet, além de acesso ao Telegram.
 
### 6.4 Restrições Externas
Falta de conhecimento e de experiência em relação a API de chatbot do Telegram e possíveis complicações relacionadas ao trabalho em equipe.
 
### 6.5 Restrições de Confiabilidade
Cada uma das funcionalidades implementadas deve passar por testes que garantam o funcionamento correto e a estabilidade da mesma.

## **7. Outros Requisitos do Produto**
