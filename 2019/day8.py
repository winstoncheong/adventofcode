

f = open('day8in.txt')
data = f.readline()

layerlen = 25*6 # size of each layer

numlayers = int(len(data)/layerlen)

layers = list()

# read off each layer as a substring of the original data
for i in range(numlayers):
    layers.append(data[i*layerlen: (i+1)*layerlen])

# find the layer with minimum number of zeros

def countchar(string,char):
    i=0
    for ch in string:
        if ch == char:
            i+=1
    return i

zerocount = list(map(lambda v: countchar(v, '0'), layers))

minzero = min(zerocount)

layer_ind = zerocount.index(minzero)

layer = layers[layer_ind]

print("First answer:", countchar(layer,'1') * countchar(layer,'2'))

# Part 2

final_image = ""
for i in range(layerlen): # pixel of the image
    for layer_i in range(len(layers)): 
        if layers[layer_i][i] != '2':
            final_image += layers[layer_i][i] # found a black or white pixel
            break

# final image complete

# 0 = black, 1 = white
# message is more readable if reversed

final_image = final_image.replace('1','*')
final_image = final_image.replace('0',' ')

print('Second answer:')
for i in range(6):
    print(final_image[i*25: (i+1)*25])
    
