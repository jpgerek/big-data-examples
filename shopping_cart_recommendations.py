from mredu import simul
import itertools

data = [
        ('customer-1', 'milk'), ('customer-1','peanut butter'), ('customer-1', 'jelly'), ('customer-1', 'cookies'), ('customer-1', 'eggs'),
        ('customer-2', 'beer'), ('customer-2', 'peanut butter'), ('customer-2', 'jelly'), ('customer-2', 'eggs'),
        ('customer-3', 'pepper'), ('customer-3', 'salt'), ('customer-3', 'milk'), ('customer-3', 'cookies'),
        ('customer-4', 'peanut butter'), ('customer-4', 'jelly')
        ]

def mapper1(customer, product):
    return customer, product

def reducer1(customer, productsList):
    result = []

    for products_pair in itertools.combinations(productsList, 2):
        result.append((tuple(sorted(products_pair)), 1))

    return result

result_mapred1 = list(simul.map_red(data, mapper1, reducer1))

print("result_mapred1:\n")
for item in result_mapred1:
    print(item)

def mapper2(products_pair, amount):
    return products_pair, amount

def reducer2(products_pair, amountsList):
    return products_pair, sum(amountsList)

result_mapred2 = list(simul.map_red(result_mapred1, mapper2, reducer2))

print("result_mapred2\n")
for item in sorted(result_mapred2, key=lambda item: item[1], reverse=True):
    print(item)
