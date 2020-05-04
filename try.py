import subprocess

file = input("Insert file path: ")
print("Reading segments from " + file)
result = subprocess.run( ("readelf -S " + file).split(' '), stdout=subprocess.PIPE).stdout.decode('utf-8')

result = result.split('\n')

lines_to_store = ['.text', '.rodata', '.data', '.bss']
offsets = {}

for line in result:
    #print(str(line[line.find(' .') : line.find('\t')].split(' ')))
    tmp = line[line.find(' .') : line.find('\t')].split(' ')
    seg = [l for l in tmp if l != ""]
    if seg != []: 
        if seg[0] in lines_to_store:
            #print(seg[0] + " " + seg[2])
            offsets[seg[0]] = seg[2]

print(offsets)