import keepa

# establish interface with keepa
mykey = 'fgq27c6s0thoa3jmsvbdr8da6k4uka6q65num7rv5jnpsvcgaqim4ealhj57s1am'
api = keepa.Keepa(mykey)

# product request (single ASIN)
request = '059035342X'
products = api.query(request)
product = products[0]

# Available columns (Data Headers)
print(products[0].keys())

# Full dataset
# print(products[0])
