def key_scheduling_algorithm(key):
    # Array "S" is initialized to the identity permutation
    S = list(range(256))
    j = 0

    keylength = len(key)
    if keylength > 256:
        keylength = 256

    for i in range(256):
        j = (j + S[i] + key[i % keylength]) % 256
        # swap values of S[i] and S[j]
        S[i], S[j] = S[j], S[i]

    return S


def pseudo_random_generation_algorithm(S, data, n=0):
    result = [0] * len(data)

    i = 0
    j = 0
    s_length = len(S)
    for iteration in range(len(data) + n):
        # increment i
        i = (i + 1) % s_length

        # looks up the ith element of S, S[i], and adds that to j
        j = (j + S[i]) % s_length

        # exchanges the values of S[i] and S[j]
        S[i], S[j] = S[j], S[i]

        if iteration >= n:
            # use the modular sum S[i] + S[j] as an index to fetch a third element of S
            k = S[(S[i] + S[j]) % s_length]
            # then bitwise exclusive ORed (XORed) with the next byte of the message to produce the next byte of either
            # ciphertext or plaintext.
            result[iteration - n] = ord(data[iteration - n]) ^ k

    return result


def convert_char_to_int(value):
    return [ord(ch) for ch in value]


def encrypt(plaintext, key, n=0):
    key = convert_char_to_int(key)
    if n == 0:
        return pseudo_random_generation_algorithm(key_scheduling_algorithm(key), plaintext, n)
    if n < 256 or n > 3_072:
        raise Exception(f"n={n} must be in range [256,3,072].")
    if n % 256:
        raise Exception(f"n={n} must be a multiple of 256.")


def decrypt(ciphertext, key, n=0):
    return encrypt(ciphertext, key, n)
