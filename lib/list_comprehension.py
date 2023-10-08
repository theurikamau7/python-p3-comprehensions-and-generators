#!/usr/bin/env python3

def return_evens(sequence):
   
    even_numbers = [x for x in sequence if x % 2 == 0]
    return even_numbers


def make_exclamation(string):
   
   make_exclamation = [string + "!" for string in string]
   return make_exclamation