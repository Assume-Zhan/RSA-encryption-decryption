# Simple RSA encryption and decryption

## Setup time
- Input : n or (p, q)
    - Select n or primes (p, q) to input
    - :warning: n must need demux into 2 primes
    - p and q must be two primes
    - Ex : 
        - If Q given n : input (n, -1, -1)
        - If Q given p, q : input (-1, p, q)
- Input e :
    - Can setup by itself or given
    - Ex : 
        - If Q given e : just input e
        - If Q not given e : input -1

## Public and private key
- Public key : [n, e]
- Private key : [n, d]

## Enc, Dec
- Mode : "enc"
    - Input : original message
    - Output : encrypted message
- Mode : "dec"
    - Input : encrypted message
    - Output : original message
- Instruction :
    - "chmod" : toggle the mode
    - "exit" : exit