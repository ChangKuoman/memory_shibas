import pygame
import random
pygame.font.init()
pygame.mixer.init()
pygame.display.set_caption("MEMORY SHIBAS")
SHIBA_ICON = pygame.transform.scale(pygame.image.load("assets/shiba_inu_6.jpg"), (32, 32))
pygame.display.set_icon(SHIBA_ICON)

# colors
BLACK = (0, 0, 0)

# fonts
MOVEMENTS_FONT = pygame.font.SysFont("britannic", 20)
WIN_FONT = pygame.font.SysFont("britannic", 100)
TITLE_FONT = pygame.font.SysFont("britannic", 40)

# constants
WIDTH, HEIGHT = 500, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60

# images
WHITE_SQUARE = pygame.transform.scale(pygame.image.load("assets/white_square.jpg"), (60, 60))
YELLOW_BACKGROUND = pygame.transform.scale(pygame.image.load("assets/yellow_background.jpg"), (WIDTH, HEIGHT))
SHIBA_INU_1 = pygame.transform.scale(pygame.image.load("assets/shiba_inu_1.jpg"), (60, 60))
SHIBA_INU_2 = pygame.transform.scale(pygame.image.load("assets/shiba_inu_2.jpg"), (60, 60))
SHIBA_INU_3 = pygame.transform.scale(pygame.image.load("assets/shiba_inu_3.jpg"), (60, 60))
SHIBA_INU_4 = pygame.transform.scale(pygame.image.load("assets/shiba_inu_4.jpg"), (60, 60))
SHIBA_INU_5 = pygame.transform.scale(pygame.image.load("assets/shiba_inu_5.jpg"), (60, 60))
SHIBA_INU_6 = pygame.transform.scale(pygame.image.load("assets/shiba_inu_6.jpg"), (60, 60))
SHIBA_INU_7 = pygame.transform.scale(pygame.image.load("assets/shiba_inu_7.jpg"), (60, 60))
SHIBA_INU_8 = pygame.transform.scale(pygame.image.load("assets/shiba_inu_8.jpg"), (60, 60))
SHIBA_INU_9 = pygame.transform.scale(pygame.image.load("assets/shiba_inu_9.jpg"), (60, 60))
SHIBA_INU_10 = pygame.transform.scale(pygame.image.load("assets/shiba_inu_10.jpg"), (60, 60))
SHIBA_INU_11 = pygame.transform.scale(pygame.image.load("assets/shiba_inu_11.jpg"), (60, 60))
SHIBA_INU_12 = pygame.transform.scale(pygame.image.load("assets/shiba_inu_12.jpg"), (60, 60))
SHIBA_INU_13 = pygame.transform.scale(pygame.image.load("assets/shiba_inu_13.jpg"), (60, 60))
SHIBA_INU_14 = pygame.transform.scale(pygame.image.load("assets/shiba_inu_14.jpg"), (60, 60))
SHIBA_INU_15 = pygame.transform.scale(pygame.image.load("assets/shiba_inu_15.jpg"), (60, 60))
SHIBA_INU_16 = pygame.transform.scale(pygame.image.load("assets/shiba_inu_16.jpg"), (60, 60))
SHIBA_INU_17 = pygame.transform.scale(pygame.image.load("assets/shiba_inu_17.jpg"), (60, 60))
SHIBA_INU_18 = pygame.transform.scale(pygame.image.load("assets/shiba_inu_18.jpg"), (60, 60))

def draw_window(stack, dictionary, lista, counter):
    WINDOW.blit(YELLOW_BACKGROUND, (0, 0))

    for i in range(20, 421, 80):
        for j in range(20, 421, 80):
            WINDOW.blit(WHITE_SQUARE, (i, j))

    for i in stack:
        WINDOW.blit(dictionary[(i.x, i.y)], (i.x, i.y))

    for i in lista:
        WINDOW.blit(dictionary[(i.x, i.y)], (i.x, i.y))

    movements_text = MOVEMENTS_FONT.render(f"Movimientos: {counter//2}", 1, BLACK)
    WINDOW.blit(movements_text, (20, 550))
    title_text = TITLE_FONT.render("MEMORY SHIBAS", 1, BLACK)
    WINDOW.blit(title_text, (20, 500))

    pygame.display.update()

def draw_win_text():
    win_text = WIN_FONT.render("¡GANASTE!", 1, BLACK)
    WINDOW.blit(win_text, (20, 250))
    pygame.display.update()
    pygame.time.delay(5000)

def main():
    run = True
    clock = pygame.time.Clock()

    imagenes = [
        SHIBA_INU_1, SHIBA_INU_1,
        SHIBA_INU_2, SHIBA_INU_2,
        SHIBA_INU_3, SHIBA_INU_3,
        SHIBA_INU_4, SHIBA_INU_4,
        SHIBA_INU_5, SHIBA_INU_5,
        SHIBA_INU_6, SHIBA_INU_6,
        SHIBA_INU_7, SHIBA_INU_7,
        SHIBA_INU_8, SHIBA_INU_8,
        SHIBA_INU_9, SHIBA_INU_9,
        SHIBA_INU_10, SHIBA_INU_10,
        SHIBA_INU_11, SHIBA_INU_11,
        SHIBA_INU_12, SHIBA_INU_12,
        SHIBA_INU_13, SHIBA_INU_13,
        SHIBA_INU_14, SHIBA_INU_14,
        SHIBA_INU_15, SHIBA_INU_15,
        SHIBA_INU_16, SHIBA_INU_16,
        SHIBA_INU_17, SHIBA_INU_17,
        SHIBA_INU_18, SHIBA_INU_18,
    ]
    dictionary = {}
    objetos = []
    stack = []
    lista = []
    counter = 0
    for i in range(20, 421, 80):
        for j in range(20, 421, 80):
            objetos.append(pygame.Rect(i, j, 60, 60))
            objeto = random.choice(imagenes)
            dictionary[(i, j)] = objeto
            imagenes.remove(objeto)

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for i in objetos:
                    if i.collidepoint(pygame.mouse.get_pos()):
                        stack.append(i)
                        objetos.remove(i)
                        counter += 1

        if len(stack) > 2:
            elem = stack.pop()
            if dictionary[(stack[0].x, stack[0].y)] == dictionary[(stack[1].x, stack[1].y)]:
                lista.append(stack[0])
                lista.append(stack[1])
            else:
                objetos += stack
            stack.clear()
            stack.append(elem)

        draw_window(stack, dictionary, lista, counter)
        if len(objetos) == 0:
            draw_win_text()
            break

    pygame.quit()


if __name__ == "__main__":
    main()
