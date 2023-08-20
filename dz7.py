from random import choice,randint

VOWELS = 'eyuioa'
CONSONANTS = 'qwrtpsdfghjklzxcvbnm'



def psevdoname_gen(min_len_name = 6, max_len_name = 30, min_bit = 256, max_bit = 4096, numb_files = 42):

    for _ in range(numb_files):
        name = ''
        for _ in range(randint(min_len_name,max_len_name)):
            name += choice(VOWELS + CONSONANTS)       
        for _ in range(randint(min_bit, max_bit)):
            byt = bytes(randint(0,100))
        with open(f' {name} .txt', 'wb') as f:
            f.write(byt)


if __name__ == '__main__':
    psevdoname_gen()





