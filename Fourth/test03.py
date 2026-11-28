players = ['zhangsan', 'lisi', 'wangwu', 'zhaoliu', 'zhengqi']

print(players[0:2])
print(players[1:])
print(players[:])

print(players[2])

print(players[-2:]) #从倒数第二个往后面一直取完

print(players[0::2]) #切片当中也可以指定相应的步长

for player in players[0:3]:
    print(player.title())

myfood = ['汉堡', '炸鸡', '薯条']
#friendfood = myfood #这两个列表是一样的列表
friendfood = myfood[:]  #这个才是列表的复制，生成了两个列表
print(myfood)
print(friendfood)

myfood.append('香肠')
print(myfood)
print(friendfood)