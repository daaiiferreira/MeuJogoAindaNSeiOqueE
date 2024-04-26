import pygame
import random
import os

pygame.init()
pygame.mixer.music.load("sons/tema3.wav")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

#criar personagem principal
def criaJogador():
    tipos = [
        'sereia'
    ]
    velocidade = 0
    tamanho = 30
    vidas = 3

    return{
        "posicao": [random.randint(200, 600), random.randint(200, 400)],
        "velocidade": velocidade,
        "tipo": tipos,
        "tamanho": tamanho,
        "vidas": vidas, 
    }
    

#criar inimigo
def inimigo():
    tipos = [
        'tubarao',
        'polvo'
    ]
    velocidade = random.randint(2, 4)
    tipo = random.choice(tipos)
    tamanho = random.randint(30, 50)
    vidas = 3

    return {
        "posicao": [random.randint(100, 0), random.randint(300, 0)],
        "velocidade": velocidade,
        "tipo": tipo,
        "tamanho": tamanho,
        "vidas": vidas, 
        "direcao": pygame.Vector2(1, 1),
        "categoria": 'inimigo',
    }

#criar amigos
def criaObstaculo():
    tipos = [
        'peixe',
        'aguaviva'
    ]

    velocidade = random.randint(1, 6)
    tipo = random.choice(tipos)
    tamanho = random.randint(10, 20)
   
    return {
        "posicao": [random.randint(50, 350), random.randint(10, 20)],
        "velocidade": velocidade,
        "tipo": tipo,
        "tamanho": tamanho, 
        "direcao": pygame.Vector2(1, 1),
        "categoria": 'amigo',
        "vidas": 3
    }

def verificaCliqueObstaculo(listaObstaculo):
    global pontuacao 

listaObstaculo = []

listaJogador = []

#amigo_jogado = []

obstaculoEvent = pygame.USEREVENT + 1

personagemEvent = pygame.USEREVENT + 1


#criar tela azul com ondinhas ciano em volta
pygame.init()
tamanho = (400, 750)
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("CrazyOcean")
relogio = pygame.time.Clock()
cor_tela = (0, 0, 255) 

fonte = pygame.font.Font(None, 200)
fonteObstaculo = pygame.font.Font(None, 15)
fonteVidaJogador = pygame.font.Font(None, 30)

pygame.time.set_timer(obstaculoEvent, 1000)

listaImagensFundo = []
for index in range(1):
    imagem = pygame.image.load(f"imagens/fundo/telajogo.png")
    imagem = pygame.transform.flip(imagem, False, True)
    imagem = pygame.transform.scale(imagem, tamanho).convert_alpha()
    listaImagensFundo.append(imagem)


listaImagensPeixe = []
for index in range(1, 7):
    imagem = pygame.image.load(f"imagens/peixe/peixe{index}.png")
    imagem = pygame.transform.flip(imagem, False, True)
    imagem = pygame.transform.scale(imagem, (50, 50)).convert_alpha()
    listaImagensPeixe.append(imagem)

listaImagensAviva = []
for index in range(1, 5):
    imagem = pygame.image.load(f"imagens/aguaviva/aviva{index}.png")
    imagem = pygame.transform.flip(imagem, False, True)
    imagem = pygame.transform.scale(imagem, (50, 50)).convert_alpha()
    listaImagensAviva.append(imagem)

listaImagensPersonagemAndando = []
for index in range(1, 7):
    imagem = pygame.image.load(f"imagens/pers/andando/andando{index}.png")
    imagem = pygame.transform.scale(imagem, (30, 30)).convert_alpha()
    listaImagensPersonagemAndando.append(imagem)



#lógica: mapa corre na vertical, de baixo pra cima. Personagem principal pega peixinhos para alimentar os tubarões para conseguir se defender. Caso não tenha peixinhos, precisa matar o tubarão para avançar.

while True:

    # personagem = [criaJogador]
    # listaImagemJogador = listaImagensPersonagemAndando

    # #if personagem["tipo"] == 'sereia' : listaImagensJogador = listaImagensPersonagemAndando
    # #if obstaculo["tipo"] == 'peixe': listaImagens = listaImagensPeixe 
                
    # imagem = listaImagemJogador[(pygame.time.get_ticks() // 100) % len(listaImagemJogador)]
    # imagem_rect = imagem.get_rect(center=(personagem["posicao"][0] - 30, personagem["posicao"][1] - 30))
    # print(f"{listaImagemJogador}")

    # tela.blit(imagem, imagem_rect)
    # personagem["posicao"][1] == 600
    
    
   
    for evento in pygame.event.get():

        # if evento.type == personagemEvent:

        #         if evento.type == pygame.KEYDOWN:
        #             if evento.key == pygame.K_RIGHT:
        #                 personagem.rect.x += 5
                
        #             elif evento.key == pygame.K_LEFT:
        #                 personagem.rect.x -= 5

                       
        
        # se o evento for de fechar a tela
        if evento.type == pygame.QUIT:
            pygame.quit() #fecha o pygame
            exit() #fecha o programa

        if evento.type == obstaculoEvent:
            listaObstaculo.append(criaObstaculo())           

        
            
            # elif evento.key == pygame.K_SPACE:
            #     if personagem.amigo_jogado is None:
            #         personagem.amigo_jogado = amigo_jogado

    

    tela.fill(cor_tela)

    for i in range(len(listaImagensFundo)):
        tela.blit(listaImagensFundo[i], (0,0))
    
    for obstaculo in listaObstaculo:
        #Desenhar a bola na tela
        # circulo = pygame.draw.circle(
        #     tela,
        #     (0, 255, 0),
        #     obstaculo["posicao"],
        #     obstaculo["tamanho"],
        #     obstaculo["categoria"],        
        # )

        listaImagens = []
        if obstaculo["tipo"] == 'peixe': listaImagens = listaImagensPeixe
        elif obstaculo["tipo"] == 'aguaviva': listaImagens = listaImagensAviva
        #elif obstaculo["tipo"] == 'tubarao': listaImagens = listaImagensTubarao
        #elif obstaculo["tipo"] == 'polvo': listaImagens = listaImagensPolvo

        imagem = listaImagens[(pygame.time.get_ticks() // 100) % len(listaImagens)]
        imagem_rect = imagem.get_rect(center=(obstaculo["posicao"][0] - 30, obstaculo["posicao"][1] - 30))

        tela.blit(imagem, imagem_rect)

        obstaculo["posicao"][1] += 5

        textoObstaculo = fonteObstaculo.render(f"{obstaculo['vidas']}", True, (255, 255, 255))
        textoBolinhaRect = textoObstaculo.get_rect(center=obstaculo["posicao"])
        tela.blit(textoObstaculo, textoBolinhaRect)



        
        
    #tela.fill((cor_tela))
    pygame.display.update()

    # Controla a quantidade de FPS
    relogio.tick(60)

#criar a lógica