from pyboy import PyBoy


pyboy = PyBoy('C:/Users/jiaoj/Desktop/口袋妖怪.金(英文).gbc')
while not pyboy.tick():
    pass