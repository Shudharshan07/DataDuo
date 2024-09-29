def str_to_binary(value):
    val04 = []
    val05 = ''
    for i in range(len(value)):
        val01 = bin(ord(value[i]))
        val02 = val01[2:len(val01)+1] 
        if len(val02) == 7:
            val03 = "0"+val02
            val04.append(val03)
        elif len(val02) == 6:
            val03 ="00" + val02
            val04.append(val03)

    
    for j in range(len(val04)):
        
        val05 = val05 + ' ' + val04[j]
    
    return val05[1:]


def binary_to_str(value_i):
    value = ' '+ value_i + ' '
    val03 = []
    val04 = []
    val05 = [0]
    val06 = []
    for i in range(0,len(value)):
        if value[i] == ' ':
            val04.append(i)

    for j in range(1,len(val04)):
        val01 = str.strip(value[(val04[j-1]):(val04[j])])
        val_pow = len(val01)-1
        for k in range(len(val01)):
            val02 = pow(2,val_pow)* int(val01[k])
            val03.append(val02)
            val_pow-=1
        
    for p in range(len(val04)):
        val04[p] = val04[p] - p
    
    for q in range(1,len(val04)):
        val06.append(sum(val03[(val04[q-1]):(val04[q])]))


    val07 = ''
    for n in val06:
        val07 = val07 + chr(n)

    return val07

