# find max count of similar one by one elements

def get_idx_next_notsimilar(input_str, cur_idx):
    # find index of next not similar symbol
    next_idx = cur_idx
    while next_idx < len(input_str) and input_str[next_idx] == input_str[cur_idx]:
        next_idx+=1
    return(next_idx)

def get_max(input_str):
    cur_idx, result = 0, 0 
    while cur_idx < len(input_str):
        next_idx = get_idx_next_notsimilar(input_str, cur_idx)
        # save to result if similar symbols count > previous result 
        result = max(result, next_idx)
        cur_idx = next_idx
    return(result)
