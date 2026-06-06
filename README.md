# 🤖 Chatbot com IA, Ferramentas e WhatsApp

## 📌 Sobre o Projeto

Este projeto consiste no desenvolvimento de um chatbot inteligente utilizando Inteligência Artificial, capaz de responder perguntas, consultar informações externas e manter contexto das conversas.

A aplicação será construída com FastAPI e seguirá uma arquitetura modular, permitindo a adição de novas funcionalidades de forma simples e escalável.

O objetivo é criar um assistente virtual capaz de:

* Conversar com usuários utilizando IA.
* Consultar dados externos em tempo real.
* Utilizar ferramentas especializadas.
* Manter memória das conversas.
* Integrar-se ao WhatsApp.
* Armazenar informações em banco de dados.

---

# 🚀 Funcionalidades

## ✅ Chat com IA

O usuário envia uma mensagem e recebe uma resposta gerada por um modelo de Inteligência Artificial.

Exemplo:

Usuário:

> Qual a capital da Argentina?

Resposta:

> A capital da Argentina é Buenos Aires.

---

## 🌤 Consulta de Clima

Permite consultar a previsão do tempo de uma cidade.

Exemplo:

> Como está o clima em Belo Horizonte?

---

## 💵 Cotação do Dólar

Consulta o valor atualizado do dólar.

Exemplo:

> Qual a cotação do dólar hoje?

---

## ₿ Cotação do Bitcoin

Consulta o preço atualizado do Bitcoin.

Exemplo:

> Quanto está o Bitcoin agora?

---

## 🌐 Busca na Internet

Permite que a IA consulte fontes externas para responder perguntas que exigem informações atualizadas.

Exemplo:

> Quem venceu a última final da Libertadores?

---

## 🧠 Memória Conversacional

O sistema salva o histórico de mensagens para permitir respostas contextualizadas.

Exemplo:

Usuário:

> Meu nome é João.

Usuário:

> Qual é o meu nome?

Resposta:

> Seu nome é João.

---

## 📱 Integração com WhatsApp

Recebe mensagens diretamente do WhatsApp e responde automaticamente utilizando a IA.

Fluxo:

WhatsApp → API → IA → Resposta

---

# 🏗 Arquitetura do Sistema

```text
Usuário
   ↓
FastAPI
   ↓
IA
   ↓
Ferramentas
 ├─ Clima
 ├─ Dólar
 ├─ Bitcoin
 └─ Busca Web
   ↓
Banco de Dados
   ↓
Resposta
```

---

# 🛠 Tecnologias Utilizadas

## Backend

* Python
* FastAPI
* SQLAlchemy
* Pydantic
* Uvicorn

## Banco de Dados

* MySQL

## Inteligência Artificial

* OpenAI API

## Integrações

* WhatsApp Cloud API
* APIs externas de clima
* APIs de cotação financeira

---

# 📂 Estrutura do Projeto

```text
chat_bot/
│
├── app/
│   ├── api/
│   ├── services/
│   ├── models/
│   ├── schemas/
│   ├── database/
│
│
├── .env
├── requirements.txt
├── main.py
└── README.md
```

---

# 🔄 Fluxo de Funcionamento

## Conversa Simples

```text
Usuário
   ↓
API
   ↓
IA
   ↓
Resposta
```

---

## Uso de Ferramentas

```text
Usuário
   ↓
IA
   ↓
Ferramenta
   ↓
Resultado
   ↓
IA
   ↓
Resposta
```

---

## Conversa com Memória

```text
Usuário
   ↓
API
   ↓
Banco de Dados
   ↓
Histórico
   ↓
IA
   ↓
Resposta
```

---

# 🗄 Banco de Dados

O sistema armazenará:

* Usuários
* Conversas
* Mensagens
* Histórico
* Configurações

Exemplo:

## Usuário

```json
{
  "id": 1,
  "name": "João",
  "email": "joao@email.com"
}
```

## Mensagem

```json
{
  "id": 15,
  "user_id": 1,
  "role": "user",
  "content": "Qual a cotação do dólar?"
}
```

---

# 🔐 Segurança

O projeto seguirá boas práticas de segurança:

* Criptografia de dados sensíveis.
* Variáveis de ambiente.
* JWT para autenticação.
* Controle de acesso.
* Validação de entradas.

---

# 🧪 Testes

Serão implementados testes para:

* Rotas da API.
* Serviços.
* Ferramentas.
* Banco de dados.
* Fluxos de autenticação.

Tecnologias:

* Pytest
* HTTPX

---

# 📈 Melhorias Futuras

* Sistema de usuários.
* Dashboard administrativo.
* Integração com Telegram.
* Integração com Discord.
* Upload de arquivos.
* Suporte a imagens.
* RAG com documentos.
* Vetorização de conhecimento.
* Múltiplos modelos de IA.

---

# 🎯 Objetivo de Aprendizado

Este projeto tem como objetivo praticar:

* Arquitetura de APIs.
* FastAPI.
* SQLAlchemy.
* Banco de dados relacionais.
* Integração com APIs externas.
* Inteligência Artificial.
* Engenharia de Software.
* Clean Code.
* Boas práticas de desenvolvimento.
* Desenvolvimento de projetos reais para portfólio.

---

# 👨‍💻 Autor

Desenvolvido como projeto de estudo para aprofundamento em desenvolvimento backend com Python, FastAPI e Inteligência Artificial.
