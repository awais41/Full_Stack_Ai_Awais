#FastFoodRestaurants.csv - numpy practice
import numpy as np
np.set_printoptions(threshold=np.inf, linewidth=np.inf)

latitude , longitude = np.genfromtxt('FastFoodRestaurants_fixed_v2.csv',
                                       delimiter=',',
                                       usecols=(4,5),
                                       unpack=True,
                                       dtype='f8',
                                       encoding='utf-8',
                                       skip_header=1,
                                       invalid_raise=False)

print(latitude)
print(longitude)

# some rows didnt load properly so removing NaN before doing stats
latitude = latitude[~np.isnan(latitude)]
longitude = longitude[~np.isnan(longitude)]

# Fastfood Latitude - statistics operations
print("Fastfood Latitude mean: ", np.mean(latitude))
print("Fastfood Latitude average: ", np.average(latitude))
print("Fastfood Latitude std: ", np.std(latitude))
print("Fastfood Latitude median: ", np.median(latitude))
print("Fastfood Latitude percentile - 25: ", np.percentile(latitude,25))
print("Fastfood Latitude percentile - 75: ", np.percentile(latitude,75))
print("Fastfood Latitude percentile - 3: ", np.percentile(latitude,3))
print("Fastfood Latitude min : ", np.min(latitude))
print("Fastfood Latitude max : ", np.max(latitude))

# Fastfood Latitude - maths operations
print("Fastfood Latitude square: ", np.square(latitude))
print("Fastfood Latitude sqrt: ", np.sqrt(np.abs(latitude)))  #abs bcz some values negative
print("Fastfood Latitude pow: ", np.power(latitude,2))
print("Fastfood Latitude abs: ", np.abs(latitude))


# Perform basic arithmetic operations
addition = latitude + longitude
subtraction = latitude - longitude
multiplication = latitude * longitude
division = latitude / longitude

print("Fastfood lat - long - Addition:", addition)
print("Fastfood lat - long - Subtraction:", subtraction)
print("Fastfood lat - long - Multiplication:", multiplication)
print("Fastfood lat - long - Division:", division)


#Trigonometric Functions
latPie = (latitude/np.pi) + 1
sine_values = np.sin(latPie)
cosine_values = np.cos(latPie)
tangent_values = np.tan(latPie)

print("Fastfood Latitude - div - pie - Sine values:", sine_values)
print("Fastfood Latitude - div - pie Cosine values:", cosine_values)
print("Fastfood Latitude - div - pie Tangent values:", tangent_values)

print("Fastfood Latitude - div - pie - Exponential values:", np.exp(latPie))

# natural log and base 10 log
log_array = np.log(np.abs(latPie))
log10_array = np.log10(np.abs(latPie))

print("Fastfood Latitude - div - pie - Natural logarithm values:", log_array)
print("Fastfood Latitude - div - pie = Base-10 logarithm values:", log10_array)

#Hyperbolic Sine
sinh_values = np.sinh(latPie)
print("Fastfood Latitude - div - pie - Hyperbolic Sine values:", sinh_values)

#Hyperbolic Cosine
cosh_values = np.cosh(latPie)
print("Fastfood Latitude - div - pie - Hyperbolic Cosine values:", cosh_values)

#Hyperbolic Tangent
tanh_values = np.tanh(latPie)
print("Fastfood Latitude - div - pie - Hyperbolic Tangent values:", tanh_values)

#Inverse Hyperbolic Sine
asinh_values = np.arcsinh(latPie)
print("Fastfood Latitude - div - pie - Inverse Hyperbolic Sine values:", asinh_values)

#Inverse Hyperbolic Cosine - needs values >= 1 so adding abs+1
acosh_values = np.arccosh(np.abs(latPie)+1)
print("Fastfood Latitude - div - pie - Inverse Hyperbolic Cosine values:", acosh_values)


#Lat Long - 2 dimensional array
D2LatLong = np.array([latitude,
                       longitude])

print("Fastfood Lat Long - 2 dimensional array - ", D2LatLong)
print("Fastfood Lat Long - 2 dimensional array - dimension", D2LatLong.ndim)
print("Fastfood Lat Long - 2 dimensional array - total number of elements", D2LatLong.size)
print("Fastfood Lat Long - 2 dimensional array - gives size of array in each dimension", D2LatLong.shape)
print("Fastfood Lat Long - 2 dimensional array - data type", D2LatLong.dtype)

# Splicing array
D2LatLongSlice = D2LatLong[0:1:1 , 1:5:1]
print("Fastfood Lat Long - 2 dimensional array - Splicing array - D2LatLong[:1,:5] ", D2LatLongSlice)
D2LatLongSlice2 = D2LatLong[:1, 4:15:4]
print("Fastfood Lat Long - 2 dimensional array - Splicing array - D2LatLong[:1, 4:15:4] ", D2LatLongSlice2)

# Indexing array
D2LatLongSliceItemOnly = D2LatLongSlice[0,1]
print("Fastfood Lat Long - 2 dimensional array - Index array - D2LatLongSlice[1,5] ", D2LatLongSliceItemOnly)
D2LatLongSlice2ItemOnly = D2LatLongSlice2[0,2]
print("Fastfood Lat Long - 2 dimensional array - index array - D2LatLongSlice2[0,2] ", D2LatLongSlice2ItemOnly)

# nditer just gives values, no index
count = 0
for elem in np.nditer(D2LatLong):
    print(elem)
    count += 1
    if count > 10:   #stopping early otherwise too much output
        break

#ndenumerate gives index as well as value
count = 0
for index, elem in np.ndenumerate(D2LatLong):
    print(index, elem)
    count += 1
    if count > 10:
        break

# 2 x N -> 1 x (2*N) - reshape
total = D2LatLong.size
D2LatLong1TOtotal = np.reshape(D2LatLong, (1, total))
print("Fastfood Lat Long - reshape : ", D2LatLong1TOtotal)
print("Fastfood Lat Long - reshape : Size ", D2LatLong1TOtotal.size)
print("Fastfood Lat Long - reshape : ndim ", D2LatLong1TOtotal.ndim)
print("Fastfood Lat Long - reshape : shape ", D2LatLong1TOtotal.shape)

