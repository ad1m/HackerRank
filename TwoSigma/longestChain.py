def  longestChain(words):
    words_set = set(words)
    mc = 0
    current = 0 
    wl = [mc]
    for w in words_set:
        if len(w) > mc: 
            pass
        else: 
            continue 
        mc1 = find_chain(w, words_set, current, wl)
        mc = max(mc1, mc)
    return mc

'''
Recursively find max chain
'''
def find_chain(w, words_set, current, mc):
    if w not in words_set: 
        mc = 0
        return mc
    current =  current + 1
    mc[0] = current
    for i in range(len(w)):
        w1 = w[:i] + w[i+1:]
        find_chain(w1, words_set, current, mc)
    mc = mc[0]
    return mc