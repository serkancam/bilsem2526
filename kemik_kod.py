#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pygame

#oyun sabitlerinin tanimlanmasi

GENISLIK = 480
YUKEKLIK = 600
FPS = 30
BASLIK = "iskelet Kod"

# Kullanışlı renklerini tanimlanması
BEYAZ = (255, 255, 255)
SIYAH = (0, 0, 0)
KIRMIZI = (255, 0, 0)
YESIL = (0, 255, 0)
MAVI = (0, 0, 255)

# pygame öğelerinin ilklenmesi ve pencere yaratılması
pygame.init()
pygame.mixer.init()
ekran = pygame.display.set_mode((GENISLIK, YUKEKLIK))
pygame.display.set_caption(BASLIK)
saat = pygame.time.Clock()

# Oyun döngüsü
calisma = True
while calisma:
    # Oyun akış hızının belirlenmesi
    saat.tick(FPS)
    # Giriş işlemeleri (olaylar)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            calisma = False

    # Güncelleme
    # Çizme / Ekranı tazeleme
    ekran.fill(BEYAZ)

    # herşeyin çizimi işleminden sonra , ekranın tazelenmesi
    pygame.display.flip()


# Oyundan çıkılması
pygame.quit()
