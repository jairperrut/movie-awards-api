# Documentação da API Movie Awards

## Visão Geral

A aplicação Movie Awards é uma API desenvolvida para processar e exibir informações relacionadas à categoria de "Pior Filme" do Golden Raspberry Awards. Ela segue os princípios de **Domain-Driven Design (DDD)** e **Clean Architecture**, promovendo manutenção e escalabilidade.

## Tecnologias Utilizadas

- **FastAPI**: Framework para desenvolvimento de APIs.
- **SQLModel**: ORM baseado em SQLAlchemy e Pydantic.
- **SQLite**: Banco de dados utilizado para armazenamento local.
- **Docker**: Containerização para execução da aplicação.
- **Docker Compose**: Orquestração dos containers.
- **Makefile**: Automatização de comandos recorrentes.

## Decisões de Design

### Clean Architecture

A aplicação está estruturada para separar as camadas de:

- **Aplicação**: Contém os casos de uso (interações principais).
- **Domínio**: Define as regras de negócio e entidades.
- **Infraestrutura**: Implementações específicas, como integrações com banco de dados.

Essa abordagem garante:

- Baixo acoplamento entre módulos.
- Facilidade de troca de tecnologias (ex.: mudança de banco de dados).
- Testabilidade, pois as regras de negócio não dependem de implementações externas.

### Banco de Dados

Utilização do SQLite como banco local. As tabelas são criadas automaticamente no startup da aplicação.

### Carregamento Inicial

Um arquivo `movielist.csv` é processado na inicialização para popular o banco com dados dos vencedores e indicados.

## Execução

Para executar a aplicação utilizando Docker Compose:

1. Certifique-se de ter o Docker e o Docker Compose instalados.
2. O arquivo `.env` contém as variáveis de configuração da aplicação. Edite se necessário (exemplo de variável: `DB_ECHO=false`).
3. Execute o comando:

```bash
docker-compose up api
```

A aplicação estará disponível em [http://localhost:8000](http://localhost:8000).
A documentação dos endpoints estará disponível em [http://localhost:8000/docs](http://localhost:8000/docs).


### Alterando a Porta

Caso a porta `8000` esteja em uso, edite o arquivo `docker-compose.yaml` e modifique o mapeamento da porta:

```yaml
ports:
  - "<nova_porta>:8000"
```

Substitua `<nova_porta>` pelo número desejado e execute novamente o comando `docker-compose up`.

## Endpoints Principais

### 1. **`GET /awards/interval`**

Retorna os intervalos máximo e mínimo entre vitórias de produtores.

#### Exemplo de Resposta:

```json
{
  "min": [
    {"producer": "Producer A", "interval": 2, "previousWin": 2015, "followingWin": 2017}
  ],
  "max": [
    {"producer": "Producer B", "interval": 13, "previousWin": 2002, "followingWin": 2015}
  ]
}
```

## Testes

A aplicação inclui testes de integração para validar o comportamento dos casos de uso.
Para executar os testes:

```bash
docker-compose up tests
```

Os testes garantem a corretude das funcionalidades, como o cálculo dos intervalos entre vitórias de produtores.

## Considerações Finais

Essa aplicação foi projetada para ser extensível e de fácil manutenção. Caso precise adicionar novas funcionalidades, siga os princípios de separação de responsabilidades descritos neste documento.
