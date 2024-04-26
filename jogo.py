import pygame
import random

def obstaculos():
    tipos = [
        'peixe',
    ]
    velocidade = random.randint(1, 8)
    tipo = random.choice(tipos)
    tamanho = random.randint(1, 5)

    return {
        "posicao": [random.randint(200, 600), random.randint(200, 400)],
        "velocidade": velocidade,
        "tipo": tipo,
        "tamanho": tamanho,
        # "vidas": vidas, 
        "direcao": pygame.Vector2(1, 1),
        #"contorno": contorno
    }

def inimigos():
    tipos = [
        'peixe',
    ]
    velocidade = random.randint(1, 4)
    tipo = random.choice(tipos)
    tamanho = random.randint(1, 5)

    return {
        "posicao": [random.randint(200, 600), random.randint(200, 400)],
        "velocidade": velocidade,
        "tipo": tipo,
        "tamanho": tamanho,
        # "vidas": vidas, 
        "direcao": pygame.Vector2(1, 1),
        #"contorno": contorno
    }

def verificaCliqueInimigos(posicao, listadeInimigos): 
    global pontuacao
    for inimigos in listadeInimigos: #Vai verificar bolinha por bolinha
        #Desenha um retangulo temporário para verificar se o click foi dentro da bola
        retanguloTemporario = pygame.draw.circle(
            tela,
            inimigos["cor"],
            inimigos["posicao"],
            inimigos["tamanho"],
        )

        recebeuClick = retanguloTemporario.collidepoint(posicao) 

        del retanguloTemporario

        if recebeuClick:
            inimigos["vidas"] -= 1

        if verificaCliqueInimigos["vidas"] <= 0: 
            pontuacao += 1
            listadeInimigos.remove(inimigos)
            
            pygame.mixer.music.load("sons/ainn-cafezinho.mp3")
            pygame.mixer.music.set_volume(1)
            pygame.mixer.music.play()
            pygame.event.wait()

pygame.init()
tamanho = (400, 700)
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("Jogo")
relogio = pygame.time.Clock()


tipo = ['tipos']
posicao = [150, 0]
raio = 50
velocidade = 0
cor_tela = (10, 10, 10) 

#Lista de bolas
listadeInimigos = []

#Evento para o tempo
novoInimigoEvent = pygame.USEREVENT + 1

pontuacao = 0

#cria uma fonta
fonte = pygame.font.Font(None, 200)
fontePeixe = pygame.font.Font(None, 15)


#Cria o evento a cada 10 segundos
pygame.time.set_timer(novoInimigoEvent, 1000)



# listaPlanoFundos = []
# for index in range(1, 10):
#     imagem = pygame.image.load(f"assets/planofundo/cemiterio/{index}.png")
#     imagem = pygame.transform.scale(imagem, tamanho).convert_alpha()
#     listaPlanoFundos.append(imagem)

while True:
    # Pega os eventos que estão acontecendo
    for evento in pygame.event.get():
        if evento.type == novoInimigoEvent:
            #Adiciona uma nova bola na lista de bolas
            listadeInimigos.append(novoInimigoEvent())

        # Se o evento for de fechar a tela
        if evento.type == pygame.QUIT:
            pygame.quit() # Fecha o Pygame
            exit() # Fecha o programa

        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1: #Botao esquedo do mouse
                #Verificar se o click foi dentro de algum circulo
                #Passa a posição do click para a função
                verificaCliqueInimigos(evento.pos, listadeInimigos)

    #######################jogo acontece aqui dentro ############################# 
    
    # Pinta a tela de branco
    tela.fill((cor_tela))

    pygame.display.update()

    # Controla a quantidade de FPS
    relogio.tick(60)
