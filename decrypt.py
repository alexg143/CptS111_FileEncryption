# Alex Glenn
# CptS 111, Fall 2017
# Programming Assignment #7
# Nov. 28, 2017
# Decryption Program - Part D
#
# This program takes a password inputted by the user, an existing ciphered file,
# and creates a clear text file that the user names. This text file is
# deciphered specifically with the password that the user has used.

from cipher import *

def main():
    """ This functions deciphers a ciphered text file using a password inputted by the
    user. It then writes and creates a new clear text file."""
    password = input('Enter password: ')
    cipher_text = input('Enter cipher text file name: ')
    clear_text = input('Enter clear text file name: ')
    amp, first_seed = gen_amp_seed(password) # amplitude and the starting seed are found by inputting user password into gen_amp_seed
    next_seed = [first_seed]                 # a next seed list is started, with the first seed being the first of the list
    infile = open(cipher_text, 'r')          # open the inputted ciphered text file to read
    outfile = open(clear_text, 'w')          # open the file that will be outputted to write
    n = 0                                    # initialize variable n at 0
    for line in infile:                      # loop for each line in clear text
        amp_null, seed_next_line, dline = line2clear(amp, next_seed[n], line.rstrip())
        next_seed.append(seed_next_line)
        # line2clear is used to decipher each line of the text. It also outputs the next
        # seed that will be used to start the next line with, which is appended to the list
        # of seeds.
        n += 1                        # add 1 to n at each loop
        print(dline, file = outfile)  # print to the clear file

main()


