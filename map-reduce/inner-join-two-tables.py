from mredu import simul

USERS = 'users'
ORDERS = 'orders'

# user_id, name
table_users = [
            (1, 'jose'),
            (2, 'isabel'),
            (3, 'jorge'),
        ]

# order_id, user_id, product_name
table_orders = [
           (1, 1, 'cafe'),
           (1, 1, 'leche'), 
           (1, 1, 'pan'), 
           (1, 1, 'galletas'),
           (2, 1, 'huevos'),
           (2, 1, 'sal'),
           (2, 1, 'pimienta'),
           (2, 1, 'filete de pollo'),
           (3, 2, 'galletas'),
           (3, 2, 'sal'),
           (3, 2, 'mantequilla'), 
        ]

data = [(USERS, record) for record in table_users] + [(ORDERS, record) for record in table_orders]

print('data')
for item in data:
    print("\t", item)

def mapper(table_name, record):
    if table_name == USERS:
        user_id = record[0]
        return (user_id, (table_name, record))
    # else it has to be orders
    user_id = record[1]
    return (user_id, (table_name, record))


def reducer(user_id, table_records):
    table_users_records   = []
    table_orders_records = []
    for table_name, records in table_records:
        if table_name == ORDERS:
            table_orders_records.append(records)
            continue 
        # else it has to be from the users table
        table_users_records.append(records)
    result = []
    for record in table_users_records:
        user_id, user_name = record
        order_id = None
        orders_hash = {}
        for record in table_orders_records:
            order_id, _, product_name = record
            if order_id not in orders_hash:
                orders_hash[order_id] = []
            orders_hash[order_id].append(product_name)
        for order_id, products_list in orders_hash.items():
            key = (user_id, order_id)
            result.append((key, products_list))
    return result

result_mapred = simul.map_red(data, mapper, reducer)

print('result_mapred')

for item in result_mapred:
    print("\t", item)
