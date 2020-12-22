# OPTIMAL TECHNIQUE
def check(element, string, j):
    var = None
    for x in range(j, len(string)):
        if element == string[x]:
            var = x
            break
        else:
            pass
    return var


def optimal_c(data, frames):
    string = list(map(int, data.split()))
    len_str = len(string)
    hit = 0
    frame_index = 0
    memory = []

    for i in range(len_str):
        if frame_index < frames:
            if string[i] in memory:
                hit += 1
            else:
                memory.append(string[i])
                frame_index += 1
        else:
            break
    # print(memory)
    val = 0
    index = 0
    for j in range(i, len_str - 1):
        if string[j] in memory:
            hit += 1
        else:
            val = 0
            for frame_index in range(0, len(memory)):
                var = check(memory[frame_index], string, j)
                if var == None:
                    index = frame_index
                    break
                elif val < var:
                    val = var
                    index = frame_index
            memory[index] = string[j]
        # print(memory)

    miss = len(string) - hit
    hit_ratio = hit / len(string)
    return hit, miss, memory, hit_ratio

"""
# DRIVER CODE
string = list(map(int, input("Enter all string val::").split()))
frames = int(input("No. of Frames: "))
memory, hit = optimal(frames, string)

print('\n{:<20}{}{}'.format('Cache Memory',':  ',memory))
print('{:<20}{}{}'.format('Total no. of HITS',':  ', hit))
print('{:<20}{}{}'.format('Total no. of Miss',':  ', len(string) - hit))
print('{:<20}{}{:.2f}'.format('HIT ratio',':  ', hit/len(string)))
"""