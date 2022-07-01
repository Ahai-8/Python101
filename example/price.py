price = int(input('Please input a price: '))

coin20 = price//20
price = price % 20
coin10 = price // 10
price = price % 10
coin5 = price//5
coin1 = price % 5

print('You should pay:')
print('20 yuan *', coin20)
print('10 yuan *', coin10)
print(' 5 yuan *', coin5)
print(' 1 yuan *', coin1)
