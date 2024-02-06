
# Sistema de Cadastro de Tarefas

O Sistema de Cadastro de Tarefas é uma aplicação simples e eficaz para gerenciar tarefas diárias. Com ele, os usuários podem criar, atualizar, visualizar e excluir tarefas, facilitando a organização e o controle do tempo e das responsabilidades.


## Stacks Utilizadas

- Python
- Flask: Um framework web para Python, para construir a aplicação.
- Werkzeug: Uma biblioteca de utilitários para lidar com requisições HTTP.
- Requests: Uma biblioteca para fazer requisições HTTP em Python. 
 

## Instalação

1. Certifique-se de ter o Python instalado em seu sistema a partir da versão 3.11.5 64bit ou superior.
2. Clone esse repositório.
3. Abra seu terminal e navegue até o diretório onde o arquivo foi baixado.
4. Instale as dependências necessárias com o comando `pip3 install -r requirements.txt`.
5. Execute o arquivo: `app.py` no seu IDE ou Editor de código-fonte de sua preferência para iniciar o jogo.

    
## Estrutura do Sistema

- O projeto é organizado em um único arquivo principal, `app.py`, que contém a lógica da aplicação Flask. Além disso, há um diretório `models` que contém o arquivo `task.py`, definindo a classe `Task` e seus métodos associados.

- As tarefas são armazenadas em uma lista global chamada `tasks`. Cada tarefa é representada por uma instância da classe `Task`, que possui atributos como `Id`, `Title`, `Description` e `Completed`. O Id das tarefas é gerado sequencialmente, começando em  1.

- O sistema não está utilizando um banco de dados para persistir as tarefas. Em vez disso, as tarefas são armazenadas na memória durante a execução da aplicação. Isso significa que, ao reiniciar a aplicação, todas as tarefas serão perdidas.


## Aprendizados

- A cada novo projeto proposto pela Rocketseat sempre há novos aprendizados e desafios, focados em nos levar a pensar fora da caixa e com isso sempre aprimorando cada vez mais o meu conhecimento adquirido em desenvolvimento FullStack.

- **Práticas de Programação Orientada a Objetos (POO)**: Trabalhei com conceitos de POO onde criei uma classe principal, chamada Task, usada para representar a tarefa e isso envolveu: `Definição de métodos dentro da classe`, `Definição de construtores para inicializar objetos.`.

- **Desenvolvimento com Flask**: Aprendi a criar uma aplicação básica usando o Flask, um microframework para Python. Isso inclui: `Configuração de rotas e métodos HTTP`, `Manipulação de requisições e respostas JSON`. 
    

- **Modelagem de Dados**: Aprendi a criação de modelo de dados para representar tarefas e isso envolveu: `Definição de classes e atribuitos`, `Conversão de objetos para dicionários para serialização em JSON`.

- **Listas e Dicionários**: Aprimorei meu entendimento em manipular listas e dicionários, que são estruturas de dados fundamentais e isso inclui: `Adição e remoção de elementos na lista`, `Atribuição e recuperação de valores em dicionários`.






