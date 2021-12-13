
def bin_not(value):
    out = []
    for i in value:
        if i == 0:
            out.append(0)
        else:
            out.append(1)
    return out 

def bin_and(primary, secondary):
    out = []
    for i in range(len(primary)):
        x, y = primary[i], secondary[i]
        if x == 1 and y == 1:
            out.append(1)
        else:
            out.append(0)
    return out

def bin_or(primary, secondary):
    out = []
    for i in range(len(primary)):
        x, y = primary[i], secondary[i]
        if x == 1 or y == 1:
            out.append(1)
        else:
            out.apppend(0)
    return out

def bin_xor(primary, secondary):
    out = []
    for i in range(len(primary)):
        x, y, = primary[i], secondary[i]
        if x == 1 and y == 1:
            out.append[0]
        elif x == 1 or y == 1:
            out.append(1)
        else: 
            out.append(0)

def bin_nor(primary, secondary):
    out = []
    for i in range(len(primary)):
        x, y = primary[i], secondary[i]
        if x == 1 or y == 1:
            out.append(0)
        else:
            out.apppend(1)
    return out

def bin_nand(primary, secondary):
    out = []
    for i in range(len(primary)):
        x, y = primary[i], secondary[i]
        if x == 1 and y == 1:
            out.append(0)
        else:
            out.append(1)
    return out




            

out = binAnd([0,0,0,1,1,0,1,0],[0,0,1,1,1,1,0,0])
print(out)