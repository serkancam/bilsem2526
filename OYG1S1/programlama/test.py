import random
import os
ADAM_ASMACA = [
    r"""
  +---+
  |   |
      |
      |
      |
      |
=========
""",
    r"""
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
    r"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
    r"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
"""
]
dosya=open("/home/serkan/Belgeler/bilsem2526/OYG1S1/programlama/sorular.txt",mode="r",encoding="utf-8")
okunan=dosya.read()
print(okunan)
dosya.close()

sorular=okunan.split(",")
# print(sorular)

secilen=random.choice(sorular)
# print(secilen)
os.system("clear")
for i in secilen:
    print("_ ",end="")
    
print(ADAM_ASMACA[4])
input("")
