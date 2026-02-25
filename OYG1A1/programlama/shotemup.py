# shotemup.py
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pygame
import random

#oyun sabitlerinin tanimlanmasi

GENISLIK = 480
YUKSEKLIK = 600
FPS = 30
BASLIK = "iskelet Kod"

# Kullanışlı renklerini tanimlanması
BEYAZ = (255, 255, 255)
SIYAH = (0, 0, 0)
KIRMIZI = (255, 0, 0)
YESIL = (0, 255, 0)
MAVI = (0, 0, 255)
RENK1=(200,75,56)

# pygame öğelerinin ilklenmesi ve pencere yaratılması
pygame.init()
pygame.mixer.init()
ekran = pygame.display.set_mode((GENISLIK, YUKSEKLIK))
pygame.display.set_caption(BASLIK)
saat = pygame.time.Clock()

# spritelar
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((50,40))
        self.image.fill(RENK1)
        self.rect=self.image.get_rect()
        self.rect.centerx=GENISLIK//2
        self.rect.bottom=YUKSEKLIK-10
        self.speed=0        
        
    def update(self):
        self.speed=0
        key_info=pygame.key.get_pressed()
        if key_info[pygame.K_LEFT]:
            self.speed=-5
        if key_info[pygame.K_RIGHT]:
            self.speed=5
        
        self.rect.x+=self.speed
                
        if self.rect.right<0:
            self.rect.left=GENISLIK
        if self.rect.left>GENISLIK:
            self.rect.right=0
        
       
    def shoot(self):
        bullet=Bullet(self.rect.centerx,self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((10,40))
        self.image.fill((128,128,128))
        self.rect=self.image.get_rect()
        self.rect.bottom=y
        self.rect.centerx=x
        self.speedy=-10       
        
        
    def update(self):
        self.rect.y+=self.speedy
        if self.rect.bottom<0:
            self.kill()


class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(KIRMIZI)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(GENISLIK - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(5, 15)
        self.speedx = random.randrange(-3, 3)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > YUKSEKLIK + 10 or self.rect.left < -25 or self.rect.right > GENISLIK + 20:
            self.rect.x = random.randrange(GENISLIK - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)
        
#sprite yapılarının gruplanması
all_sprites=pygame.sprite.Group()
bullets=pygame.sprite.Group()
mobs=pygame.sprite.Group()
player1=Player()
all_sprites.add(player1)
for i in range(5):
    m=Mob()
    all_sprites.add(m)
    mobs.add(m)

# Oyun döngüsü
calisma = True
while calisma:
    # Oyun akış hızının belirlenmesi
    saat.tick(FPS)
    # Giriş işlemeleri (olaylar)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            calisma = False
        if event.type==pygame.KEYUP:
           if event.key==pygame.K_SPACE:
               pass
        if event.type==pygame.MOUSEBUTTONDOWN:
            sol,orta,sag=pygame.mouse.get_pressed()
            if sol:
                player1.shoot()
     
    # Güncelleme
    all_sprites.update()
    hits_g=pygame.sprite.groupcollide(mobs,bullets,True,True)
    for h in hits_g:
        m=Mob()
        all_sprites.add(m)
        mobs.add(m)
    
    hits_p=pygame.sprite.spritecollide(player1,mobs,False)
    if hits_p:
        calisma=False
   
    # Çizme / Ekranı tazeleme
    ekran.fill(SIYAH)
   
    all_sprites.draw(ekran)
    # herşeyin çizimi işleminden sonra , ekranın tazelenmesi
    pygame.display.flip()


# Oyundan çıkılması
pygame.quit()
