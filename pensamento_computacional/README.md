# 🐍 Projetos Python: Lista de Compras e Calculadora Simples

Dois projetos desenvolvidos para praticar conceitos fundamentais de Python, incluindo estruturas de controle, manipulação de dados, e interação com o usuário.

---

## 📋 Descrição

### 1. **Lista de Compras**
Um sistema para gerenciar produtos em uma lista de compras, com persistência de dados em JSON.  
**Funcionalidades:**
- Adicionar/Remover produtos
- Pesquisar por nome
- Listagem automática com IDs únicos
- Tratamento de erros

### 2. **Calculadora Simples**
Uma calculadora de operações básicas com interface via terminal.  
**Operações:**
- Soma, Subtração, Multiplicação, Divisão
- Tratamento de divisão por zero

---

## ⚙️ Pré-requisitos
- Python 3.6 ou superior

---

## 📂 Estrutura do Repositório
```
.
├── lista_de_compras.py           # Sistema de lista de compras com persistência em JSON
├── desafio_calculadora.py        # Calculadora com operações básicas
└── README.md                     # Documentação do projeto
```

---

## 🚀 Como Usar

### Lista de Compras
```bash
python lista_de_compras.py
```
**Comandos disponíveis:**  
- `A`: Adicionar produto (nome, unidade, quantidade, descrição)
- `B`: Remover produto por ID
- `C`: Pesquisar produtos por nome
- `D`: Sair do programa

### Calculadora
```bash
python desafio_calculadora.py
```
**Operações:**  
- `1-4`: Seleção de operações matemáticas
- `s`: Sair do programa

---

## 🛠️ Funcionalidades Detalhadas

### 🛒 Lista de Compras
- **Persistência em JSON:** Dados salvos automaticamente em `lista_de_compras.json`
- **Validações:**  
  - Nome não pode ser vazio
  - IDs únicos e autoincrementáveis
  - Unidades de medida pré-definidas
- **Interface intuitiva:** Lista de produtos exibida automaticamente ao abrir o menu
- **Loop contínuo:** Permite múltiplas operações até o usuário sair

### ➗ Calculadora
- **Tratamento de erros:**  
  - Entradas numéricas validadas
  - Bloqueio de divisão por zero
- **Loop contínuo:** Permite múltiplas operações até o usuário sair

---

## 🧰 Tecnologias Utilizadas
- Python 3
- Módulo `json` para persistência de dados (Lista de Compras)

---
**Desenvolvido como parte da trilha de Pensamento Computacional** 🚀
```
