# Alex Glenn
# CptS 111, Fall 2017
# Programming Assignment #7
# Nov. 28, 2017
# Cipher Program - Part A/B
#
# This program contains six different functions that can be imported into other
# programs: decipher_chr, cipher_chr, log_map, line2cipher, line2clear, and
# gen_amp_seed. The first three functions were created during lab eleven. The
# next two, line2cipher and line2clear, are used to cipher and decipher text
# in a string line. Lastly, gen_amp_seed is used to find an amplitude and seed
# given a password. gen_amp_seed was created by Prof. John B. Schneider.
#_________________________________________________________________________________________________________

def decipher_chr(symbol, offset):
    """ This function takes a cipher and how much it was offset by, and
    then returns the orginal character based on that offset."""
    new_num = (ord(symbol) - 32) - offset # creates new character without offset
    new_num = (new_num % 95) + 32         # ensures it loops within viewable characters
    return chr(new_num)                   # returns the original character
#_________________________________________________________________________________________________________

def cipher_chr(symbol, offset):
    """ This functions takes a character and offsets it by a user inputted
    amoount, this will then return a ciphered character."""
    new_num = (ord(symbol) - 32) + offset # creates new character with offset
    new_num = (new_num % 95) + 32         # ensures it loops within viewable characters
    return chr(new_num)                   # returns a ciphered character
#_________________________________________________________________________________________________________

def log_map(a, x):
    """ This functions takes amplitude (a) between 1-4 and a seed (x). It uses this to create a new seed."""
    return (a * x) * (1 - x)              # returns a new seed using x and a
#_________________________________________________________________________________________________________

def line2cipher(amp, seed, line): # Part A
    """ This function ciphers each character in a line with a new seed. It does
    this by using a for-loop as well as the log_map and cipher_chr functions."""
    cipher_line = ''            # Initializes an empy string accumulator
    seed_list = [seed]          # Initializes a list for seeds with the first seed already in the list
    n = 0                       # Initializes variable n at 0
    for ch in line:             # Loop for each character in string line
        offset = int(seed_list[n] * 96)        # The offset is the seed multiplied by 96, as an integer
        cipher_line += cipher_chr(ch, offset)  # Add each cipher character to string using cipher_chr
        new_seed = log_map(amp, seed_list[n])  # Each new seed is found using log_map
        seed_list.append(new_seed)             # Append new seeds to the seed list
        n += 1                                 # Add 1 to n on each loop
    return amp, seed_list[-1], cipher_line     # Return the amplitude, last seed, and ciphered line
#_________________________________________________________________________________________________________

def line2clear(amp, seed, line): # Part B
    """ This function deciphers each character in a line with a new seed. It does
    this by using a for-loop as well as the log_map and decipher_chr functions."""
    decipher_line = ''          # Initializes an empy string accumulator
    seed_list = [seed]          # Initializes a list for seeds with the first seed already in the list
    n = 0                       # Initializes variable n at 0
    for ch in line:             # Loop for each character in string line
        offset = int(seed_list[n] * 96)           # The offset is the seed multiplied by 96, as an integer
        decipher_line += decipher_chr(ch, offset) # Add each deciphered character to string using decipher_chr
        new_seed = log_map(amp, seed_list[n])     # Each new seed is found using log_map
        seed_list.append(new_seed)                # Append new seeds to the seed list
        n += 1                                    # Add 1 to n on each loop
    return amp, seed_list[-1], decipher_line      # Return the amplitude, last seed, and deciphered line
#_________________________________________________________________________________________________________

# John B. Schneider
# gen_amp_seed() function
#######################################################################
# Function to calculate an "amplitude" and a "seed" appropriate for
# starting the encryption/decryption process.  These values are based
# on the password given as the argument (which is assumed to be a
# string).  This function uses the SHA1 hash function from the hashlib
# module.  See http://en.wikipedia.org/wiki/SHA-1 for details
# concerning this function.  The hash function creates a unique
# 160-bit 'digest' for a given string.  This digest is split into two
# parts.  One part is used to set the amplitude and the other is used
# to set the seed value.
import hashlib

def gen_amp_seed(password):
    h = hashlib.sha1()          # Create a SHA1 hash object.
    h.update(password.encode()) # Update object with password.
    # Create a 160-bit hexadecimal digest which is returned as a
    # 40-character string.
    d = h.hexdigest()
    # Split the digest into two parts, each of 20 hexadecimal
    # characters/digits.
    d1 = d[ : 20]     
    d2 = d[20 : ]
    # max_possible is the maximum possible value that 20 hexadecimal
    # digits can have.
    max_possible = 0xFFFFFFFFFFFFFFFFFFFF
    # Set the amp and seed values.  amp is 3.99 plus a number that is
    # between 0.0 and 0.01 while seed is between 0.0 and 1.0.  In the
    # unlikely event that d2 equals max_possible, then seed will be
    # 1.0 which will cause the log_map() function to return zero.
    # Although simple to account for this, we will not do so here.
    amp = 3.99 + eval('0x' + d1) / max_possible / 100
    seed = eval('0x' + d2) / max_possible
    return amp, seed
