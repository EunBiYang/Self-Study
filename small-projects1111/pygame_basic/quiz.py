
import pygame
import random
############################################################################
#기본 초기화 (반드시 해야하는것들)

pygame.init()

#화면크기 설정
screen_width = 500
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption('DDong Game')

#FPS
clock = pygame.time.Clock()


############################################################################


# 1. 사용자 게임 초기화(배경화면, 게임 이미지, 좌표,속도, 폰트)
#배경이미지 불러오기
background = pygame.image.load('D:\\workspace\\small-projects\\pygame_basic\\backgroung.png')

#캐릭터 이미지
character = pygame.image.load('D:\\workspace\\small-projects\\pygame_basic\\character.png')
character_size = character.get_rect().size 
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width/2) - (character_width/2)
character_y_pos = screen_height - character_height

#적 이미지
enemy = pygame.image.load('D:\\workspace\\small-projects\\pygame_basic\\enemy.png')
enemy_size = enemy.get_rect().size 
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = random.randint(0, screen_width - enemy_width)
enemy_y_pos = 0
enemy_speed = 10

#이동위치
to_x = 0
to_y = 0

#속도
character_speed = 1

#폰트



running = True 
while running:
    dt = clock.tick(30)     
    
    # 2.이벤트 처리 (키보드, 마우스)
    for event in pygame.event.get():       
        if event.type == pygame.QUIT:          
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            if event.key == pygame.K_RIGHT:
                to_x += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                to_x = 0
    
    #3.게임 케릭터의 위치 정의
    character_x_pos += to_x *dt
    
    if character_x_pos < 0:
        character_x_pos =0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    enemy_y_pos += enemy_speed #똥이 떨어지게 만드는 코드

    if enemy_y_pos > screen_height:  #화면상에서 떨어졌으면
        enemy_y_pos = 0          #다시 맨위로 올려준다는 의미
        enemy_x_pos = random.randint(0, screen_width - enemy_width)


    
    # 4. 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos
    
    if character_rect.colliderect(enemy_rect):
        print('충돌했습니다')
        running = False

    # 5. 화면에 그리기
    screen.blit(background,(0,0))
    screen.blit(character,(character_x_pos, character_y_pos))
    screen.blit(enemy,(enemy_x_pos,enemy_y_pos))

    pygame.display.update()  #게임화면을 계속해서 다시 그려주는 코드!!

pygame.quit()