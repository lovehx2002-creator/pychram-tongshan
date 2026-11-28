cars = ['audi', 'kaidilake', 'bmw', 'meisii']

for car in cars:
    if car == 'audi':
        print(car.upper())
    else:
        print(car)


car = "Audi"
if car.lower() == "AUDI".lower():
    print('this is true')
    
request_food = '汉堡'
if request_food != '薯条':
    print('你还咩有薯条')

bool = 6 > 7
print(bool)

requested_food = ['zhaji', 'hanbao', 'shutiao']
print('hanbao' in requested_food)
print('qiangbaojimihua' not  in  requested_food)