from tools import coins
from tools import data
price = data.read_money('Digite o Preco: R$')
coins.summary(price, 30, 90)