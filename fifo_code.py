# VIRTUAL MEMORY MAPPING

def fifo_c(data, frames):
    string = list(map(int, data.split()))
    len_str = len(string)
    hit = 0
    j = 0
    memory = []

    for i in range(frames):
        memory.append('')

    for i in range(len_str):
        if j >= frames:
            j = 0

        if string[i] in memory:
            hit += 1
        else:
            memory[j] = string[i]
            j += 1
        # print(memory)
    miss = len(string) - hit
    hit_ratio = hit/len(string)
    return hit, miss, memory, hit_ratio


"""
# DRIVER
string = list(map(int, input("Enter all string val::").split()))
frames = int(input("No. of Frames: "))
hit, memory = fifo(string, frames)

print('\n{:<20}{}{}'.format('Cache Memory', ':  ', memory))
print('{:<20}{}{}'.format('Total no. of HITS', ':  ', hit))
print('{:<20}{}{}'.format('Total no. of Miss', ':  ', len(string) - hit))
print('{:<20}{}{:.2f}'.format('HIT ratio', ':  ', hit/len(string)))
"""
