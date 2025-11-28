# 📚 Documentação Complementar da Disciplina

## *Sistema de Gestão Farmacêutica – Versão 2.0*

---

# 🏗 1. Projeto – Aplicação CRUD

Este sistema implementa operações *CRUD completas* para medicamentos e laboratórios, utilizando Python e estruturas de dados baseadas em listas e dicionários.

### *Funcionalidades implementadas*

* *Create*

  * Cadastrar medicamentos
  * Cadastrar novos laboratórios implicitamente ao criar medicamentos
* *Read*

  * Listar laboratórios
  * Listar medicamentos por urgência
  * Gerar relatórios por categoria
* *Update*

  * Editar nome de laboratório
* *Delete*

  * Excluir laboratório (e seus medicamentos)
  * Excluir medicamento individual

### *Estrutura de Dados Usada*

python
medicamentos: List[Dict[str, str]] = [
    {
        "nome": "...",
        "apresentacao": "...",
        "laboratorio": "...",
        "quantidade": int,
        "urgencia": "verde/amarelo/vermelho"
    }
]


---

# 🧠 2. Pseudocódigo do Sistema

## *Função cadastrar_medicamentos()*


enquanto verdadeiro:
    exibe cabeçalho
    nome ← ler entrada do usuário
    se nome == "voltar": sair do loop

    se nome vazio: mostrar erro e continuar

    apresentação ← ler
    laboratório ← ler
    se algum estiver vazio: erro e continuar

    repetir até quantidade válida:
        ler quantidade
        se número e > 0: ok
        senão: erro

    repetir até urgência válida:
        ler urgência
        se urgência ∈ {verde, amarelo, vermelho}: ok
        senão: erro

    se medicamento já existe (mesmo nome + laboratório):
        erro e continuar

    criar dicionário com os dados
    adicionar à lista

    perguntar se deseja continuar
    se não: sair


---

## *Função listar_laboratorios()*


extrair laboratório de cada medicamento
usar conjunto para remover duplicados
ordenar alfabeticamente
retornar lista


---

## *Função editar_laboratorio()*


labs ← listar_laboratorios
se vazio: erro

mostrar lista com índices

opção ← ler número
validar índice

novo_nome ← ler
validar que não é vazio e não duplica outro laboratório

confirmar alteração
se confirmar:
    para cada medicamento:
        se laboratório == lab_antigo:
            atualizar para novo_nome
mostrar sucesso


---

## *Função deletar_laboratorio()*


labs ← listar_laboratorios
se vazio: erro

mostrar lista com índices
opção ← ler número
validar

coletar medicamentos pertencentes ao laboratório escolhido
exibir alerta e lista dos itens que serão apagados

usuário precisa digitar "CONFIRMAR"
se confirmado:
    remover todos medicamentos do laboratório
mostrar sucesso


---

## *Função deletar_medicamento()*


se lista estiver vazia: erro

listar medicamentos com índice

opção ← ler número
validar índice

confirmar remoção
se sim:
    remover item da lista
mostrar sucesso


---

## *Função gerar_listas()*


se lista vazia: erro

filtrar medicamentos em:
    vermelhos
    amarelos
    verdes

função auxiliar: agrupar_por_laboratorio(lista):
    criar dicionário
    para cada medicamento:
        adicionar em sua chave de laboratório
    retornar dicionário

imprimir listas formatadas:
    vermelhos agrupados
    amarelos agrupados
    verdes agrupados

calcular estatísticas:
    total por urgência
    total geral
    total de laboratórios


---

# 🔄 3. Fluxograma (Markdown + ASCII)

---

## *Fluxo Geral do Sistema*


          ┌──────────────────────┐
          │  Início do Sistema   │
          └─────────┬────────────┘
                    │
                    ▼
          ┌──────────────────────┐
          │ Mostrar Menu Principal│
          └───────┬──────────────┘
                  │
 ┌────────────────┼──────────────────────┐
 │                │                      │
 ▼                ▼                      ▼
1 - Cadastrar   2 - Gerar listas      3 - Editar lab
 │                │                      │
 ▼                ▼                      ▼
Função           Função                 Função
cadastrar()      gerar_listas()         editar_laboratório()

 ┌────────────────┼──────────────────────────────────────────┐
 │                │                                          │
 ▼                ▼                                          ▼
4 - Deletar lab  5 - Listar labs                         6 - Deletar med
 │                │                                          │
 ▼                ▼                                          ▼
Função           listar_laboratórios()                  deletar_medicamento()
deletar_laboratório()

                    ▼
          ┌──────────────────────┐
          │  Sair do Sistema     │
          └──────────────────────┘


---

# 📝 4. Especificação em Linguagem Algorítmica (Português Estruturado)

## *Algoritmo Principal*


Algoritmo SistemaDeGestaoFarmaceutica
    medicamentos ← lista vazia

    Enquanto verdadeiro faça
        MostrarMenuPrincipal()

        Leia opcao

        Se opcao = "1" então
            cadastrar_medicamentos(medicamentos)

        Senão se opcao = "2" então
            gerar_listas(medicamentos)

        Senão se opcao = "3" então
            editar_laboratorio(medicamentos)

        Senão se opcao = "4" então
            deletar_laboratorio(medicamentos)

        Senão se opcao = "5" então
            listar_laboratorios(medicamentos)

        Senão se opcao = "6" então
            deletar_medicamento(medicamentos)

        Senão se opcao = "7" então
            Pare

    FimEnquanto
FimAlgoritmo


---
