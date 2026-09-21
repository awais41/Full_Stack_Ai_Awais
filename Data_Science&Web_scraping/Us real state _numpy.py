# RealEstate-USA.csv - numpy practice

import numpy as np
np.set_printoptions(threshold=np.inf, linewidth=np.inf)

price, house_size = np.genfromtxt(
    'RealEstate-USA (1).csv',
    delimiter=',',
    usecols=(2,10),
    unpack=True,
    dtype='f8',
    encoding='utf-8',
    skip_header=1,
    invalid_raise=False
)

print(price)
print(house_size)

# some rows didnt load properly so removing NaN before doing stats
mask = ~np.isnan(price) & ~np.isnan(house_size)

price = price[mask]
house_size = house_size[mask]

print("Total valid rows:", len(price))

# Real Estate Price - statistics operations
print("Real Estate Price mean: ", np.mean(price))
print("Real Estate Price average: ", np.average(price))
print("Real Estate Price std: ", np.std(price))
print("Real Estate Price median: ", np.median(price))
print("Real Estate Price percentile - 25: ", np.percentile(price,25))
print("Real Estate Price percentile - 75: ", np.percentile(price,75))
print("Real Estate Price percentile - 3: ", np.percentile(price,3))
print("Real Estate Price min : ", np.min(price))
print("Real Estate Price max : ", np.max(price))

# Real Estate Price - maths operations
print("Real Estate Price square: ", np.square(price))
print("Real Estate Price sqrt: ", np.sqrt(np.abs(price)))
print("Real Estate Price pow: ", np.power(price,2))
print("Real Estate Price abs: ", np.abs(price))

# Perform basic arithmetic operations
addition = price + house_size
subtraction = price - house_size
multiplication = price * house_size

division = np.divide(
    price,
    house_size,
    out=np.zeros_like(price),
    where=house_size != 0
)

print("Real Estate Price - House Size - Addition:", addition)
print("Real Estate Price - House Size - Subtraction:", subtraction)
print("Real Estate Price - House Size - Multiplication:", multiplication)
print("Real Estate Price - House Size - Division:", division)

# Trigonometric Functions
pricePie = np.log(np.abs(price) + 1)

sine_values = np.sin(pricePie)
cosine_values = np.cos(pricePie)
tangent_values = np.tan(pricePie)

print("Real Estate Price - log - Sine values:", sine_values)
print("Real Estate Price - log - Cosine values:", cosine_values)
print("Real Estate Price - log - Tangent values:", tangent_values)

print("Real Estate Price - log - Exponential values:", np.exp(pricePie))

# natural log and base 10 log
log_array = np.log(np.abs(pricePie))
log10_array = np.log10(np.abs(pricePie))

print("Real Estate Price - log - Natural logarithm values:", log_array)
print("Real Estate Price - log - Base-10 logarithm values:", log10_array)

# Hyperbolic Sine
sinh_values = np.sinh(pricePie)
print("Real Estate Price - log - Hyperbolic Sine values:", sinh_values)

# Hyperbolic Cosine
cosh_values = np.cosh(pricePie)
print("Real Estate Price - log - Hyperbolic Cosine values:", cosh_values)

# Hyperbolic Tangent
tanh_values = np.tanh(pricePie)
print("Real Estate Price - log - Hyperbolic Tangent values:", tanh_values)

# Inverse Hyperbolic Sine
asinh_values = np.arcsinh(pricePie)
print("Real Estate Price - log - Inverse Hyperbolic Sine values:", asinh_values)

# Inverse Hyperbolic Cosine
acosh_values = np.arccosh(np.abs(pricePie)+1)
print("Real Estate Price - log - Inverse Hyperbolic Cosine values:", acosh_values)

# Price House Size - 2 dimensional array
D2PriceHouse = np.array([
    price,
    house_size
])

print("Real Estate Price House Size - 2 dimensional array - ", D2PriceHouse)
print("Real Estate Price House Size - 2 dimensional array - dimension", D2PriceHouse.ndim)
print("Real Estate Price House Size - 2 dimensional array - total number of elements", D2PriceHouse.size)
print("Real Estate Price House Size - 2 dimensional array - gives size of array in each dimension", D2PriceHouse.shape)
print("Real Estate Price House Size - 2 dimensional array - data type", D2PriceHouse.dtype)

# Splicing array
D2PriceHouseSlice = D2PriceHouse[0:1:1 , 1:5:1]
print("Real Estate Price House Size - Splicing array - D2PriceHouse[:1,:5] ", D2PriceHouseSlice)

D2PriceHouseSlice2 = D2PriceHouse[:1,4:15:4]
print("Real Estate Price House Size - Splicing array - D2PriceHouse[:1,4:15:4] ", D2PriceHouseSlice2)

# Indexing array
D2PriceHouseSliceItemOnly = D2PriceHouseSlice[0,1]
print("Real Estate Price House Size - Index array - D2PriceHouseSlice[0,1] ", D2PriceHouseSliceItemOnly)

if D2PriceHouseSlice2.shape[1] > 2:
    D2PriceHouseSlice2ItemOnly = D2PriceHouseSlice2[0,2]
    print("Real Estate Price House Size - Index array - D2PriceHouseSlice2[0,2] ", D2PriceHouseSlice2ItemOnly)

# nditer just gives values, no index
count = 0
for elem in np.nditer(D2PriceHouse):
    print(elem)
    count += 1
    if count > 10:
        break

# ndenumerate gives index as well as value
count = 0
for index, elem in np.ndenumerate(D2PriceHouse):
    print(index, elem)
    count += 1
    if count > 10:
        break

# 2 x N -> 1 x (2*N) - reshape
total = D2PriceHouse.size
D2PriceHouse1TOtotal = np.reshape(D2PriceHouse, (1,total))

print("Real Estate Price House Size - reshape : ", D2PriceHouse1TOtotal)
print("Real Estate Price House Size - reshape : Size ", D2PriceHouse1TOtotal.size)
print("Real Estate Price House Size - reshape : ndim ", D2PriceHouse1TOtotal.ndim)
print("Real Estate Price House Size - reshape : shape ", D2PriceHouse1TOtotal.shape)

print()