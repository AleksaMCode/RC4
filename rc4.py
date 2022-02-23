from lib2to3.pytree import convert
from re import L

def key_scheduling_algorithm(key, state_vector_len):

    if state_vector_len > 255:
        state_vector_len = 255

    # Array "S" is initialized to the identity permutation
    S = range(state_vector_len + 1)

    j = 0
    keylength = len(key)

    for i in range (state_vector_len + 1):
        j = (j + S[i] + key[i % keylength]) % state_vector_len
        # swap values of S[i] and S[j]
        S[i], S[j] = S[j], S[i]

    return S

def pseudo_random_generation_algorithm(S, data):
    result = []

    i = 0
    j = 0
    s_length = len(S)
    for iteration in range(len(data)):
        # increment i
        i = (i + 1) % s_length
        
        # looks up the ith element of S, S[i], and adds that to j
        j = (j + S[i]) % s_length
        
        # exchanges the values of S[i] and S[j] then uses the sum S[i] + S[j] (modulo 256) as an index to fetch a third element of S (the keystream value K below)
        S[i], S[j] = S[j], S[i]
        k = S[(S[i] + S[j]) % s_length]
        
        # then bitwise exclusive ORed (XORed) with the next byte of the message to produce the next byte of either ciphertext or plaintext.
        result[i] =  data[i] ^ k

    return result

def convert_char_to_int(value):
    return [ord(ch) for ch in value]

def main():
    key = 'Secret'
    key = convert_char_to_int(key)
    open_text = 'Attack at dawn'
    len = 256
    result = pseudo_random_generation_algorithm(key_scheduling_algorithm(key, len), open_text)

if __name__ == "__main__":
    main()
