def create_key(candidate):
    upper_cand=candidate.upper()
    char_even= [c for c in upper_cand[::2]]
    char_odd = [c for c in upper_cand[1::2]]
    key={char_even[i]:char_odd[i] for i in range(min(len(char_even),len(char_odd)))}
    key.update({char_odd[i]:char_even[i] for i in range(min(len(char_even),len(char_odd)))})
    return key, len(key)==len(candidate)


    


if __name__=='__main__':
    print(create_key("POLITYKARENU"))

    print(create_key("LOLE"))