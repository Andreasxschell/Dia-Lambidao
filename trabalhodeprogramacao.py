import random
import os
import time

dia = 0
estoque = []
moedas = 50
pedidos_loja = []

# INFRAESTRUTURA DO BUNKER (0 A 10 CADA)
porta = 10
teto = 10
vent = 10

# JOGADOR 1 (INTELIGENTE)
vida1 = 100
fome1 = 100
sede1 = 100
sanidade1 = 100
explorando1 = 0
estaVivo1 = True

# JOGADOR 2 (DEPRIMIDO)
vida2 = 100
fome2 = 100
sede2 = 100
sanidade2 = 100
explorando2 = 0
estaVivo2 = True

# JOGADOR 3 (ANSIOSO)
vida3 = 100
fome3 = 100
sede3 = 100
sanidade3 = 100
explorando3 = 0
campeonato3 = 0  # DIAS RESTANTES NO CAMPEONATO DE AURA
estaVivo3 = True

evento = 0
evento_forcado = None

# ITENS DISPONÍVEIS NA LOJA VIRTUAL E SEUS PREÇOS EM MOEDAS
itens_loja = {
    "Comida": 15,
    "Agua": 15,
    "Medkit": 40,
    "Caixa de Ferramentas": 50
}


def digitarTexto(texto, velocidade=0.05):
    for caractere in texto:
        print(caractere, end='', flush=True)
        time.sleep(velocidade)
    print()  # QUEBRA LINHAs


def limparTela():
    os.system('cls' if os.name == 'nt' else 'clear')


def atualizarAtributos():
    if explorando1 == 0 and estaVivo1:
        print(f"\n {nome1}: Vida:{vida1}% | Fome: {fome1}% | Sede: {sede1}% | Sanidade: {sanidade1}% ")
    if explorando2 == 0 and estaVivo2:
        print(f"\n {nome2}: Vida: {vida2}% | Fome: {fome2}% | Sede: {sede2}% | Sanidade: {sanidade2}% ")
    if explorando3 == 0 and campeonato3 == 0 and estaVivo3:
        print(f"\n {nome3}: Vida: {vida3}% | Fome: {fome3}% | Sede: {sede3}% | Sanidade: {sanidade3}% ")


def atualizarDia(somar=0):
    global dia
    if somar == 1:
        dia += 1
    
    print(f"Dia {dia}")


def atualizarInfraestrutura():
    print(f"STATUS DO BUNKER -> Porta: {porta}/10 | Teto: {teto}/10 | Ventilação: {vent}/10")


def atualizarMoedas():
    print(f"Moedas (Sucatas): {moedas}")


def arrumarInfraestrutura():
    global porta, teto, vent
    limparTela()
    print("|| MANUTENÇÃO DO BUNKER ||")
    print(f"1. Reparar Porta ({porta}/10)")
    print(f"2. Reparar Teto ({teto}/10)")
    print(f"3. Reparar Ventilação ({vent}/10)")
    print("4. Voltar")
    
    escolha = input(":")
    
    if escolha in ["1", "2", "3"]:
        if editorDoEstoque(1, "Caixa de Ferramentas"):
            if escolha == "1":
                porta = 10
                print("! Você usou uma Caixa de Ferramentas e reforçou a Porta !")
            elif escolha == "2":
                teto = 10
                print("! Você usou uma Caixa de Ferramentas e arrumou o Teto !")
            elif escolha == "3":
                vent = 10
                print("! Você usou uma Caixa de Ferramentas e reparou a Ventilação !")
        else:
            print("Você precisa de uma Caixa de Ferramentas no estoque!")
        input("\nEsperando Interação...")
    elif escolha == "4":
        return
    else:
        print("Entrada Invalida")
        input("\nEsperando Interação...")


# FUNÇÃO DA LOJA VIRTUAL NO COMPUTADOR DO BUNKER
def lojaVirtual():
    global moedas, pedidos_loja
    while True:
        limparTela()
        print("|| LOJA VIRTUAL (COMPUTADOR DO BUNKER) ||")
        print(f"Moedas (Sucatas) disponíveis: {moedas}")
        print("Os itens comprados chegam no dia seguinte, ao dormir!")
        print("--------------------------------------------------------")
        opcoes = list(itens_loja.keys())
        for i, item in enumerate(opcoes, start=1):
            print(f"{i}. {item} - {itens_loja[item]} Moedas")
        print(f"{len(opcoes)+1}. Voltar")

        escolha = input(":")

        # COMPRA DO ITEM ESCOLHIDO SE HOUVER MOEDAS SUFICIENTES
        if escolha.isdigit() and 1 <= int(escolha) <= len(opcoes):
            item_escolhido = opcoes[int(escolha)-1]
            preco = itens_loja[item_escolhido]
            if moedas >= preco:
                moedas -= preco
                pedidos_loja.append(item_escolhido)
                print(f"! Pedido de {item_escolhido} feito! Chega amanhã !")
            else:
                print("Você não tem Moedas suficientes para esse item!")
            input("Esperando Interação...")
        elif escolha == str(len(opcoes)+1):
            return
        else:
            print("Entrada Invalida")
            input("Esperando Interação...")


def diasSobrevividos():
    if dia < 1:
        digitarTexto("Eu me pergunto como você morreu antes mesmo do jogo começar de verdade", 0.05)
    elif dia < 5:
        digitarTexto("Você é muito ruim, jogue melhor na proxima :P", 0.05)
    elif dia < 10:
        digitarTexto("Eu diria que você é um jogador mediano, meh", 0.05)
    elif dia < 15:
        digitarTexto("HMMMMMMMMM você não é tão ruim assim, estou surpreso", 0.05)
    elif dia < 20:
        digitarTexto("Não aguentou a dificuldade hard do jogo né né né né hahaha, parabéns por estar chegando no fim", 0.05)


def gameOver(motivo):
    limparTela()

    print("\n  GAME OVER  \n")
    
    if motivo == 0:
        digitarTexto("O tanque de urânio para o drone CALA não foi neutralizado diariamente e explodiu o bunker em pedacinhos :(", 0.05)
        digitarTexto("Assim seus sobreviventes ficaram sem volta para casa e andaram sem rumo...", 0.05)
        digitarTexto("Seus sobreviventes morreram porque os lambedores deram lambidões e eles derreteram brutalmente", 0.05)
        diasSobrevividos()
    elif motivo == 1:
        digitarTexto("Seus sobreviventes morreram porque ficaram sem recursos", 0.05)
        digitarTexto("Assim... enfraqueceram lentamente e dramaticamente..........", 0.05)
        digitarTexto("E morreram enquanto dormiam.....", 0.1)
        digitarTexto("DRAMATICAMENTE!!!", 0.01)
        diasSobrevividos()
    elif motivo == 2:
        digitarTexto("Ihhh fodeu! A dança dos sobreviventes foi tão patética e desafinada que não impressionou ninguém!", 0.05)
        digitarTexto("Os Lambedores Musculosos deram um LAMBIDÃO TRIPLO no tanque de Urânio do CALA!", 0.05)
        digitarTexto("O tanque explodiu instantaneamente e evaporou o bunker inteiro com todo mundo dentro!", 0.05)
        diasSobrevividos()
    else:
        digitarTexto("Seus sobreviventes esqueceram de respirar e morreram porque eu quis", 0.05)
        diasSobrevividos()
        
    input("\nPressione Enter para fechar o jogo...")
    exit()


# FUNÇÃO DE FINAL DE JOGO NO DIA 30 (PLACEHOLDER PRA HISTÓRIA)
def fimDoJogo():
    limparTela()
    print("\n  FIM DE JOGO  \n")
    digitarTexto("E foi assim que essa história idiota chegou ao fim, de um jeito meio aleatório mesmo.", 0.05)
    input("\nPressione Enter para fechar o jogo...")
    exit()


def sortearEvento():
    global evento, evento_forcado
    
    # SE FOI USADO O COMANDO DEBUG, USA O EVENTO FORÇADO
    if evento_forcado is not None:
        evento = evento_forcado
        evento_forcado = None
        return evento

    # SE O TETO ESTIVER ABERTO, O LAMBEDOR OBSERVADOR TEM PRIORIDADE ABSOLUTA!
    if teto == 0:
        evento = 6
        return evento

    # SORTEIA EVENTOS GERAIS (1, 2, 3, 4, 5, 7, 8, 9, 10)
    evento = random.choice([1, 2, 3, 4, 5, 7, 8, 9, 10]) 
    
    # VALIDAÇÃO DO EVENTO 3 (CAMPEONATO DE AURA)
    if evento == 3:
        if not estaVivo3 or explorando3 > 0 or campeonato3 > 0:
            evento = 1

    # VALIDAÇÃO DO EVENTO 4 (SÓ OCORRE SE A PORTA ESTIVER DESTRUÍDA)
    if evento == 4 and porta > 0:
        evento = 2

    # VALIDAÇÃO DO EVENTO 7 (BICHO BUFADO) EXIGE DEPRIMIDO VIVO E NO BUNKER
    if evento == 7:
        if not estaVivo2 or explorando2 > 0:
            evento = 5

    # VALIDAÇÃO DO EVENTO 10 (SHIN NÃO CANÔNICO) SÓ DEPOIS DO DIA 20 E COM O INTELIGENTE VIVO E NO BUNKER
    if evento == 10:
        if dia <= 20 or not estaVivo1 or explorando1 > 0:
            evento = 2

    return evento


def minigameDanca():
    limparTela()
    print("==========================================================")
    print(" [!] MINIGAME: A DANÇA DA SOBREVIVÊNCIA")
    print("==========================================================")
    digitarTexto("RESUMO: Os Lambedores Musculosos querem lamber o Urânio!", 0.03)
    digitarTexto("A única forma de assustá-los é mandar uma dança PERFEITA!", 0.03)
    digitarTexto("Uma sequência de 8 números (0 e 1) vai piscar por 1 SEGUNDO.", 0.03)
    digitarTexto("Memorize e digite exatamente como viu para realizar os passos!", 0.03)
    print("==========================================================")
    input("\nQuando estiver pronto, pressione Enter para começar...")

    limparTela()
    
    sequencia_correta = "".join([str(random.randint(0, 1)) for _ in range(8)])
    
    print("\n  MEMORIZE A DANÇA:")
    print(f"\n      >>> {sequencia_correta} <<<\n")
    time.sleep(1)
    
    limparTela()
    print("==========================================================")
    resposta = input("Digite a sequência da dança: ").strip()
    
    acertos = 0
    for i in range(min(len(resposta), len(sequencia_correta))):
        if resposta[i] == sequencia_correta[i]:
            acertos += 1

    print("\n----------------------------------------------------------")
    print(f"Sequência Correta: {sequencia_correta}")
    print(f"Sua Resposta     : {resposta}")
    print(f"Acertos: {acertos} de 8")
    print("----------------------------------------------------------")
    
    if acertos >= 4:
        digitarTexto("\n!!! INCRÍVEL !!! Os sobreviventes mandaram uns passos de dança insanos!", 0.03)
        digitarTexto("Os Lambedores Musculosos ficaram horrorizados com o físico e a sincronia de vocês!", 0.03)
        digitarTexto("Eles entraram em pânico e fugiram correndo do bunker!", 0.03)
        input("\nPressione Enter para continuar...")
    else:
        digitarTexto("\nA dança foi um desastre total... Os sobreviventes tropeçaram nas próprias pernas!", 0.03)
        input("\nPressione Enter para ver as consequências...")
        gameOver(2)


# MINIGAME PEDRA, PAPEL E TESOURA (BICHO BUFADO / SUPER BUFADO)
def minigamePedraPapelTesoura(is_super_bufado=False):
    global vida2, estaVivo2
    limparTela()
    print("==========================================================")
    if is_super_bufado:
        print(" [!] MINIGAME SUPREMO: PEDRA, PAPEL E TESOURA CONTRA O SUPER MEGA BLASTER BUFADO")
    else:
        print(" [!] MINIGAME: PEDRA, PAPEL E TESOURA CONTRA O BICHO BUFADO")
    print("==========================================================")
    digitarTexto("1. Pedra | 2. Papel | 3. Tesoura", 0.03)
    
    opcoes = {"1": "Pedra", "2": "Papel", "3": "Tesoura"}
    escolha_jogador = input("\nEscolha sua jogada (1, 2 ou 3): ").strip()
    
    while escolha_jogador not in ["1", "2", "3"]:
        escolha_jogador = input("Escolha inválida! Digite 1 (Pedra), 2 (Papel) ou 3 (Tesoura): ").strip()

    jogada_bicho = random.choice(["1", "2", "3"])
    
    print("\n----------------------------------------------------------")
    digitarTexto(f"Você jogou: {opcoes[escolha_jogador]}", 0.03)
    digitarTexto(f"O Bicho Bufado jogou: {opcoes[jogada_bicho]}", 0.03)
    print("----------------------------------------------------------")

    if escolha_jogador == jogada_bicho:
        digitarTexto("\nEMPATE! O Bicho Bufado foge com seus musculos musculosos", 0.03)
    elif (escolha_jogador == "1" and jogada_bicho == "3") or \
         (escolha_jogador == "2" and jogada_bicho == "1") or \
         (escolha_jogador == "3" and jogada_bicho == "2"):
        digitarTexto(f"\nVITÓRIA! Você venceu o Bicho Bufado!", 0.03)
        digitarTexto("Ele ficou instantaneamente NERFADO de tanta humilhação >:)", 0.03)
        digitarTexto("Tentou sair correndo de vergonha, tropeçou nas próprias pernas e QUEBROU O PESCOÇO!", 0.03)
    else:
        digitarTexto(f"\nDERROTA! O Bicho Bufado ganhou o jogo!", 0.03)
        
        if is_super_bufado:
            digitarTexto(f"O Bicho Super Ultra Mega Blaster Bufado deu um LAMBIDÃO MORTAL direto em {nome2}!", 0.03)
            digitarTexto(f"{nome2} DERRETEU INSTANTANEAMENTE EM UMA POÇA DE CARNE E MORREU!", 0.03)
            vida2 = 0
            estaVivo2 = False
        else:
            digitarTexto(f"Ele deu um sorriso com seus dentes brancos e perfeitos e desferiu um SOCO MONSTRUOSO no {nome2}!", 0.03)
            if vida2 > 20:
                dano_real = min(50, vida2 - 20)
                vida2 -= dano_real
                digitarTexto(f"O soco causou {dano_real} de dano! {nome2} ficou com {vida2}% de Vida! (Nunca morre pelo soco)", 0.03)
            else:
                digitarTexto(f"{nome2} já estava fraco demais ({vida2}% de vida). O soco não deu dano extra!", 0.03)

    input("\nPressione Enter para continuar...")


# MINIGAME QUEDA DE BRAÇO CONTRA O SHIN
def minigameQuedaDeBraco():
    global porta, teto, vent
    limparTela()
    print("==========================================================")
    print(" [!] MINIGAME: QUEDA DE BRAÇO CONTRA O SHIN")
    print("==========================================================")
    digitarTexto("RESUMO: O Shin invadiu e quer disputar força numa Queda de Braço!", 0.03)
    digitarTexto("A cada rodada, uma sequência de 4 letras (WASD) pisca por 0.5 SEGUNDOS.", 0.03)
    digitarTexto("Memorize e digite a sequência exatamente em MAIÚSCULAS ou minúsculas!", 0.03)
    print("\n--- REGRAS DA BARRA DE FORÇA ---")
    digitarTexto("Sua força começa em 5/10. Chegue a 10 para VENCER!", 0.03)
    digitarTexto("Se sua força chegar a 0, você PERDE e o Shin destrói o bunker!", 0.03)
    digitarTexto("4 Acertos = +2 Força | 3 Acertos = +1 Força | 2 Acertos = 0 Força", 0.03)
    digitarTexto("1 Acerto  = -1 Força | 0 Acertos = -2 Força", 0.03)
    print("==========================================================")
    input("\nPressione Enter para começar a disputa...")

    forca = 5
    teclas = ["W", "A", "S", "D"]

    while 0 < forca < 10:
        limparTela()
        barra = "█" * forca + "░" * (10 - forca)
        print(f"FORÇA ATUAL: [{barra}] ({forca}/10)")
        print("----------------------------------------------------------")
        input("Pressione Enter para ver a sequência da rodada...")

        sequencia = "".join([random.choice(teclas) for _ in range(4)])

        limparTela()
        print(f"\n      >>> {sequencia} <<<\n")
        time.sleep(0.5)

        limparTela()
        print(f"FORÇA ATUAL: [{barra}] ({forca}/10)")
        resposta = input("Digite a sequência de 4 letras (WASD): ").strip().upper()

        acertos = 0
        for i in range(min(len(resposta), 4)):
            if resposta[i] == sequencia[i]:
                acertos += 1

        print(f"\nSequência Correta: {sequencia}")
        print(f"Sua Resposta     : {resposta}")
        print(f"Acertos: {acertos} de 4")

        if acertos == 4:
            forca += 2
            print(">> PERFEITO!")
        elif acertos == 3:
            forca += 1
            print(">> BOM!")
        elif acertos == 2:
            print(">> MEDIANO!")
        elif acertos == 1:
            forca -= 1
            print(">> RUIM!")
        else:
            forca -= 2
            print(">> PÉSSIMO!")

        forca = max(0, min(10, forca))
        time.sleep(1.5)

    limparTela()
    if forca >= 10:
        digitarTexto("==========================================================", 0.02)
        digitarTexto(" VI-TÓ-RI-A!", 0.03)
        digitarTexto(" A armadura radiante perde o brilho brutalmente...", 0.03)
        digitarTexto(" O Shin solta o seu braço, balança a cabeça decepcionado e vaza em silêncio!", 0.03)
        digitarTexto("==========================================================", 0.02)
    else:
        digitarTexto("==========================================================", 0.02)
        digitarTexto(" DERROTA! O SHIN ESMAGA SEU BRAÇO COM UMA FORÇA BRUTAL E HUMILHANTE!", 0.03)
        digitarTexto(" Tomado de fúria e deboche, o Shin entra em um frenzy destruidor...", 0.03)
        digitarTexto(" ELE ARREBENTA A PORTA, O TETO E A VENTILAÇÃO DO BUNKER COMPLETAMENTE!", 0.03)
        digitarTexto("==========================================================", 0.02)
        porta = 0
        teto = 0
        vent = 0

    input("\nPressione Enter para continuar...")


# MINIGAME DE CONTAS CONTRA O SHIN NÃO CANÔNICO
def minigameContasShinNaoCanonico():
    global estoque

    limparTela()
    print("==========================================================")
    print(" [!] MINIGAME: A LÂMINA DA MEMÓRIA CONTRA O SHIN NÃO CANÔNICO")
    print("==========================================================")
    digitarTexto(f"{nome1} pega uma faca e se prepara pra cortar cada lambidão que vier!", 0.03)
    digitarTexto("A CADA RODADA UM NÚMERO VAI APARECER, DÊ ENTER PRA VER A OPERAÇÃO SEGUINTE!", 0.03)
    digitarTexto("ELE NUNCA VAI MOSTRAR O RESULTADO ANTERIOR DE NOVO, TU TEM QUE MEMORIZAR!", 0.03)
    digitarTexto("SÃO 10 CONTAS SEGUIDAS, UM ERRO E O ESTOQUE INTEIRO SOME JUNTO COM ELE!", 0.03)
    print("==========================================================")
    input("\nPressione Enter para começar a sequência...")

    limparTela()
    resultado_atual = random.randint(1, 20)
    print(f"\n      >>> NÚMERO INICIAL: {resultado_atual} <<<\n")
    time.sleep(2)
    limparTela()

    for rodada in range(1, 11):
        operador = random.choice(["+", "-"])
        numero_op = random.randint(1, 15)

        if operador == "+":
            resultado_correto = resultado_atual + numero_op
        else:
            resultado_correto = resultado_atual - numero_op

        print(f"RODADA {rodada}/10")
        print(f"\n      >>> {operador} {numero_op} <<<\n")
        time.sleep(1.5)
        limparTela()

        try:
            resposta = int(input(f"RODADA {rodada}/10 - Qual o resultado da conta com o número anterior? "))
        except ValueError:
            resposta = None

        if resposta != resultado_correto:
            limparTela()
            digitarTexto("\nA FACA ESCORREGA DA MÃO! A CONTA ESTAVA ERRADA!", 0.03)
            digitarTexto("O SHIN NÃO CANÔNICO DÁ UM LAMBIDÃO SILENCIOSO EM TODO O ESTOQUE!", 0.03)
            estoque = []
            digitarTexto("E ELE SIMPLESMENTE SOME JUNTO COM TUDO, SEM DEIXAR VESTÍGIOS...", 0.03)
            input("\nPressione Enter para continuar...")
            return

        resultado_atual = resultado_correto
        limparTela()

    digitarTexto("\nA ÚLTIMA CONTA FOI CORTADA COM PRECISÃO!", 0.03)
    digitarTexto(f"{nome1} encara o Shin Não Canônico com a faca erguida, sem hesitar...", 0.03)
    digitarTexto("O SHIN NÃO CANÔNICO FICA IMÓVEL POR UM INSTANTE...", 0.03)
    digitarTexto("...E SOME NO AR SEM DAR NENHUMA RESPOSTA, COMO SE NUNCA TIVESSE ESTADO ALI.", 0.03)
    input("\nPressione Enter para continuar...")


def exibirCardEvento():
    global porta, teto, vent, campeonato3, estoque
    global sanidade1, sanidade2, sanidade3
    
    if evento == 0:
        return

    limparTela()

    if evento == -1:
        print("\n [!] EVENTO DE TESTE: DAVI GEHART")
        print(" --------------------------------------------------------")
        digitarTexto(" Um lambedor albino e desnutrido tentou lamber a porta do bunker,", 0.03)
        digitarTexto(" errou a mira, tropeçou na própria língua e caiu de cara no chão.", 0.03)
        digitarTexto(" Ai o Davi Gehart apareceu e pulverizou o lambedor com raio laser pelos olhos", 0.03)
        digitarTexto(" e o lambedor explodiu brutalmente", 0.03)
        print(" --------------------------------------------------------")
        digitarTexto(" Efeito: Aura", 0.03)

    elif evento == 1:
        print("\n [!] EVENTO: ATAQUE DO LAMBEDOR BEBÊ")
        print("          █    █")
        print("          ██  ██")
        print("          ██████")
        print("         ▓██████▓")
        print("          ██████")
        print("           ████")
        print("         ████████")
        print("        ██████████")
        print("        ██████████")
        print("        ██████████")
        print("▒▒▒▒▒▒▒▒██▓█  █▓██▒▒▒▒▒▒▒▒")
        print("░░░░░░░░█ ▓▓▓▓▓▓ █░░░░░░░░")
        print("▒▒▒▒▒▒▒▒▒███▒▒███▒▒▒▒▒▒▒▒▒")
        print("░░░░░░░░░░░░░░░░░░░░░░░░░░")
        print("░░░░░░░░░░░░░░░░░░░░░░░░░░")
        print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
        print(" --------------------------------------------------------")
        digitarTexto(" Um lambedor bebê minúsculo e invocadinho se enfiou pelo tubo de ar.", 0.03)
        digitarTexto(" Ele tentou invadir o bunker, mas ficou entalado na grade de ferro.", 0.03)
        digitarTexto(" Ficou TÃO bravo com a humilhação que deu uma birra, esperneou", 0.03)
        digitarTexto(" e EXPLODIU de pura raiva junto com a ventilação!", 0.03)
        print(" --------------------------------------------------------")
        vent = 0
        digitarTexto(" EFEITO: A Ventilação foi completamente destruída na explosão! (0/10)", 0.03)

    elif evento == 2:
        print("\n [!] EVENTO: O LAMBEDOR SAFADO")
        print(" --------------------------------------------------------")
        digitarTexto(" Durante a madrugada, um lambedor safado veio sorrateiramente até a entrada.", 0.03)
        digitarTexto(" Ele deu um lambidão supremo ultra corrosiva na porta blindada do bunker!", 0.03)
        digitarTexto(" O metal deu um chiado cabuloso e começou a Derreter um pedaço!", 0.03)
        print(" --------------------------------------------------------")
        porta = max(0, porta - 4)
        digitarTexto(f" EFEITO: A resistência da Porta caiu em -4 pontos! (Status atual: {porta}/10)", 0.03)
        if porta == 0:
            digitarTexto(" [!] ATENÇÃO: A porta foi completamente destruída! O bunker está desprotegido!", 0.03)

    elif evento == 3:
        print("\n [!] EVENTO: O CAMPEONATO DE FARMAR AURA")
        print(" --------------------------------------------------------")
        digitarTexto(f" Um lambedor estiloso bateu na porta e convidou {nome3} para o Campeonato de Farmar Aura.", 0.03)
        digitarTexto(f" tomado por um orgulho desmedido, {nome3} aceitou na hora, pulou a janela e fugiu!", 0.03)
        
        dias_fora = random.randint(1, 5)
        campeonato3 = dias_fora
        print(" --------------------------------------------------------")
        digitarTexto(f" EFEITO: {nome3} sumiu para competir e voltará em {dias_fora} dia(s)!", 0.03)

        # SE ANSIOSO FOI PRO CAMPEONATO E OS OUTROS DOIS JÁ ESTAVAM EM EXPEDIÇÃO, O BUNKER FICA VAZIO
        ninguem_no_bunker = not ((estaVivo1 and explorando1 == 0) or (estaVivo2 and explorando2 == 0))
        if ninguem_no_bunker:
            digitarTexto(" [!] NÃO SOBROU NINGUÉM NO BUNKER PRA CUIDAR DO TANQUE DE URÂNIO!", 0.03)
            input("\nPressione Enter para ver as consequências...")
            gameOver(0)
            return

    elif evento == 4:
        print("\n [!] EVENTO CRÍTICO: INVASÃO DOS LAMBEDORES MUSCULOSOS")
        print(" --------------------------------------------------------")
        digitarTexto(" Como a porta do bunker está DESTRUÍDA, um bando de Lambedores Musculosos invadiu a sala!", 0.03)
        digitarTexto(" Eles estão babando e marchando direto em direção ao tanque de Urânio para dar um lambidão!", 0.03)
        print(" --------------------------------------------------------")
        input("\nPressione Enter para tentar impedir a tragédia...")
        minigameDanca()
        return

    elif evento == 5:
        print("\n [!] EVENTO: O LAMBEDOR TARADO")
        print(" --------------------------------------------------------")
        digitarTexto(" Um lambedor tarado subiu no teto do bunker, e deu um LAMBIDÃO", 0.03)
        digitarTexto(" O teto derreteu instantaneamente abrindo um buraco enorme, e o tarado fugiu rindo!", 0.03)
        print(" --------------------------------------------------------")
        teto = 0
        digitarTexto(" EFEITO: O Teto do bunker foi completamente destruído! (0/10)", 0.03)

    elif evento == 6:
        print("\n [!] EVENTO: O LAMBEDOR OBSERVADOR")
        print(" --------------------------------------------------------")
        digitarTexto(" Como o teto está DESTRUÍDO e aberto, uma sombra sinistra apareceu espiando lá de cima...", 0.03)
        digitarTexto(" Um Lambedor Observador encarou fixamente cada pessoa presente no bunker...", 0.03)
        digitarTexto(" Ele sussurrou com uma voz assustadora: 'Eu sou o Tio do Shin...' e vazou de mansinho!", 0.03)
        print(" --------------------------------------------------------")
        
        afetados = []
        if estaVivo1 and explorando1 == 0:
            sanidade1 = max(0, int(sanidade1 * 0.25))
            afetados.append(nome1)
        if estaVivo2 and explorando2 == 0:
            sanidade2 = max(0, int(sanidade2 * 0.25))
            afetados.append(nome2)
        if estaVivo3 and explorando3 == 0 and campeonato3 == 0:
            sanidade3 = max(0, int(sanidade3 * 0.25))
            afetados.append(nome3)

        if afetados:
            digitarTexto(f" EFEITO: Trauma psicológico grave! {', '.join(afetados)} perderam 75% da Sanidade!", 0.03)
        else:
            digitarTexto(" EFEITO: Não havia ninguém dentro do bunker no momento para ser traumatizado!", 0.03)

    elif evento == 7:
        if dia > 20:
            print("\n [!] EVENTO EXTREMO: O BICHO SUPER ULTRA MEGA BLASTER BUFADO PRA CARALHO")
            print(" --------------------------------------------------------")
            digitarTexto(" O CHÃO TREME! Um Bicho Super Ultra Mega Blaster Bufado despenca do céu,", 0.03)
            digitarTexto(" DESTRUINDO O TETO DO BUNKER COMPLETAMENTE COM O SEU PESO!", 0.03)
            digitarTexto(f" Com dentes reluzentes e músculos absurdos, ele encarou {nome2} faminto!", 0.03)
            teto = 0
            print(" --------------------------------------------------------")
            input("\nPressione Enter para encarar a batalha mortal no Pedra, Papel e Tesoura...")
            minigamePedraPapelTesoura(is_super_bufado=True)
            return
        else:
            print("\n [!] EVENTO: O BICHO BUFADO PRA CARALHO")
            print(" --------------------------------------------------------")
            digitarTexto(" Um lambedor extremamente bombado, reluzente e com dentes brancos e lindos surge!", 0.03)
            digitarTexto(f" Ele força seus músculos gigantes na frente de {nome2} só para humilhá-lo brutalmente <:O!", 0.03)
            digitarTexto(f" Ele desafia o {nome2} para uma disputa decisiva!", 0.03)
            print(" --------------------------------------------------------")
            input("\nPressione Enter para encarar o Bicho Bufado no Pedra, Papel e Tesoura...")
            minigamePedraPapelTesoura(is_super_bufado=False)
            return

    elif evento == 8:
        print("\n [!] EVENTO LENDÁRIO: A APARIÇÃO DO SHIN")
        print(" --------------------------------------------------------")
        digitarTexto(" UMA LUZ VERDE CEGANTE ILUMINA A ENTRADA DO BUNKER!", 0.03)
        digitarTexto(" A porta se escancara violentamente! Surge o lendário SHIN,", 0.03)
        digitarTexto(" um lambedor verde imponente ostentando uma ARMADURA ULTRA RADIANTE!", 0.03)
        digitarTexto(" Com um olhar desafiador, ele aponta para a mesa do bunker e exige...", 0.03)
        digitarTexto(" UMA DISPUTA DE QUEDA DE BRAÇO MORTAL!", 0.03)
        print(" --------------------------------------------------------")
        input("\nPressione Enter para medir forças na Queda de Braço...")
        minigameQuedaDeBraco()
        return

    elif evento == 9:
        print("\n [!] EVENTO: A CHEGADA DE OMEGA")
        print(" --------------------------------------------------------")
        digitarTexto(" A porta range devagar e um lambedor gigantesco se arrasta pra dentro...", 0.03)
        digitarTexto(" SEU NOME É OMEGA, TEM UMA BARRIGA ENORME E APENAS UM BRAÇO!", 0.03)
        digitarTexto(" Ele encara vocês com uma fome absurda e resmunga...", 0.03)
        digitarTexto(" 'AFJIOAWFIAOFMRIGOGROEIGMERO'", 0.03)
        print(" --------------------------------------------------------")
        input("\nPressione Enter para ver o que o estoque tem...")

        qtd_comida = estoque.count("Comida")

        if qtd_comida >= 3:
            for _ in range(3):
                editorDoEstoque(1, "Comida")
            digitarTexto("\n Vocês entregam as 3 comidas para Omega.", 0.03)
            digitarTexto(" Ele devora tudo numa mordida só, solta um arroto satisfeito...", 0.03)
            digitarTexto(" ...e sai se arrastando de volta pra fora do bunker, tranquilo e satisfeito.", 0.03)
        else:
            digitarTexto(f"\n Vocês só têm {qtd_comida} Comida(s) no estoque, não é o suficiente!", 0.03)
            digitarTexto(" OMEGA FICA VERMELHO DE RAIVA...", 0.03)
            digitarTexto(" E DÁ UMA BARRIGADA VIOLENTA EM CIMA DO ESTOQUE!", 0.03)

            qtd_destruir = min(len(estoque), random.randint(2, 4))
            itens_destruidos = []
            for _ in range(qtd_destruir):
                if estoque:
                    item_removido = random.choice(estoque)
                    estoque.remove(item_removido)
                    itens_destruidos.append(item_removido)

            if itens_destruidos:
                digitarTexto(f"\n A barrigada esmagou e destruiu: {', '.join(itens_destruidos)}!", 0.03)
            else:
                digitarTexto("\n Felizmente o estoque já estava vazio, nada para destruir.", 0.03)

            digitarTexto("\n Omega fica MUITO IRRITADO, grita algo incompreensível e vaza correndo com o braço só balançando.", 0.03)

    elif evento == 10:
        print("\n [!] EVENTO ESPECIAL: O SHIN NÃO CANÔNICO")
        print(" --------------------------------------------------------")
        digitarTexto(" A LUZ DO BUNKER TREME E UMA FIGURA QUASE INVISÍVEL SE MATERIALIZA...", 0.03)
        digitarTexto(" ELE É CINZA, TRANSLÚCIDO, MAS SUA PRESENÇA ESMAGA O AR DA SALA...", 0.03)
        digitarTexto(" É O SHIN NÃO CANÔNICO, E NINGUÉM SABE EXPLICAR DIREITO COMO ELE EXISTE...", 0.03)
        digitarTexto(f" {nome1} ENCARA A FIGURA CINZA, PEGA UMA FACA E SE PREPARA PRA REAGIR!", 0.03)
        print(" --------------------------------------------------------")
        input("\nPressione Enter para encarar o Shin Não Canônico...")
        minigameContasShinNaoCanonico()
        return

    print("==========================================================")
    input("\nPressione Enter para continuar o dia...")


def atualizarEstoque():
    print("\nSeu Estoque: ", end='')
    for i in range(len(estoque)):
        if i == len(estoque)-1:
            print(estoque[i])
        else: 
            print(estoque[i] + ", ", end='')


def chamarSobreviventes():
    global evento_forcado
    while True:
        print("\n|| ESCOLHA UMA AÇÃO ||")
        
        if not estaVivo1:
            print(f"1.{nome1} está morto")
        elif explorando1 == 0:
            print(f"1.Mover {nome1}")
        else:
            print(f"1.{nome1} está explorando")

        if not estaVivo2:
            print(f"2.{nome2} está morto")
        elif explorando2 == 0:
            print(f"2.Mover {nome2}")
        else:
            print(f"2.{nome2} está explorando")

        if not estaVivo3:
            print(f"3.{nome3} está morto")
        elif campeonato3 > 0:
            print(f"3.{nome3} está no campeonato de aura")
        elif explorando3 == 0:
            print(f"3.Mover {nome3}")
        else:
            print(f"3.{nome3} está explorando")

        print("4.Manutenção da Infraestrutura (Porta, Teto, Ventilação)")
        print("5.Loja Virtual (Computador)")
        print("6.Dormir")
        print("7.Sair do Jogo")
        entrada = input(":")

        if entrada == "debugevento":
            try:
                num_evt = int(input("Digite o número do evento que quer forçar (-1 a 10): "))
                evento_forcado = num_evt
                print(f"DEBUG: Próximo evento forçado para {evento_forcado}!")
            except ValueError:
                print("Número de evento inválido!")
            input("Pressione Enter para continuar...")
            limparTela()
            break
        elif entrada == "1":
            if not estaVivo1:
                limparTela()
                print(f"{nome1} está morto e não pode realizar ações!")
            elif explorando1 == 0:
                limparTela()
                sobrevivente(1)
                break
            else:
                limparTela()
                print(f"{nome1} está explorando e não pode ser movido")
        elif entrada == "2":
            if not estaVivo2:
                limparTela()
                print(f"{nome2} está morto e não pode realizar ações!")
            elif explorando2 == 0:
                limparTela()
                sobrevivente(2)
                break
            else:
                limparTela()
                print(f"{nome2} está explorando e não pode ser movido")
        elif entrada == "3":
            if not estaVivo3:
                limparTela()
                print(f"{nome3} está morto e não pode realizar ações!")
            elif campeonato3 > 0:
                limparTela()
                print(f"{nome3} está ocupado farmando aura no campeonato!")
            elif explorando3 == 0:
                limparTela()
                sobrevivente(3)
                break
            else:
                limparTela()
                print(f"{nome3} está explorando e não pode ser movido")
        elif entrada == "4":
            arrumarInfraestrutura()
            break
        elif entrada == "5":
            lojaVirtual()
            break
        elif entrada == "6":
            dormir()
            break
        elif entrada == "7":
            limparTela()
            print("|| SAIR DO JOGO ||")
            confirmacao = input("Tem certeza que quer sair? (y para confirmar, se não aperte enter): ").upper()
            if confirmacao == "Y":
                limparTela()
                digitarTexto("Saindo do jogo...", 0.05)
                exit()
            else:
                limparTela()
        elif entrada == "esqueci de respirar":
            gameOver("a terra é plana")
        else:
            limparTela()
            print("Entrada Invalida")


# FUNÇÃO QUE CONTA QUANTOS SOBREVIVENTES ESTÃO NO BUNKER, EXCLUINDO UM DELES
def vivosNoBunkerExcluindo(qual):
    total = 0
    if qual != 1 and estaVivo1 and explorando1 == 0:
        total += 1
    if qual != 2 and estaVivo2 and explorando2 == 0:
        total += 1
    if qual != 3 and estaVivo3 and explorando3 == 0 and campeonato3 == 0:
        total += 1
    return total


# FUNÇÃO PARA SOBREVIVENTES
def sobrevivente(qual):
    global fome1, fome2, fome3, sede1, sede2, sede3, vida1, vida2, vida3, explorando1, explorando2, explorando3
    while True:
        print("|| ESCOLHA UMA AÇÃO ||")
        print("1.Comer")
        print("2.Beber")
        print("3.Curar")
        print("4.Explorar")
        print("5.Cancelar")
        entrada = input(":")

        # PEGA A SANIDADE ATUAL DO SOBREVIVENTE SELECIONADO
        sanidade_atual = sanidade1 if qual == 1 else (sanidade2 if qual == 2 else sanidade3)

        # AÇÃO DE COMER
        if entrada == "1":
            if sanidade_atual <= 20:
                print(f"! A sanidade está baixa demais, o sobrevivente se recusa a comer !")
                input("Esperando Interação...")
                break
            if editorDoEstoque(1, "Comida"):
                if qual == 1:
                    fome1 = min(100, fome1 + 50) 
                elif qual == 2:
                    fome2 = min(100, fome2 + 50) 
                else:
                    fome3 = min(100, fome3 + 50)
                print(f"! Gastou uma comida !")
            else:
                print("Você não tem Comida no estoque!")
            input("Esperando Interação...")
            break

        # AÇÃO DE BEBER
        elif entrada == "2":
            if sanidade_atual <= 20:
                print(f"! A sanidade está baixa demais, o sobrevivente se recusa a beber !")
                input("Esperando Interação...")
                break
            if editorDoEstoque(1, "Agua"):
                if qual == 1:
                    sede1 = min(100, sede1 + 70)
                elif qual == 2:
                    sede2 = min(100, sede2 + 70)
                else:
                    sede3 = min(100, sede3 + 70)
                print(f"! Gastou uma Agua !")
            else:
                print("Você não tem Agua no estoque!")
            input("Esperando Interação...")
            break

        # AÇÃO DE CURAR
        elif entrada == "3":
            if editorDoEstoque(1, "Medkit"):
                if qual == 1:
                    vida1 = min(100, vida1 + 20)
                elif qual == 2:
                    vida2 = min(100, vida2 + 20)
                else:
                    vida3 = min(100, vida3 + 20)
                print(f"! Gastou um Medkit !")
            else:
                print("Você não tem Medkit no estoque!")
            input("Esperando Interação...")
            break

        # AÇÃO DE EXPLORAR
        elif entrada == "4":
            if vivosNoBunkerExcluindo(qual) == 0:
                print("! Não dá pra explorar, esse é o único sobrevivente no bunker no momento !")
                input("Esperando Interação...")
                break
            if qual == 1:
                explorando1 = 3
                digitarTexto(f"!!! {nome1} saiu para uma expedição de 3 dias !!!", 0.04)
            elif qual == 2:
                explorando2 = 3
                digitarTexto(f"!!! {nome2} saiu para uma expedição de 3 dias !!!", 0.04)
            else:
                explorando3 = 3
                digitarTexto(f"!!! {nome3} saiu para uma expedição de 3 dias !!!", 0.04)
            input("Esperando Interação...")
            break

        elif entrada == "5":
            break
        else:
            limparTela()
            print("Entrada Invalida")

# FUNÇÃO PARA DORMIR
def dormir():
    global vida1, vida2, vida3, sanidade1, sanidade2, sanidade3, fome1, fome2, fome3, sede1, sede2, sede3, dia
    global explorando1, explorando2, explorando3, campeonato3, estoque, moedas, pedidos_loja
    global vent
    global estaVivo1, estaVivo2, estaVivo3

    itens_possiveis = ["Comida", "Agua", "Medkit", "Caixa de Ferramentas"]

    dia += 1

    # SE CHEGOU NO DIA 30, O JOGO ACABA AQUI (PLACEHOLDER PRA HISTÓRIA)
    if dia >= 30:
        fimDoJogo()
        return

    sortearEvento()

    # ENTREGA OS PEDIDOS DA LOJA VIRTUAL FEITOS NO DIA ANTERIOR
    if pedidos_loja:
        estoque.extend(pedidos_loja)
        pedidos_loja = []

    vent = max(0, vent - random.randint(0, 3))

    # RECUPERAÇÃO OU RETORNO DE EXPEDIÇÃO DO INTELIGENTE
    p1_retornou = False
    if estaVivo1:
        if explorando1 == 0:
            vida1 = min(100, vida1 + 10)
            sanidade1 = min(100, sanidade1 + 5)
        else:
            explorando1 -= 1
            if explorando1 == 0:
                p1_retornou = True
                dano = random.randint(0, 60)
                vida1 = max(0, vida1 - dano)
                if vida1 > 0:
                    for _ in range(5):
                        estoque.append(random.choice(itens_possiveis))
                    moedas_ganhas1 = random.randint(0, 150)
                    moedas += moedas_ganhas1

    # RECUPERAÇÃO OU RETORNO DE EXPEDIÇÃO DO DEPRIMIDO
    p2_retornou = False
    if estaVivo2:
        if explorando2 == 0:
            vida2 = min(100, vida2 + 10)
            sanidade2 = min(100, sanidade2 + 5)
        else:
            explorando2 -= 1
            if explorando2 == 0:
                p2_retornou = True
                dano = random.randint(0, 60)
                vida2 = max(0, vida2 - dano)
                if vida2 > 0:
                    for _ in range(5):
                        estoque.append(random.choice(itens_possiveis))
                    moedas_ganhas2 = random.randint(0, 150)
                    moedas += moedas_ganhas2

    # RECUPERAÇÃO, RETORNO DE EXPEDIÇÃO OU RETORNO DO CAMPEONATO DO ANSIOSO
    p3_retornou = False
    p3_retornou_campeonato = False
    dano_campeonato = 0
    if estaVivo3:
        if campeonato3 > 0:
            campeonato3 -= 1
            if campeonato3 == 0:
                p3_retornou_campeonato = True
                for _ in range(5):
                    estoque.append(random.choice(itens_possiveis))
                dano_campeonato = random.choice([0, 80])
                vida3 = max(0, vida3 - dano_campeonato)
                if dano_campeonato == 0:
                    moedas += 200
        elif explorando3 == 0:
            vida3 = min(100, vida3 + 10)
            sanidade3 = min(100, sanidade3 + 5)
        else:
            explorando3 -= 1
            if explorando3 == 0:
                p3_retornou = True
                dano = random.randint(0, 60)
                vida3 = max(0, vida3 - dano)
                if vida3 > 0:
                    for _ in range(5):
                        estoque.append(random.choice(itens_possiveis))
                    moedas_ganhas3 = random.randint(0, 150)
                    moedas += moedas_ganhas3

    # CÁLCULO DA PERDA DE SANIDADE POR CONTA DA VENTILAÇÃO QUEBRADA
    perda_sanidade_vent = 0
    if vent == 0:
        perda_sanidade_vent = 15

    # APLICAÇÃO DA PERDA DE SANIDADE EM QUEM ESTÁ NO BUNKER
    if perda_sanidade_vent > 0:
        if explorando1 == 0 and estaVivo1:
            sanidade1 = max(0, sanidade1 - perda_sanidade_vent)
        if explorando2 == 0 and estaVivo2:
            sanidade2 = max(0, sanidade2 - perda_sanidade_vent)
        if explorando3 == 0 and campeonato3 == 0 and estaVivo3:
            sanidade3 = max(0, sanidade3 - perda_sanidade_vent)

    # DESGASTE DIÁRIO DE FOME E SEDE DE QUEM NÃO ESTÁ NO CAMPEONATO
    if estaVivo1:
        fome1 = max(0, fome1 - 15)
        sede1 = max(0, sede1 - 20)
    if estaVivo2:
        fome2 = max(0, fome2 - 15)
        sede2 = max(0, sede2 - 20)
    if estaVivo3 and campeonato3 == 0:
        fome3 = max(0, fome3 - 15)
        sede3 = max(0, sede3 - 20)

    # DANO NA VIDA POR FICAR SEM SEDE
    if estaVivo1 and sede1 == 0:
        vida1 = max(0, vida1 - 25)
    if estaVivo2 and sede2 == 0:
        vida2 = max(0, vida2 - 25)
    if estaVivo3 and campeonato3 == 0 and sede3 == 0:
        vida3 = max(0, vida3 - 25)

    # DANO NA SANIDADE POR FICAR SEM FOME
    if estaVivo1 and fome1 == 0:
        sanidade1 = max(0, sanidade1 - 20)
    if estaVivo2 and fome2 == 0:
        sanidade2 = max(0, sanidade2 - 20)
    if estaVivo3 and campeonato3 == 0 and fome1 == 0:
        sanidade3 = max(0, sanidade3 - 20)

    # SE NINGUÉM SOBREVIVEU, ACABA O JOGO POR FALTA DE RECURSOS
    if not estaVivo1 and not estaVivo2 and not estaVivo3:
        gameOver(1)

    limparTela()
    digitarTexto("Vocês fecham os olhos e tentam descansar...", 0.04)
    digitarTexto("...", 0.4)
    digitarTexto(f"Hoje é Dia {dia}\n", 0.08)

    if perda_sanidade_vent > 0:
        digitarTexto("!!! O ar dentro do bunker está ficando insuportável por conta da ventilação quebrada !!!", 0.04)

    # NARRATIVA DO RETORNO DE EXPEDIÇÃO DO INTELIGENTE
    if p1_retornou:
        if vida1 > 0:
            digitarTexto(f"!!! {nome1} voltou da expedição !", 0.04)
        else:
            digitarTexto("...", 0.5)
            digitarTexto(f"{nome1} não voltou da expedição...", 0.1)
            estaVivo1 = False

    # MORTE DO INTELIGENTE POR FALTA DE RECURSOS
    if vida1 <= 0 and estaVivo1:
        digitarTexto("...", 0.2)
        digitarTexto(f"{nome1} ainda não acordou, e está muito pálido...", 0.04)
        digitarTexto(f"{nome1} não resistiu à falta de recursos e morreu!", 0.08)
        estaVivo1 = False

    # NARRATIVA DO RETORNO DE EXPEDIÇÃO DO DEPRIMIDO
    if p2_retornou:
        if vida2 > 0:
            digitarTexto(f"!!! {nome2} voltou da expedição !", 0.04)
        else:
            digitarTexto("...", 0.5)
            digitarTexto(f"{nome2} não voltou da expedição...", 0.1)
            estaVivo2 = False

    # MORTE DO DEPRIMIDO POR FALTA DE RECURSOS
    if vida2 <= 0 and estaVivo2:
        digitarTexto("...", 0.2)
        digitarTexto(f"{nome2} ainda não acordou, e está muito pálido...", 0.04)
        digitarTexto(f"{nome2} não resistiu à falta de recursos e morreu!", 0.08)
        estaVivo2 = False

    # NARRATIVA DO RETORNO DO CAMPEONATO DE FARMAR AURA DO ANSIOSO
    if p3_retornou_campeonato:
        digitarTexto(f"!!! {nome3} voltou triunfante do Campeonato de Aura trazendo 5 itens extras! !", 0.04)
        if dano_campeonato == 0:
            digitarTexto(f"{nome3} venceu o campeonato e trouxe 200 Moedas de premiação!", 0.04)
        if vida3 <= 0:
            digitarTexto(f"Porém, {nome3} levou surras terríveis no campeonato e faleceu ao chegar...", 0.08)
            estaVivo3 = False

    # NARRATIVA DO RETORNO DE EXPEDIÇÃO DO ANSIOSO
    if p3_retornou:
        if vida3 > 0:
            digitarTexto(f"!!! {nome3} voltou da expedição !", 0.04)
        else:
            digitarTexto("...", 0.5)
            digitarTexto(f"{nome3} não voltou da expedição...", 0.1)
            estaVivo3 = False

    # MORTE DO ANSIOSO POR FALTA DE RECURSOS
    if vida3 <= 0 and estaVivo3:
        digitarTexto("...", 0.2)
        digitarTexto(f"{nome3} ainda não acordou, e está muito pálido...", 0.04)
        digitarTexto(f"{nome3} não resistiu à falta de recursos e morreu!", 0.08)
        estaVivo3 = False

    # CONTAGEM DE QUEM FICOU NO BUNKER PRA CUIDAR DO TANQUE DE URÂNIO
    vivos_no_bunker = 0
    if estaVivo1 and explorando1 == 0:
        vivos_no_bunker += 1
    if estaVivo2 and explorando2 == 0:
        vivos_no_bunker += 1
    if estaVivo3 and explorando3 == 0 and campeonato3 == 0:
        vivos_no_bunker += 1

    # SE NINGUÉM FICOU NO BUNKER, O TANQUE DE URÂNIO EXPLODE
    if (estaVivo1 or estaVivo2 or estaVivo3) and vivos_no_bunker == 0:
        gameOver(0)

    input("\nPressione Enter para ver o evento do dia...")
    
    exibirCardEvento()

# FUNÇÃO PARA MEXER NO ESTOQUE
def editorDoEstoque(parametro, item):
    global estoque
    
    if parametro == 0:
        return item in estoque
        
    elif parametro == 1:
        if item in estoque:
            estoque.remove(item) 
            return True 
        else:
            return False 


def initJogo():
    itens_possiveis = ["Comida", "Agua", "Medkit", "Caixa de Ferramentas"]
    for i in range(10):
        estoque.append(random.choice(itens_possiveis))

    while True:
        limparTela()
        atualizarDia(0)
        atualizarInfraestrutura()
        atualizarMoedas()
        atualizarAtributos()
        atualizarEstoque()
        chamarSobreviventes()


print("▀▄▀ ░ ████  █  ███     █      ███  █   █ ████  █ ████   ███  █████ ░ ▀▄▀")
print("▀▄▀ ░ █   █ █ █   █    █     █   █ ██ ██ █   █   █   █ █   █ █   █ ░ ▀▄▀")
print("▀▄▀ ░ █   █ █ █████    █     █████ █ █ █ ████  █ █   █ █████ █   █ ░ ▀▄▀")
print("▀▄▀ ░ █   █ █ █   █    █     █   █ █   █ █   █ █ █   █ █   █ █   █ ░ ▀▄▀")
print("▀▄▀ ░ ████  █ █   █    █████ █   █ █   █ ████  █ ████  █   █ █████ ░ ▀▄▀")
print("                   Andreas Schell e Davi Gehart")
print("                      Versão 0.1  2025-08-15")
nome1 = input("Insira o nome do sobrevivente inteligente: ")
# EASTER EGG QUE NINGUÉM VAI ENTENDER PORQUE É ALGO PESSOAL
if nome1 == "FNaS":
    nome1 = "Andrax"
    nome2 = "Speed"
    nome3 = "Lemon"
else:
    nome2 = input("Insira o nome do sobrevivente deprimido: ")
    nome3 = input("Insira o nome do sobrevivente ansioso: ")

# FUNÇÃO QUE MOSTRA O TUTORIAL COMPLETO DO JOGO
def exibirTutorial():
    limparTela()
    print("|| TUTORIAL DO JOGO ||")
    print("==========================================================")
    digitarTexto("O OBJETIVO É SOBREVIVER O MÁXIMO DE DIAS POSSÍVEL DENTRO DO BUNKER!", 0.02)
    digitarTexto("VOCÊ CONTROLA 3 SOBREVIVENTES: O INTELIGENTE, O DEPRIMIDO E O ANSIOSO.", 0.02)
    print("----------------------------------------------------------")
    digitarTexto("CADA SOBREVIVENTE TEM 4 ATRIBUTOS: VIDA, FOME, SEDE E SANIDADE, TODOS DE 0 A 100%.", 0.02)
    digitarTexto("SE A SEDE CHEGAR A 0, A VIDA COMEÇA A CAIR. SE A FOME CHEGAR A 0, A SANIDADE COMEÇA A CAIR.", 0.02)
    digitarTexto("SE A SANIDADE DE UM SOBREVIVENTE FICAR EM 20% OU MENOS, ELE SE RECUSA A COMER OU BEBER!", 0.02)
    print("----------------------------------------------------------")
    digitarTexto("AS AÇÕES DISPONÍVEIS PRA CADA SOBREVIVENTE NO BUNKER SÃO: COMER, BEBER, CURAR OU EXPLORAR.", 0.02)
    digitarTexto("COMER E BEBER GASTAM ITENS DO ESTOQUE PRA RECUPERAR FOME E SEDE.", 0.02)
    digitarTexto("CURAR GASTA UM MEDKIT PRA RECUPERAR VIDA.", 0.02)
    digitarTexto("EXPLORAR MANDA O SOBREVIVENTE PRA UMA EXPEDIÇÃO DE 3 DIAS, TRAZENDO ITENS E MOEDAS AO VOLTAR (SE SOBREVIVER).", 0.02)
    digitarTexto("VOCÊ NÃO PODE MANDAR PRA EXPEDIÇÃO O ÚLTIMO SOBREVIVENTE QUE SOBROU NO BUNKER!", 0.02)
    print("----------------------------------------------------------")
    digitarTexto("O BUNKER TAMBÉM TEM UMA INFRAESTRUTURA: PORTA, TETO E VENTILAÇÃO, TODOS DE 0 A 10.", 0.02)
    digitarTexto("SE ALGUM DESSES CHEGAR A 0, COISAS RUINS ACONTECEM. USE UMA CAIXA DE FERRAMENTAS PRA REPARAR!", 0.02)
    print("----------------------------------------------------------")
    digitarTexto("EXISTE UMA LOJA VIRTUAL NUM COMPUTADOR DO BUNKER, ONDE VOCÊ COMPRA ITENS COM MOEDAS (SUCATAS).", 0.02)
    digitarTexto("VOCÊ COMEÇA COM 50 MOEDAS, E OS ITENS COMPRADOS CHEGAM NO DIA SEGUINTE, AO DORMIR.", 0.02)
    print("----------------------------------------------------------")
    digitarTexto("A CADA VEZ QUE VOCÊS DORMEM, UM DIA PASSA E UM EVENTO ALEATÓRIO PODE ACONTECER.", 0.02)
    digitarTexto("ALGUNS EVENTOS SÃO SÓ NARRATIVOS, OUTROS VÊM COM MINIGAMES QUE VOCÊ PRECISA VENCER!", 0.02)
    digitarTexto("SE O ESTOQUE DE COMIDA E ÁGUA ACABAR OU A INFRAESTRUTURA FOR DESTRUÍDA, AS CONSEQUÊNCIAS PODEM SER FATAIS.", 0.02)
    print("----------------------------------------------------------")
    digitarTexto("SE NINGUÉM FICAR NO BUNKER PRA CUIDAR DO TANQUE DE URÂNIO DO CALA, O JOGO ACABA NA HORA!", 0.02)
    digitarTexto("SE TODOS OS SOBREVIVENTES MORREREM, O JOGO TAMBÉM ACABA.", 0.02)
    digitarTexto("SE VOCÊ SOBREVIVER ATÉ O DIA 30, O JOGO CHEGA AO FIM COM UM FINAL ESPECIAL!", 0.02)
    print("==========================================================")
    input("\nPressione Enter para voltar ao menu...")


# FUNÇÃO DO MENU INICIAL COM AS OPÇÕES DE JOGAR E TUTORIAL
def menuInicial():
    while True:
        limparTela()
        print("|| MENU INICIAL ||")
        print("1. Jogar")
        print("2. Tutorial")
        escolha = input(":")

        if escolha == "1":
            return
        elif escolha == "2":
            exibirTutorial()
        else:
            limparTela()
            print("Entrada Invalida")
            input("Esperando Interação...")


menuInicial()

entradaInicial = input("\nAgora você está pronto com os seus sobreviventes? ou quer ver a história? (y para ver a história, se não aperte enter): ").upper()

if entradaInicial == "Y":
    limparTela()
    digitarTexto("2026 - Planeta Terra...", 0.2)
    print("")
    print()
    print("             ██▓▓▓▓")
    print("         ░░███▓▓▓▓▓░░░░")
    print("       ██░░░░░▓▓░░░░░░▓▓░")
    print("     ░██░░█░█░░▓░░░░▓▓░▓▓▓▓                  ░░░░")
    print("     ░▓▓▓▓▓▓▓░░░░░░▓░░░░░░▓                ░░░░░░░░")
    print("   ░░░░▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓░░░              ░░░░░░░░")
    print("   ░░░░░▓░░░░░░░░░░▓▓▓▓▓▓▓░░░                ░░░░")
    print("   ░░░░░░▓▓▓░░░░░░░░▓▓▓▓▓▓░░░")
    print("     ░░░▓▓▓▓░░░░░░░░░▓▓▓▓░░")
    print("     ░░░░░▓▓░░░░░░░░░▓▓▓░░░")
    print("       ░░░░▓░░░░░░░░░░░░░")
    print("         ░░░░░░░░░░░░░░")
    print("             ▓▓▓▓▓▓")
    print("")
    print("")

    digitarTexto("Em um dia ensolarado, estranhos objetos flutuavam na atmosfera, pareciam grandes prédios metálicos...", 0.05)
    digitarTexto("\nTodos eles atingiram o chão em velocidades sônicas, formando grandes crateras(obvio).", 0.05)
    digitarTexto("As escotilhas abriram, e revelaram seres totalmente anormais...", 0.05)
    digitarTexto("\nLAMBEDORES, peludos, verdes, gigantes, com uma língua enorme...", 0.05)
    digitarTexto("Eles começaram a dar lambidão em todas as pessoas existentes, e essas pessoas todas DERRETERAM!", 0.05)
    digitarTexto("\nA população terrestre tentou revidar: facas, pistolas, bombas nucleares, nada funcionava...", 0.05)
    digitarTexto("Eles pareciam invencíveis...", 0.05)
    digitarTexto("\n2030 - Bilhões de pessoas viraram poças de carne, só restavam poucos milhares.......", 0.05)
    digitarTexto(f"\nAté que 3 idiotas... {nome1}, {nome2} e {nome3} com um bunker e muita determinação, descobriram a fraqueza suprema...", 0.05)
    digitarTexto("Cortar a língua dos lambedores!", 0.05)
    digitarTexto("A língua é algo sagrado e vital pra eles. Sem ela, eles não conseguem dar lambidão e se transformam em seres tímidos...", 0.05)
    digitarTexto("\nEstá nas mãos deles.... a vitória da humanidade contra os lambedores!", 0.05)
    digitarTexto("Agora mesmo estão num bunker construindo o Cortador Aerodinâmico de Línguas Analfabetas... conhecido como CALA.", 0.05)
    digitarTexto("\nAgora será que você consegue jogar bem o suficiente para criar o CALA?", 0.05)
    digitarTexto("Duvido :)", 0.08)
    input("\nPressione Enter para começar a jogar...")

limparTela()

initJogo()
