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
        self.image.fill(YESIL)
        self.rect=self.image.get_rect()
        self.rect.centerx=GENISLIK//2
        self.rect.bottom=YUKSEKLIK-10
        self.speedx=0
    def update(self):
        self.speedx=0
        key_states=pygame.key.get_pressed()
     
        if key_states[pygame.K_a]:
            self.speedx=-5
        if key_states[pygame.K_d]:
            self.speedx=5
        # if key_states[pygame.K_SPACE] :
        #     self.shoot()
        self.rect.x+=self.speedx
    def shoot(self):
        bullet=Bullet(self.rect.centerx,self.rect.top)
        all_sprites.add(bullet)
        bullet_sprites.add(bullet)

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((5,30))
        self.image.fill((67,32,125))
        self.rect=self.image.get_rect()
        self.rect.centerx=x
        self.rect.bottom=y
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
        # if self.rect.top>YUKSEKLIK:
        #     self.kill()
        
#sprite yapılarının gruplanması
all_sprites=pygame.sprite.Group()
bullet_sprites=pygame.sprite.Group()
mobs_sprites=pygame.sprite.Group()
player1=Player()
all_sprites.add(player1)
for i in range(5):
    mob=Mob()
    all_sprites.add(mob)
    mobs_sprites.add(mob)
# Oyun döngüsü
calisma = True
while calisma:
    # Oyun akış hızının belirlenmesi
    saat.tick(FPS)
    # Giriş işlemeleri (olaylar)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            calisma = False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                player1.shoot()
                

    # Güncelleme
    all_sprites.update()
    hits=pygame.sprite.groupcollide(mobs_sprites,bullet_sprites,True,True)
    for hit in hits:
        mob=Mob()
        all_sprites.add(mob)
        mobs_sprites.add(mob)
    
    hits=pygame.sprite.spritecollide(player1,mobs_sprites,False)
    if hits:
        calisma=False
    # Çizme / Ekranı tazeleme
    ekran.fill(SIYAH)
    all_sprites.draw(ekran)

    # herşeyin çizimi işleminden sonra , ekranın tazelenmesi
    pygame.display.flip()


# Oyundan çıkılması
pygame.quit()
