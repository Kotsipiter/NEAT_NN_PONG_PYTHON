import pygame,sys,random
pygame.init()

WIDTH, HEIGHT=700,500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

FPS = 60

WHITE = (255,255,255)
BLACK = (0,0,0)

PADDLE_WIDTH,PADDLE_HEIGHT = 20,100
class Paddle:
    COLOR = WHITE
    vel = 7
    
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def draw(self,win):
        pygame.draw.rect(win,self.COLOR,(self.x,self.y,self.width,self.height))
    def move(self,up=True):
        if up:
            self.y -= self.vel
        else:
            self.y += self.vel
        
    

def draw(win,paddles):
    win.fill(BLACK)
    for paddle in paddles:
        paddle.draw(win)
    pygame.draw.aaline(win,WHITE,(WIDTH/2,0),(WIDTH/2,HEIGHT))
    pygame.display.update()
    
def handle_pandle_movement(keys,left_paddle,right_paddle):
    if keys[pygame.K_w] and left_paddle.y - left_paddle.vel >= 0:
        left_paddle.move(up=True)
    if keys[pygame.K_s] and left_paddle.y + left_paddle.vel + left_paddle.height <= HEIGHT:
        left_paddle.move(up=False)
    if keys[pygame.K_a] and right_paddle.y - right_paddle.vel >= 0:
        right_paddle.move(up=True)
    if keys[pygame.K_d] and right_paddle.y + right_paddle.vel + right_paddle.height <= HEIGHT:
        right_paddle.move(up=False)

def main():
    run = True
    clock = pygame.time.Clock()
    left_paddle = Paddle(10,HEIGHT//2-PADDLE_HEIGHT//2,PADDLE_WIDTH,PADDLE_HEIGHT)
    right_paddle = Paddle(WIDTH-10-PADDLE_WIDTH,HEIGHT//2-PADDLE_HEIGHT//2,PADDLE_WIDTH,PADDLE_HEIGHT)
    
    while run:
        clock.tick(FPS)
        draw(WIN,[left_paddle,right_paddle])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            
            keys = pygame.key.get_pressed()
            handle_pandle_movement(keys,left_paddle,right_paddle)
            
    pygame.quit()

if __name__=='__main__':
    main()

