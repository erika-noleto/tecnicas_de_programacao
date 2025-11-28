from typing import List, Dict


def cadastrar_medicamentos(medicamentos: List[Dict[str, str]]) -> None:
    """Cadastrar medicamentos interativamente."""
    while True:
        print("\n--- CADASTRO DE MEDICAMENTOS ---")
        nome = input("Nome do medicamento (ou 'voltar' para menu): ").strip()
        if nome.lower() == 'voltar':
            break

        apresentacao = input("Apresentação: ").strip()
        laboratorio = input("Laboratório: ").strip()

        # Validação simples para quantidade (inteiro positivo)
        while True:
            quantidade = input("Quantidade: ").strip()
            if quantidade.isdigit() and int(quantidade) >= 0:
                break
            print("❌ Digite um número inteiro válido para quantidade.")

        # Urgência com validação
        while True:
            urgencia = input("Urgência (verde/amarelo/vermelho): ").strip().lower()
            if urgencia in ['verde', 'amarelo', 'vermelho']:
                break
            print("❌ Por favor, digite apenas: verde, amarelo ou vermelho")

        medicamentos.append({
            'nome': nome,
            'apresentacao': apresentacao,
            'laboratorio': laboratorio,
            'quantidade': quantidade,
            'urgencia': urgencia
        })
        print("✅ Medicamento adicionado com sucesso!")


def listar_laboratorios(medicamentos: List[Dict[str, str]]) -> List[str]:
    """Retorna lista ordenada de laboratórios cadastrados (sem repetição)."""
    laboratorios = {med['laboratorio'] for med in medicamentos}
    return sorted(laboratorios)


def editar_laboratorio(medicamentos: List[Dict[str, str]]) -> None:
    """Editar o nome de um laboratório e atualizar os medicamentos."""
    labs = listar_laboratorios(medicamentos)
    if not labs:
        print("❌ Nenhum laboratório cadastrado.")
        return

    print("\n--- EDITAR LABORATÓRIO ---")
    print("Laboratórios cadastrados:")
    for i, lab in enumerate(labs, 1):
        print(f"{i}. {lab}")

    try:
        opcao = int(input("\nNúmero do laboratório a editar: ")) - 1
        if 0 <= opcao < len(labs):
            lab_antigo = labs[opcao]
            novo_nome = input(f"Novo nome para '{lab_antigo}': ").strip()
            if novo_nome:
                for med in medicamentos:
                    if med['laboratorio'] == lab_antigo:
                        med['laboratorio'] = novo_nome
                print(f"✅ Laboratório '{lab_antigo}' alterado para '{novo_nome}'")
            else:
                print("❌ Nome inválido.")
        else:
            print("❌ Opção inválida.")
    except ValueError:
        print("❌ Por favor, digite um número válido.")


def deletar_laboratorio(medicamentos: List[Dict[str, str]]) -> None:
    """Deleta um laboratório e todos os medicamentos associados."""
    labs = listar_laboratorios(medicamentos)
    if not labs:
        print("❌ Nenhum laboratório cadastrado.")
        return

    print("\n--- DELETAR LABORATÓRIO ---")
    print("Laboratórios cadastrados:")
    for i, lab in enumerate(labs, 1):
        count = sum(1 for med in medicamentos if med['laboratorio'] == lab)
        print(f"{i}. {lab} ({count} medicamento(s))")

    try:
        opcao = int(input("\nNúmero do laboratório a deletar: ")) - 1
        if 0 <= opcao < len(labs):
            lab_deletar = labs[opcao]
            confirmar = input(f"Tem certeza que deseja deletar '{lab_deletar}'? (s/n): ").strip().lower()
            if confirmar == 's':
                medicamentos[:] = [med for med in medicamentos if med['laboratorio'] != lab_deletar]
                print(f"✅ Laboratório '{lab_deletar}' e todos os seus medicamentos foram removidos.")
            else:
                print("❌ Operação cancelada.")
        else:
            print("❌ Opção inválida.")
    except ValueError:
        print("❌ Por favor, digite um número válido.")


def deletar_medicamento(medicamentos: List[Dict[str, str]]) -> None:
    """Deleta um único medicamento do sistema."""
    if not medicamentos:
        print("❌ Nenhum medicamento cadastrado.")
        return

    print("\n--- DELETAR MEDICAMENTO ---")
    print("Medicamentos cadastrados:")

    for i, med in enumerate(medicamentos, 1):
        print(f"{i}. {med['nome']} ({med['laboratorio']}) - urgência: {med['urgencia']}")

    try:
        opcao = int(input("\nNúmero do medicamento a deletar: ")) - 1

        if 0 <= opcao < len(medicamentos):
            med = medicamentos[opcao]
            confirmar = input(
                f"Tem certeza que deseja remover '{med['nome']}' do laboratório '{med['laboratorio']}'? (s/n): "
            ).strip().lower()

            if confirmar == 's':
                medicamentos.pop(opcao)
                print("✅ Medicamento removido com sucesso!")
            else:
                print("❌ Operação cancelada.")
        else:
            print("❌ Opção inválida.")

    except ValueError:
        print("❌ Por favor, digite um número válido.")


def gerar_listas(medicamentos: List[Dict[str, str]]) -> None:
    """Gera e exibe listas agrupadas por urgência e por laboratório."""
    if not medicamentos:
        print("❌ Nenhum medicamento cadastrado.")
        return

    vermelhos = [med for med in medicamentos if med['urgencia'] == 'vermelho']
    amarelos = [med for med in medicamentos if med['urgencia'] == 'amarelo']
    verdes = [med for med in medicamentos if med['urgencia'] == 'verde']

    def agrupar_por_laboratorio(lista_medicamentos: List[Dict[str, str]]):
        laboratorios = {}
        for med in lista_medicamentos:
            lab = med['laboratorio']
            laboratorios.setdefault(lab, []).append(med)
        return laboratorios

    vermelhos_agrupados = agrupar_por_laboratorio(vermelhos)
    amarelos_agrupados = agrupar_por_laboratorio(amarelos)
    verdes_agrupados = agrupar_por_laboratorio(verdes)

    def imprimir_lista(titulo: str, cor: str, medicamentos_agrupados: Dict[str, List[Dict[str, str]]]) -> None:
        print(f"\n{cor} {titulo} {cor}")
        print("=" * 60)
        if not medicamentos_agrupados:
            print("Nenhum medicamento nesta categoria")
            return
        for lab, lista in medicamentos_agrupados.items():
            print(f"\n🏭 Laboratório: {lab.upper()}")
            for i, med in enumerate(lista, 1):
                print(f"   {i}. {med['nome']}")
                print(f"      📦 Apresentação: {med['apresentacao']}")
                print(f"      📊 Quantidade: {med['quantidade']}")
            print()

    imprimir_lista("LISTA 1 - ALTA URGÊNCIA (VERMELHO)", "🔴", vermelhos_agrupados)
    imprimir_lista("LISTA 2 - MÉDIA URGÊNCIA (AMARELO)", "🟡", amarelos_agrupados)
    imprimir_lista("LISTA 3 - BAIXA URGÊNCIA (VERDE)", "🟢", verdes_agrupados)

    print("\n" + "=" * 60)
    print("📊 RESUMO GERAL")
    print("=" * 60)
    print(f"🔴 Alta urgência: {len(vermelhos)} medicamento(s)")
    print(f"🟡 Média urgência: {len(amarelos)} medicamento(s)")
    print(f"🟢 Baixa urgência: {len(verdes)} medicamento(s)")
    print(f"📦 Total: {len(medicamentos)} medicamento(s)")
    print(f"🏭 Laboratórios: {len(listar_laboratorios(medicamentos))}")


def main() -> None:
    medicamentos: List[Dict[str, str]] = []

    print("=== SISTEMA DE LISTA DE COMPRAS - FARMÁCIA ===")
    print("Níveis de urgência:")
    print("🟢 VERDE - Baixa prioridade")
    print("🟡 AMARELO - Média prioridade")
    print("🔴 VERMELHO - Alta prioridade\n")

    while True:
        print("\n" + "=" * 50)
        print("MENU PRINCIPAL")
        print("=" * 50)
        print("1. 📝 Cadastrar medicamentos")
        print("2. 📊 Gerar listas por urgência")
        print("3. ✏  Editar laboratório")
        print("4. 🗑  Deletar laboratório")
        print("5. 🏭 Listar laboratórios cadastrados")
        print("6. 🚪 Sair")
        print("7. ❌ Excluir medicamento")

        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == '1':
            cadastrar_medicamentos(medicamentos)
        elif opcao == '2':
            gerar_listas(medicamentos)
        elif opcao == '3':
            editar_laboratorio(medicamentos)
        elif opcao == '4':
            deletar_laboratorio(medicamentos)
        elif opcao == '5':
            labs = listar_laboratorios(medicamentos)
            if labs:
                print("\n🏭 LABORATÓRIOS CADASTRADOS:")
                for i, lab in enumerate(labs, 1):
                    count = sum(1 for med in medicamentos if med['laboratorio'] == lab)
                    print(f"{i}. {lab} ({count} medicamento(s))")
            else:
                print("❌ Nenhum laboratório cadastrado.")
        elif opcao == '6':
            print("👋 Obrigado por usar o sistema!")
            break
        elif opcao == '7':
            deletar_medicamento(medicamentos)
        else:
            print("❌ Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
