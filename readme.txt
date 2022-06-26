How to run for encode: python3 main.py enc ../folder_x/key1.txt ../folder_y/plain_input.txt output_enc.txt

How to run for decode python3 main.py dec ../folder_x/key1.txt ../folder_y/ciphertext.txt output_dec.txt

Encoder and decode using a matrix:

first argument can be either enc or dec and it decides which process is taken.

second argument key1.txt includes a matrix of nxn size. Matrix has to be all integers and its inverse also should be all integers.

third is either a text or a ciphered text.

fourth prints a ciphered text or deciphered text depends on the first argument.

All the cases that causes errors is in Assertions.zip