def min_subsequences(source, target):
    
    def find_subsequence(src, tgt):
        src_index, tgt_index = 0, 0
        while src_index < len(src) and tgt_index < len(tgt):
            if src[src_index] == tgt[tgt_index]:
                tgt_index += 1
            src_index += 1
        return tgt_index

    count = 0
    current_index = 0
    while current_index < len(target):
        matched = find_subsequence(source, target[current_index:])
        if matched == 0:
            return -1
        current_index += matched
        count += 1

    return count

user_input = input()
source, target = user_input.split()
result = min_subsequences(source, target)
print(result)

