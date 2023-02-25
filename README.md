# RC4 Algorithm
<p align="justify">For my python practice I decided to implement a simple stream cipher called RC4 (Rivest Cipher 4) and its variant RC4-drop[n]. While it is simple to use and to implement, multiple vulnerabilities have rendered it insecure.

RC4 is comprised of two phases:
<ol>
    <li> <b>KSA</b> (key-scheduling algorithm) : initializes a permutation in the state vector S.
    </li>
    <li> <b>PRGA</b> (pseudo-random generation algorithm): produces a stream of keys K[0], K[1], ... which is XOR-ed with a given plaintext to obtain a ciphertext.
</ol></p>

<p align="justify">You can find detailed explanation about the algorithm online. Also, here is my favorite quote I read about RC4: "<i>You can fit the code for RC4 onto a cocktail napkin, with plenty of room left over for the cocktail.</i>".</p>

## RC4-drop[n]
<p align="justify">Small modification to the well known RC4 algorithm that skips first n bytes of keystream, where <code>n=0</code> corresponds to regular RC4. The number of skipped bytes should be in range <code>n∈[256,3,072]</code> where <code>n≡0(mod 256)</code>.