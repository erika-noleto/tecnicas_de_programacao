
# # 📘 **DOCUMENTAÇÃO COMPLEMENTAR – SISTEMA DE LISTA DE COMPRAS – FARMÁCIA**

---

# ## 📌 1. Projeto Desenvolvido com Aplicação CRUD

### **Descrição Geral**

O sistema gerencia medicamentos que precisam ser comprados pela farmácia, organizados por:

* Nome
* Apresentação
* Laboratório
* Quantidade
* Nível de urgência (verde, amarelo, vermelho)

O programa permite:

* **C**reate → Cadastrar medicamentos
* **R**ead → Listar laboratórios e gerar listas por urgência
* **U**pdate → Editar laboratório
* **D**elete → Excluir laboratório e excluir medicamentos

---

# ## 📌 2. Pseudocódigo do Sistema

A seguir, todo o funcionamento do sistema está descrito em **pseudocódigo**, de forma clara e padronizada.

---

## ### 🔷 **Função: cadastrar_medicamentos**

```
ENQUANTO verdadeiro
    Mostrar título "Cadastro"
    Ler nome
    SE nome == "voltar"
        SAIR do loop
    FIM SE

    Ler apresentação
    Ler laboratório

    REPETIR
        Ler quantidade
    ATÉ quantidade seja inteiro >= 0

    REPETIR
        Ler urgencia
    ATÉ urgencia esteja em {verde, amarelo, vermelho}

    Adicionar medicamento à lista
    Mostrar "Medicamente adicionado"
FIM ENQUANTO
```

---

## ### 🔷 **Função: listar_laboratorios**

```
Criar conjunto vazio laboratórios
PARA cada medicamento na lista
    Adicionar laboratório ao conjunto
ORDENAR conjunto
RETORNAR lista ordenada
```

---

## ### 🔷 **Função: editar_laboratorio**

```
labs ← listar_laboratorios
SE labs estiver vazio
    Mostrar "nenhum laboratório"
    RETORNAR

Mostrar lista numerada de laboratórios
Ler escolha do usuário

SE escolha for válida
    lab_antigo ← laboratório escolhido
    Ler novo_nome
    SE novo_nome não for vazio
        PARA cada medicamento
            SE medicamento.laboratorio == lab_antigo
                Trocar laboratório pelo novo_nome
        Mostrar "Laboratório alterado"
    SENÃO
        Mostrar "nome inválido"
SENÃO
    Mostrar "opção inválida"
```

---

## ### 🔷 **Função: deletar_laboratorio**

```
labs ← listar_laboratorios
SE labs estiver vazio
    Mostrar "nenhum laboratório"
    RETORNAR

Mostrar lista com quantidade de medicamentos por laboratório

Ler escolha
SE escolha válida
    lab_deletar ← laboratório escolhido
    Confirmar operação
    SE confirmado
        Remover todos medicamentos cujo laboratório == lab_deletar
        Mostrar "laboratório deletado"
    SENÃO
        Operação cancelada
SENÃO
    Mostrar "opção inválida"
```

---

## ### 🔷 **Função: deletar_medicamento**

```
SE lista de medicamentos estiver vazia
    Mostrar "nenhum medicamento"
    RETORNAR

Mostrar lista numerada de medicamentos
Ler escolha

SE escolha válida
    Confirmar remoção
    SE confirmado
        Remover medicamento escolhido
        Mostrar "removido"
    SENÃO
        Cancelado
SENÃO
    Mostrar "opção inválida"
```

---

## ### 🔷 **Função: gerar_listas**

```
Separar medicamentos por urgência:
    vermelhos, amarelos, verdes

Agrupar cada cor por laboratório

Para cada categoria:
    Mostrar título
    SE não houver medicamentos
        Mostrar "vazio"
    SENÃO
        Para cada laboratório
            Mostrar medicamentos e dados

Exibir resumo geral da lista
```

---

## ### 🔷 **Função principal (main)**

```
Criar lista vazia de medicamentos

Mostrar título inicial

ENQUANTO verdadeiro
    Mostrar menu
    Ler opção

    SE opção == 1 → cadastrar_medicamentos
    SENÃO SE opção == 2 → gerar_listas
    SENÃO SE opção == 3 → editar_laboratorio
    SENÃO SE opção == 4 → deletar_laboratorio
    SENÃO SE opção == 5 → listar_laboratorios
    SENÃO SE opção == 6 → SAIR
    SENÃO SE opção == 7 → deletar_medicamento
    SENÃO → Mostrar "inválido"
FIM ENQUANTO
```

---

# ## 📌 3. Fluxograma (em Markdown)

Representado em formato de fluxograma textual — aceito em trabalhos acadêmicos e PDFs.

---

## ### 🔷 **Fluxograma Geral do Sistema**

```
            ┌─────────────────────────┐
            │ Início do Programa       │
            └─────────────┬───────────┘
                          │
                ┌─────────▼───────────┐
                │ Exibe Menu Principal │
                └───────┬─────────────┘
                        │
        ┌───────────────┼─────────────────────────┐
        │               │                         │
   ┌────▼───┐     ┌─────▼─────┐          ┌────────▼──────┐
   │ Opção 1│     │ Opção 2    │          │ Opção 3        │
   │Cadastrar│    │Gerar Listas│          │Editar Lab      │
   └────┬────┘     └─────┬─────┘          └──────┬────────┘
        │                │                       │
        ▼                ▼                       ▼
Executa função   Exibe listas por urgência   Edita laboratório
        │                │                       │
        ├────────────────┼───────────────────────┤
        │                │                       │
        ▼                ▼                       ▼
   ┌────┴─────┐    ┌─────┴──────┐           ┌────┴─────┐
   │ Opção 4   │    │ Opção 5    │           │ Opção 7   │
   │Excluir Lab│    │Listar Labs │           │Excluir Med│
   └────┬──────┘    └─────┬──────┘           └────┬──────┘
        │                 │                     │
        └─────────────────┼─────────────────────┘
                          │
               ┌──────────▼─────────┐
               │ Opção 6 → Sair      │
               └──────────┬─────────┘
                          │
                   ┌──────▼───────┐
                   │ Encerrar     │
                   └──────────────┘
```

---

# ## 📌 4. Especificação em Linguagem Algorítmica

*(Estilo Portugol / Portugol Studio / Algoritmo Genérico)*

---

### **Algoritmo: SistemaFarmacia**

```
INÍCIO
    medicamentos ← lista vazia

    ESCREVA "Sistema de Lista de Compras"

    REPITA
        ESCREVA menu

        LEIA opcao

        CASO opcao SEJA
            1: chamar cadastrar_medicamentos
            2: chamar gerar_listas
            3: chamar editar_laboratorio
            4: chamar deletar_laboratorio
            5: mostrar laboratórios cadastrados
            6: ENCERRAR
            7: chamar deletar_medicamento
            OUTRO: ESCREVER "opção inválida"
        FIM CASO
    ATÉ opcao == 6
FIM
