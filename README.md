# RC4 Algorithm
<p align="justify">For my python practise I decided to implement a simple stream cipher called RC4 (Rivest Cipher 4). While it is simple to use and to implement, multiple vulnerabilities have rendered it insecure.

RC4 is comprised of two phases:
<ol>
    <li> <b>KSA</b> (key-scheduling algorithm) : initialize the permutation in the state vector S.
    </li>
    <li> <b>PRGA</b> (pseudo-random generation algorithm): it produces a stream of K[0], K[1], ... which is XOR-ed with the given plaintext to obtain the ciphertext.
</ol></p>

<p align="justify">You can find detailed explanation about the algorithm online. Also, here is my favorite quote I read about RC4: "<i>You can fit the code for RC4 onto a cocktail napkin, with plenty of room left over for the cocktail.</i>".</p>