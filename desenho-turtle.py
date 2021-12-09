
import turtle
from time import sleep

loop = True
janela = turtle.Screen()
caneta = turtle.Turtle()
caneta.speed(-10)
caneta.pensize(5)
caneta.shape("blank")
caneta.penup()
dados_desenho = []


def Retângulo():
    # ESCOLHA DA CANETA
    escolha_caneta = turtle.numinput(
        "FORMATO DA CANETA",
        "Qual o formato da caneta que você deseja usar?\n Você pode escolher:\n 1)Seta\n 2)Invisível\n 3)Círculo\n 4)Clássica\n 5)Quadrado\n 6)Triângulo\n 7)Tartaruga\n Qual você deseja?:",
        minval=1,
        maxval=7,
    )

    if escolha_caneta == 1:
        shape = "arrow"
        shape2 = "Seta"
        caneta.shape(shape)
    if escolha_caneta == 2:
        shape = "blank"
        shape2 = "Invisível"
        caneta.shape(shape)
    if escolha_caneta == 3:
        shape = "circle"
        shape2 = "Circulo"
        caneta.shape(shape)
    if escolha_caneta == 4:
        shape = "classic"
        shape2 = "Classica"
        caneta.shape(shape)
    if escolha_caneta == 5:
        shape = "square"
        shape2 = "Quadrado"
        caneta.shape(shape)
    if escolha_caneta == 6:
        shape = "triangle"
        shape2 = "Triangulo"
        caneta.shape(shape)
    if escolha_caneta == 7:
        shape = "turtle"
        shape2 = "Tartaruga"
        caneta.shape(shape)

    # POSIÇÃO X
    posicao_x = int(
        turtle.numinput(
            "POSIÇÃO EM X",
            "Qual será a posição em X do seu desenho?:\nOBS:VOCÊ SÓ PODE ESCOLHER ENTRE -300 e 300!",
            minval=-300,
            maxval=300,
        )
    )

    # POSIÇÃO Y
    posicao_y = int(
        turtle.numinput(
            "POSIÇÃO EM Y",
            "Qual será a posição em Y do seu desenho?:\nOBS:VOCÊ SÓ PODE ESCOLHER ENTRE -300 e 300!",
            minval=-300,
            maxval=300,
        )
    )
    caneta.setpos(posicao_x, posicao_y)

    # ORIENTAÇÃO DA CANETA
    escolha_orientacao = int(
        turtle.numinput(
            "ORIENTAÇÃO INICIAL",
            "Qual será a orientação em graus que você gostaria que seu desenho comece a ser desenhado?\n 1)0°\n 2)30°\n 3)60°\n 4)90°\n 5)120°\n 6)150°\n 7)180°\n 8)210°\n 9)240°\n 10)270°\n 11)300°\n 12)330°\n Qual você deseja?:",
            minval=1,
            maxval=12,
        )
    )

    if escolha_orientacao == 1:
        orientação = 0
    if escolha_orientacao == 2:
        orientação = 30
    if escolha_orientacao == 3:
        orientação = 60
    if escolha_orientacao == 4:
        orientação = 90
    if escolha_orientacao == 5:
        orientação = 120
    if escolha_orientacao == 6:
        orientação = 150
    if escolha_orientacao == 7:
        orientação = 180
    if escolha_orientacao == 8:
        orientação = 210
    if escolha_orientacao == 9:
        orientação = 240
    if escolha_orientacao == 10:
        orientação = 270
    if escolha_orientacao == 11:
        orientação = 300
    if escolha_orientacao == 12:
        orientação = 330

    # COR
    escolha_de_cor = int(
        turtle.numinput(
            "COR DO DESENHO",
            "Qual será a cor do seu desenho?\n 1)Branco?\n 2)Roxo?\n 3)Rosa?\n 4)Amarelo?\n 5)Vermelho?\n 6)Verde?\n 7)Preto?\n 8)Marrom?\n 9)Laranja?\n 10)Ciano?\n Qual você deseja?:",
            minval=1,
            maxval=10,
        )
    )

    if escolha_de_cor == 1:
        cor = "white"
        cor2 = "Branco"
    if escolha_de_cor == 2:
        cor = "medium purple"
        cor2 = "Roxo"
    if escolha_de_cor == 3:
        cor = "deep pink"
        cor2 = "Rosa"
    if escolha_de_cor == 4:
        cor = "yellow"
        cor2 = "Amarelo"
    if escolha_de_cor == 5:
        cor = "red"
        cor2 = "Vermelho"
    if escolha_de_cor == 6:
        cor = "lime green"
        cor2 = "Verde"
    if escolha_de_cor == 7:
        cor = "black"
        cor2 = "Preto"
    if escolha_de_cor == 8:
        cor = "sienna"
        cor2 = "Marrom"
    if escolha_de_cor == 9:
        cor = "coral"
        cor2 = "Laranja"
    if escolha_de_cor == 10:
        cor = "cyan"
        cor2 = "Ciano"

    caneta.fillcolor(cor)
    caneta.begin_fill()
    caneta.pendown()
    caneta.left(orientação)
    largura_retangulo = int(
        turtle.numinput("Qual a Largura?", "Insira a largura do retângulo:")
    )

    altura_retangulo = int(
        turtle.numinput("Qual a Altura?", "Insira a altura do retângulo:")
    )
    caneta.fd(largura_retangulo)
    caneta.left(90)
    caneta.fd(altura_retangulo)
    caneta.left(90)
    caneta.fd(largura_retangulo)
    caneta.left(90)
    caneta.fd(altura_retangulo)
    caneta.penup()
    caneta.home()
    caneta.end_fill()
    dados_desenho.append("A figura escolhida foi o Retângulo!")
    dados_desenho.append((f"A caneta escolhida foi: {shape2}"))
    dados_desenho.append((f"A posição escolhida foi: {posicao_x,posicao_y}"))
    dados_desenho.append((f"A orientação escolhida foi: {orientação}°"))
    dados_desenho.append((f"Cor escolhida:{cor2}"))
    dados_desenho.append((f"A largura do retângulo é: {largura_retangulo}"))
    dados_desenho.append((f"A altura do retângulo é: {altura_retangulo}"))


def Triângulo():
    # ESCOLHA DA CANETA
    escolha_caneta = turtle.numinput(
        "FORMATO DA CANETA",
        "Qual o formato da caneta que você deseja usar?\n Você pode escolher:\n 1)Seta\n 2)Invisível\n 3)Círculo\n 4)Clássica\n 5)Quadrado\n 6)Triângulo\n 7)Tartaruga\n Qual você deseja?:",
        minval=1,
        maxval=7,
    )

    if escolha_caneta == 1:
        shape = "arrow"
        shape2 = "Seta"
        caneta.shape(shape)
    if escolha_caneta == 2:
        shape = "blank"
        shape2 = "Invisível"
        caneta.shape(shape)
    if escolha_caneta == 3:
        shape = "circle"
        shape2 = "Circulo"
        caneta.shape(shape)
    if escolha_caneta == 4:
        shape = "classic"
        shape2 = "Classica"
        caneta.shape(shape)
    if escolha_caneta == 5:
        shape = "square"
        shape2 = "Quadrado"
        caneta.shape(shape)
    if escolha_caneta == 6:
        shape = "triangle"
        shape2 = "Triangulo"
        caneta.shape(shape)
    if escolha_caneta == 7:
        shape = "turtle"
        shape2 = "Tartaruga"
        caneta.shape(shape)

    # POSIÇÃO X
    posicao_x = int(
        turtle.numinput(
            "POSIÇÃO EM X",
            "Qual será a posição em X do seu desenho?:\nOBS:VOCÊ SÓ PODE ESCOLHER ENTRE -150 e 150!",
            minval=-300,
            maxval=300,
        )
    )

    # POSIÇÃO Y
    posicao_y = int(
        turtle.numinput(
            "POSIÇÃO EM Y",
            "Qual será a posição em Y do seu desenho?:\nOBS:VOCÊ SÓ PODE ESCOLHER ENTRE -300 e 300!",
            minval=-300,
            maxval=300,
        )
    )
    caneta.setpos(posicao_x, posicao_y)

    # ORIENTAÇÃO DA CANETA
    escolha_orientacao = int(
        turtle.numinput(
            "ORIENTAÇÃO INICIAL",
            "Qual será a orientação em graus que você gostaria que seu desenho comece a ser desenhado?\n 1)0°\n 2)30°\n 3)60°\n 4)90°\n 5)120°\n 6)150°\n 7)180°\n 8)210°\n 9)240°\n 10)270°\n 11)300°\n 12)330°\n Qual você deseja?:",
            minval=1,
            maxval=12,
        )
    )

    if escolha_orientacao == 1:
        orientação = 0
    if escolha_orientacao == 2:
        orientação = 30
    if escolha_orientacao == 3:
        orientação = 60
    if escolha_orientacao == 4:
        orientação = 90
    if escolha_orientacao == 5:
        orientação = 120
    if escolha_orientacao == 6:
        orientação = 150
    if escolha_orientacao == 7:
        orientação = 180
    if escolha_orientacao == 8:
        orientação = 210
    if escolha_orientacao == 9:
        orientação = 240
    if escolha_orientacao == 10:
        orientação = 270
    if escolha_orientacao == 11:
        orientação = 300
    if escolha_orientacao == 12:
        orientação = 330

    # COR
    escolha_de_cor = int(
        turtle.numinput(
            "COR DO DESENHO",
            "Qual será a cor do seu desenho?\n 1)Branco?\n 2)Roxo?\n 3)Rosa?\n 4)Amarelo?\n 5)Vermelho?\n 6)Verde?\n 7)Preto?\n 8)Marrom?\n 9)Laranja?\n 10)Ciano?\n Qual você deseja?:",
            minval=1,
            maxval=10,
        )
    )

    if escolha_de_cor == 1:
        cor = "white"
        cor2 = "Branco"
    if escolha_de_cor == 2:
        cor = "medium purple"
        cor2 = "Roxo"
    if escolha_de_cor == 3:
        cor = "deep pink"
        cor2 = "Rosa"
    if escolha_de_cor == 4:
        cor = "yellow"
        cor2 = "Amarelo"
    if escolha_de_cor == 5:
        cor = "red"
        cor2 = "Vermelho"
    if escolha_de_cor == 6:
        cor = "lime green"
        cor2 = "Verde"
    if escolha_de_cor == 7:
        cor = "black"
        cor2 = "Preto"
    if escolha_de_cor == 8:
        cor = "sienna"
        cor2 = "Marrom"
    if escolha_de_cor == 9:
        cor = "coral"
        cor2 = "Laranja"
    if escolha_de_cor == 10:
        cor = "cyan"
        cor2 = "Ciano"
    caneta.fillcolor(cor)
    caneta.begin_fill()
    caneta.pendown()
    caneta.left(orientação)
    cateto1 = int(
        turtle.numinput(
            "Qual é o primeiro Cateto?", "Insira o valor do primeiro Cateto:"
        )
    )
    cateto2 = int(
        turtle.numinput("Qual é o segundo Cateto?", "Insira o valor do segundo Cateto:")
    )
    caneta.fd(cateto1)
    caneta.left(90)
    caneta.fd(cateto2)
    caneta.setposition(posicao_x, posicao_y)
    caneta.penup()
    caneta.home()
    caneta.end_fill()
    dados_desenho.append("A figura escolhida foi o Triângulo Retângulo")
    dados_desenho.append((f"A caneta escolhida foi: {shape2}"))
    dados_desenho.append((f"A posição escolhida foi: {posicao_x,posicao_y}"))
    dados_desenho.append((f"A orientação escolhida foi: {orientação}°"))
    dados_desenho.append((f"Cor escolhida:{cor2}"))
    dados_desenho.append((f"O tamano do primeiro cateto é: {cateto1}"))
    dados_desenho.append((f"O tamano do segundo cateto é: {cateto2}"))


def Circulo():
    # ESCOLHA DA CANETA
    escolha_caneta = turtle.numinput(
        "FORMATO DA CANETA",
        "Qual o formato da caneta que você deseja usar?\n Você pode escolher:\n 1)Seta\n 2)Invisível\n 3)Círculo\n 4)Clássica\n 5)Quadrado\n 6)Triângulo\n 7)Tartaruga\n Qual você deseja?:",
        minval=1,
        maxval=7,
    )

    if escolha_caneta == 1:
        shape = "arrow"
        shape2 = "Seta"
        caneta.shape(shape)
    if escolha_caneta == 2:
        shape = "blank"
        shape2 = "Invisível"
        caneta.shape(shape)
    if escolha_caneta == 3:
        shape = "circle"
        shape2 = "Circulo"
        caneta.shape(shape)
    if escolha_caneta == 4:
        shape = "classic"
        shape2 = "Classica"
        caneta.shape(shape)
    if escolha_caneta == 5:
        shape = "square"
        shape2 = "Quadrado"
        caneta.shape(shape)
    if escolha_caneta == 6:
        shape = "triangle"
        shape2 = "Triangulo"
        caneta.shape(shape)
    if escolha_caneta == 7:
        shape = "turtle"
        shape2 = "Tartaruga"
        caneta.shape(shape)
    # POSIÇÃO X
    posicao_x = int(
        turtle.numinput(
            "POSIÇÃO EM X",
            "Qual será a posição em X do seu desenho?:\nOBS:VOCÊ SÓ PODE ESCOLHER ENTRE -300 e 300!",
            minval=-300,
            maxval=300,
        )
    )

    # POSIÇÃO Y
    posicao_y = int(
        turtle.numinput(
            "POSIÇÃO EM Y",
            "Qual será a posição em Y do seu desenho?:\nOBS:VOCÊ SÓ PODE ESCOLHER ENTRE 0 e 300!",
            minval=-300,
            maxval=300,
        )
    )
    caneta.setpos(posicao_x, posicao_y)

    # ORIENTAÇÃO DA CANETA
    escolha_orientacao = int(
        turtle.numinput(
            "ORIENTAÇÃO INICIAL",
            "Qual será a orientação em graus que você gostaria que seu desenho comece a ser desenhado?\n 1)0°\n 2)30°\n 3)60°\n 4)90°\n 5)120°\n 6)150°\n 7)180°\n 8)210°\n 9)240°\n 10)270°\n 11)300°\n 12)330°\n Qual você deseja?:",
            minval=1,
            maxval=12,
        )
    )

    if escolha_orientacao == 1:
        orientação = 0
    if escolha_orientacao == 2:
        orientação = 30
    if escolha_orientacao == 3:
        orientação = 60
    if escolha_orientacao == 4:
        orientação = 90
    if escolha_orientacao == 5:
        orientação = 120
    if escolha_orientacao == 6:
        orientação = 150
    if escolha_orientacao == 7:
        orientação = 180
    if escolha_orientacao == 8:
        orientação = 210
    if escolha_orientacao == 9:
        orientação = 240
    if escolha_orientacao == 10:
        orientação = 270
    if escolha_orientacao == 11:
        orientação = 300
    if escolha_orientacao == 12:
        orientação = 330

    # COR
    escolha_de_cor = int(
        turtle.numinput(
            "COR DO DESENHO",
            "Qual será a cor do seu desenho?\n 1)Branco?\n 2)Roxo?\n 3)Rosa?\n 4)Amarelo?\n 5)Vermelho?\n 6)Verde?\n 7)Preto?\n 8)Marrom?\n 9)Laranja?\n 10)Ciano?\n Qual você deseja?:",
            minval=1,
            maxval=10,
        )
    )

    if escolha_de_cor == 1:
        cor = "white"
        cor2 = "Branco"
    if escolha_de_cor == 2:
        cor = "medium purple"
        cor2 = "Roxo"
    if escolha_de_cor == 3:
        cor = "deep pink"
        cor2 = "Rosa"
    if escolha_de_cor == 4:
        cor = "yellow"
        cor2 = "Amarelo"
    if escolha_de_cor == 5:
        cor = "red"
        cor2 = "Vermelho"
    if escolha_de_cor == 6:
        cor = "lime green"
        cor2 = "Verde"
    if escolha_de_cor == 7:
        cor = "black"
        cor2 = "Preto"
    if escolha_de_cor == 8:
        cor = "sienna"
        cor2 = "Marrom"
    if escolha_de_cor == 9:
        cor = "coral"
        cor2 = "Laranja"
    if escolha_de_cor == 10:
        cor = "cyan"
        cor2 = "Ciano"

    caneta.fillcolor(cor)
    caneta.begin_fill()
    caneta.pendown()
    raio = int(
        turtle.numinput(
            "Qual é o raio do seu Círculo?", "Insira o valor do raio do Círculo:"
        )
    )
    caneta.circle(raio)
    caneta.penup()
    caneta.home()
    caneta.end_fill()
    dados_desenho.append("A figura escolhida foi o Círculo")
    dados_desenho.append((f"A caneta escolhida foi: {shape2}"))
    dados_desenho.append((f"A posição escolhida foi: {posicao_x,posicao_y}"))
    dados_desenho.append((f"A orientação escolhida foi: {orientação}°"))
    dados_desenho.append((f"Cor escolhida:{cor2}"))
    dados_desenho.append((f"O tamano do raio é: {raio}"))


def Poligono():
    # ESCOLHA DA CANETA
    escolha_caneta = turtle.numinput(
        "FORMATO DA CANETA",
        "Qual o formato da caneta que você deseja usar?\n Você pode escolher:\n 1)Seta\n 2)Invisível\n 3)Círculo\n 4)Clássica\n 5)Quadrado\n 6)Triângulo\n 7)Tartaruga\n Qual você deseja?:",
        minval=1,
        maxval=7,
    )

    if escolha_caneta == 1:
        shape = "arrow"
        shape2 = "Seta"
        caneta.shape(shape)
    if escolha_caneta == 2:
        shape = "blank"
        shape2 = "Invisível"
        caneta.shape(shape)
    if escolha_caneta == 3:
        shape = "circle"
        shape2 = "Circulo"
        caneta.shape(shape)
    if escolha_caneta == 4:
        shape = "classic"
        shape2 = "Classica"
        caneta.shape(shape)
    if escolha_caneta == 5:
        shape = "square"
        shape2 = "Quadrado"
        caneta.shape(shape)
    if escolha_caneta == 6:
        shape = "triangle"
        shape2 = "Triangulo"
        caneta.shape(shape)
    if escolha_caneta == 7:
        shape = "turtle"
        shape2 = "Tartaruga"
        caneta.shape(shape)

    # POSIÇÃO X
    posicao_x = int(
        turtle.numinput(
            "POSIÇÃO EM X",
            "Qual será a posição em X do seu desenho?:\nOBS:VOCÊ SÓ PODE ESCOLHER ENTRE -300 e 300!",
            minval=-300,
            maxval=300,
        )
    )

    # POSIÇÃO Y
    posicao_y = int(
        turtle.numinput(
            "POSIÇÃO EM Y",
            "Qual será a posição em Y do seu desenho?:\nOBS:VOCÊ SÓ PODE ESCOLHER ENTRE 0 e 300!",
            minval=-300,
            maxval=300,
        )
    )
    caneta.setpos(posicao_x, posicao_y)

    # ORIENTAÇÃO DA CANETA
    escolha_orientacao = int(
        turtle.numinput(
            "ORIENTAÇÃO INICIAL",
            "Qual será a orientação em graus que você gostaria que seu desenho comece a ser desenhado?\n 1)0°\n 2)30°\n 3)60°\n 4)90°\n 5)120°\n 6)150°\n 7)180°\n 8)210°\n 9)240°\n 10)270°\n 11)300°\n 12)330°\n Qual você deseja?:",
            minval=1,
            maxval=12,
        )
    )

    if escolha_orientacao == 1:
        orientação = 0
    if escolha_orientacao == 2:
        orientação = 30
    if escolha_orientacao == 3:
        orientação = 60
    if escolha_orientacao == 4:
        orientação = 90
    if escolha_orientacao == 5:
        orientação = 120
    if escolha_orientacao == 6:
        orientação = 150
    if escolha_orientacao == 7:
        orientação = 180
    if escolha_orientacao == 8:
        orientação = 210
    if escolha_orientacao == 9:
        orientação = 240
    if escolha_orientacao == 10:
        orientação = 270
    if escolha_orientacao == 11:
        orientação = 300
    if escolha_orientacao == 12:
        orientação = 330

    # COR
    escolha_de_cor = int(
        turtle.numinput(
            "COR DO DESENHO",
            "Qual será a cor do seu desenho?\n 1)Branco?\n 2)Roxo?\n 3)Rosa?\n 4)Amarelo?\n 5)Vermelho?\n 6)Verde?\n 7)Preto?\n 8)Marrom?\n 9)Laranja?\n 10)Ciano?\n Qual você deseja?:",
            minval=1,
            maxval=10,
        )
    )

    if escolha_de_cor == 1:
        cor = "white"
        cor2 = "Branco"
    if escolha_de_cor == 2:
        cor = "medium purple"
        cor2 = "Roxo"
    if escolha_de_cor == 3:
        cor = "deep pink"
        cor2 = "Rosa"
    if escolha_de_cor == 4:
        cor = "yellow"
        cor2 = "Amarelo"
    if escolha_de_cor == 5:
        cor = "red"
        cor2 = "Vermelho"
    if escolha_de_cor == 6:
        cor = "lime green"
        cor2 = "Verde"
    if escolha_de_cor == 7:
        cor = "black"
        cor2 = "Preto"
    if escolha_de_cor == 8:
        cor = "sienna"
        cor2 = "Marrom"
    if escolha_de_cor == 9:
        cor = "coral"
        cor2 = "Laranja"
    if escolha_de_cor == 10:
        cor = "cyan"
        cor2 = "Ciano"
    caneta.fillcolor(cor)
    caneta.begin_fill()
    caneta.pendown()
    n_lados = int(
        turtle.numinput(
            "Qual é o número de lados do seu Poligono?",
            "Insira o número de lados do Poligono:",
            minval=3,
        )
    )
    tam_lado = int(
        turtle.numinput(
            "Qual é o tamanho dos lados?",
            "Insira o tamanho dos lados do Poligono:",
        )
    )

    for i in range(n_lados):
        caneta.fd(tam_lado)
        caneta.left(360 / n_lados)
    caneta.penup()
    caneta.home()
    caneta.end_fill()
    dados_desenho.append("A figura escolhida foi o Poligono Regular")
    dados_desenho.append((f"A caneta escolhida foi: {shape2}"))
    dados_desenho.append((f"A posição escolhida foi: {posicao_x,posicao_y}"))
    dados_desenho.append((f"A orientação escolhida foi: {orientação}°"))
    dados_desenho.append((f"Cor escolhida:{cor2}"))
    dados_desenho.append((f"O Polígono tem {n_lados} lados!"))
    dados_desenho.append(f"O tamanho dos lados do Poligono é: {tam_lado}")


# MENU
while loop:
    escolha = int(
        turtle.numinput(
            "DESENHO VETORIAL",
            "O que você gostaria de desenhar hoje?\n 1)Retângulo?\n 2)Triângo Retângulo?\n 3)Circulo?\n 4)Poligono Regular?\n 5)Sair?\n Qual você deseja?:",
            minval=1,
            maxval=5,
        )
    )
    if escolha == 1:
        Retângulo()

    if escolha == 2:
        Triângulo()

    if escolha == 3:
        Circulo()

    if escolha == 4:
        Poligono()

    if escolha == 5:
        loop = False
        caneta.shape("blank")
        caneta.penup()
        fonte = ("Comic Sans", 50, "italic")
        caneta.write("OBRIGADO!", False, "center", fonte)
        caneta.fd(40)
        sleep(3)
        turtle.Screen().bye()

    escolha_2 = int(
        turtle.numinput(
            "Deseja continuar?",
            "Você deseja continuar?\n 1)Sim\n 2)Não",
            minval=1,
            maxval=2,
        )
    )
    if escolha_2 == 1:
        escolha_3 = int(
            turtle.numinput(
                "Deseja apagar?",
                "Deseja apagar o que já foi desenhado?\n 1)Sim\n 2)Não",
                minval=1,
                maxval=2,
            )
        )
        if escolha_3 == 1:
            caneta.clear()

    else:
        loop = False
        caneta.clear()
        caneta.shape("blank")
        caneta.right(90)
        caneta.penup()
        fonte = ("Comic Sans", 50, "bold")
        fonte2 = ("Comic Sans", 40, "normal")
        fonte3 = ("Comic Sans", 10, "normal")
        caneta.write("OBRIGADO!", False, "center", fonte)
        sleep(10)
        turtle.Screen().bye()

janela.exitonclick()
