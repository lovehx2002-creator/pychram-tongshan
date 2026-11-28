value = "haha"

if value:
    print("True")
else:
    print("False")

have_food = ['  hanbao', 'shutiao', 'kele']
request_food = ['hanbao', 'shutiao', 'zhaji']

for food in request_food:
    if food in have_food:
        print(f"{food}我给你点单")
        print(f'点单完成{food}')
    else:
        print(f"没有这个食物{food}")
print("所有点单完成")