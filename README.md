# Exercício — Integração Python e MySQL (Floricultura)

## Objetivo

O objetivo deste exercício é desenvolver uma aplicação em Python integrada a um banco de dados MySQL, utilizando o padrão DAO (Data Access Object) para realizar operações de manipulação e consulta de dados.

O banco de dados `floricultura` armazena informações sobre plantas disponíveis para venda.

## Tecnologias utilizadas

- Python
- MySQL
- mysql-connector-python

## Estrutura do projeto

```text
Exercicio-C07-Aula11/
│
├── floricultura.sql
├── README.md
│
└── python/
    ├── connection_dao.py
    ├── planta_dao.py
    ├── main.py
    └── requirements.txt
```

## Funcionalidades implementadas

No arquivo `planta_dao.py`, foram implementadas seis funções:

1. **inserir_planta:** cadastra uma nova planta e retorna o ID gerado pelo banco.
2. **listar_plantas:** consulta todas as plantas cadastradas, ordenadas pelo ID.
3. **buscar_por_especie:** busca as plantas de acordo com a espécie informada.
4. **atualizar_preco:** atualiza o preço de uma planta utilizando seu ID.
5. **remover_planta:** remove uma planta pelo ID informado.
6. **valor_total_estoque:** calcula o valor total do estoque, multiplicando o preço pela quantidade disponível de cada planta.

As operações utilizam parâmetros SQL para evitar SQL Injection. Também foram utilizados `commit()`, `rollback()` e `finally` para controlar as transações e fechar as conexões com o banco de dados.

## Como executar

### 1. Configurar o banco de dados

Abra o MySQL Workbench e execute o arquivo `floricultura.sql`. Ele cria o banco de dados, a tabela `planta` e insere os cinco registros iniciais.

### 2. Configurar a conexão

Verifique os dados de acesso ao MySQL no arquivo `python/connection_dao.py`, ajustando a senha conforme sua configuração local.

### 3. Instalar as dependências

No terminal, acesse a pasta `python` e execute:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 4. Executar a aplicação

Ainda dentro da pasta `python`, execute:

```bash
python main.py
```

O programa realizará automaticamente as operações implementadas e apresentará os resultados no terminal.

**Observação:** para repetir a execução com os mesmos resultados esperados, execute novamente o arquivo `floricultura.sql` no MySQL Workbench antes de rodar o programa. Isso recria o banco com os cinco registros iniciais.

---