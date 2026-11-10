# Atividade 2 — API Flask em contêiner Docker

## Descrição da aplicação

API web simples feita em Python com Flask. Ela roda dentro de um contêiner Docker, escuta na porta 8000 e responde em JSON nestes endereços:

| Endereço | O que devolve |
| --- | --- |
| `/` | Mensagem de boas-vindas |
| `/health` | `{"status":"ok"}`, usado para saber se a aplicação está viva |
| `/soma?a=2&b=3` | A soma de `a` e `b`. Se faltar parâmetro ou não for número inteiro, devolve erro 400 |

## Estrutura do projeto

```text
atividade2-docker-ci/
├── app.py              # a aplicação Flask
├── requirements.txt    # bibliotecas da aplicação
├── Dockerfile          # instruções para construir a imagem
├── .dockerignore       # o que o Docker ignora no build
├── .gitignore          # o que o Git ignora
├── README.md           # este arquivo
└── docs/               # prints que comprovam o funcionamento
```

## Como construir a imagem (build)

```bash
docker build -t minha-api:1.0 .
```

## Como executar o contêiner (run)

```bash
docker run -d --name minha-api -p 8000:8000 minha-api:1.0
```

## Como verificar que está funcionando

Abra no navegador:

- http://localhost:8000/
- http://localhost:8000/health
- http://localhost:8000/soma?a=2&b=3

Ou veja os logs do contêiner:

```bash
docker logs minha-api
```

## Como parar e remover o contêiner

```bash
docker stop minha-api
docker rm minha-api
```

## Evidências do funcionamento

Aplicação respondendo no navegador:

![Aplicação respondendo no navegador](docs/evidencia-navegador.png)

Contêiner em execução:

![Contêiner em execução](docs/evidencia-terminal.png)