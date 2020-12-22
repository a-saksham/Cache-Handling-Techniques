def lru_c(data, frames):
    string = list(map(int, data.split()))

    len_str = len(string)
    hit = 0
    j = 0

    count = [0]*frames
    memory = [None]*frames

    for i in range(len_str):

        if string[i] in memory:
            hit += 1

            for v in range(frames):
                if memory[v] == string[i]:
                    count[v] = 0

            for w in range(frames):
                count[w] += 1
            # print(memory)

        elif j < frames:
            memory[j] = string[i]
            j += 1
            for x in range(j):
                count[x] = count[x]+1
            # print(memory)

        else:

            for y in range(frames):
                if count[y] == max(count):
                    memory[y] = string[i]
                    count[y] = 0
                    # print(memory)
                    break

            for z in range(frames):
                count[z] += 1

    new_mem = []
    for i in memory:
        if i == None:
            pass
        else:
            new_mem.append(i)

    miss = len(string) - hit
    hit_ratio = hit / len(string)

    return hit, miss, new_mem, hit_ratio


"""
# string = [1,2,3,4,2,1,5,6,2,1,2,3,7,6,3,2,1,2,3,6]
# string = [0,255,1,4,3,8,133,159,216,129,63,8,48,32,73,92,155]
# string = [4,3,25,8,19,6,25,8,16,35,45,22,8,3,16,25,7]

print('\n{:<20}{}{}'.format('Cache Memory',':  ',memory))
print('{:<20}{}{}'.format('Total no. of HITS',':  ', hit))
print('{:<20}{}{}'.format('Total no. of Miss',':  ', len(string) - hit))
print('{:<20}{}{:.2f}'.format('HIT ratio',':  ', hit/len(string)))
"""