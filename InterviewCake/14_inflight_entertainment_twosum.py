#!/usr/bin/env python

def is_two_sum_movies(movie_lengths, flight_length):
    if len(movie_lengths) < 2 or not flight_length: return False
    comps = set()
    for ml in movie_lengths:
        if ml in comps: return True
        comps.add(flight_length - ml)
        
    return False

arr = [5, 3, 8, 12]
target = 13
    
print is_two_sum_movies(arr, target)
