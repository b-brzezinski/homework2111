KEYS=['GADERYPOLUKI','POLITYKARENU'] #default options for keys
def create_key(candidate):
    upper_cand=candidate.upper() #changes text into uppercase for consistency
    char_even= [c for c in upper_cand[::2]]
    char_odd = [c for c in upper_cand[1::2]]
    key={char_even[i]:char_odd[i] for i in range(min(len(char_even),len(char_odd)))} #creates first half of the key
    key.update({char_odd[i]:char_even[i] for i in range(min(len(char_even),len(char_odd)))}) #adds the second half of the key
    return key, len(key)==len(candidate) #function returns the key and the test for validity for the key

def cipher(text, key):
    text_upper=text.upper()
    ciphered_text=''
    for c in text_upper:
        if c in key.keys(): #ciphers the character if it's in the dictionary
            ciphered_text+=key[c]
        else:
            ciphered_text+=c
    return ciphered_text #return the ciphered text

def cipher_file(input_file,output_file, key):
    with open(input_file,'r') as fin:
        with open(output_file,'w') as fout:
            fout.write(cipher(fin.read(),key))
def main():
    answr=input('Do you want to use (1)GADERYPOLUKI, (2)POLITYKARENU or maybe your own key(3)?')
    while int(answr) not in [1,2,3]:
        answr = input('please input a valid answer (1,2 or 3)')
    if answr == '3':
        while True:
            cand = input('please entere a candidate for key:')
            key_cand = create_key(cand)
            if key_cand[1]:
                key=key_cand[0]
                break
            else:
                print('Your candidate was invalid!')
    else:
        key=create_key(KEYS[int(answr)-1])[0]
    while True:
        answr=input('Do you want to cipher text file or text from terminal [f,t]')
        if answr == 'f' or answr == 't':
            break
    if answr == 'f':
        input_file=input('please enter name of the input file:')
        output_file=input('please enter name of the output file:')
        cipher_file(input_file,output_file,key)
    elif answr == 't':
        text = input('Please enter text to cypher:')
        print(cipher(text, key))

if __name__=='__main__':
    main()