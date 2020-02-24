import Mine_Board
import Player_Board
import pygame

pygame.init()

window_width = 400
window_height = 400
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Mine Sweeper")
clock = pygame.time.Clock()

row = 20
col = 20
mine = 50
mineB = Mine_Board.Mine_Board(row, col, mine)
playerB = Player_Board.Player_Board(row, col, mine)

# 이미지 저장
img_list = []
for i in range(12):
    img_list.append(pygame.transform.scale(pygame.image.load("image/"+str(i)+".jpg").convert(), (int(window_width / row), int(window_height / col))))

# 이미지 출력 함수
def set_Image(img, x, y):
    screen.blit(img, (x, y))

# 메인 게임 루프
def game_loop():
    loop = True
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONUP and not(playerB.pause):
                mousex, mousey = event.pos
                x, y = int(mousex/row), int(mousey/col)
                # 좌클릭
                if event.button == 1:
                    playerB.open(x, y, mineB)

                # 우클릭
                elif event.button == 3:
                    if playerB.get_cell(x, y) == 10:
                        playerB.set_cell(x, y, 11)
                    elif playerB.get_cell(x, y) == 11:
                        playerB.set_cell(x, y, 10)

        # 이미지 처리
        for x in range(row):
            for y in range(col):
                set_Image(img_list[playerB.get_cell(x, y)], x*row, y*col)

        clock.tick(30)
        pygame.display.update()
        loop = not(playerB.gameover)


print("Mine Sweeper!")
game_loop()
pygame.quit()
quit()
