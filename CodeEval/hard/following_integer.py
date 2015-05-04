#!/usr/bin/env python

# Challenge description:
# You are writing out a list of numbers.Your list contains all numbers with 
# exactly Di digits in its decimal representation which are equal to i, for each 
# i between 1 and 9, inclusive. You are writing them out in ascending order. For 
# example, you might be writing every number with two '1's and one '5'. Your list 
# would begin 115, 151, 511, 1015, 1051. Given N, the last number you wrote, 
# compute what the next number in the list will be. The number of 1s, 2s, ..., 9s 
# is fixed but the number of 0s is arbitrary.

from fileinput import input

for line in input():
    num = line.strip()
    # Convert num into array of ints.
    digits = [int(i) for i in str(num)]
    ascending = sorted(digits)
    descending = sorted(digits, reverse=True)
    
    # Worst case
    if digits == descending:
        # Then add a 0 in second place.
        result = ascending[:1] + [0] + ascending[1:]
        # Account for case where 0s are in front.
        zeroes = [dig for dig in result if dig == 0]
        if zeroes:
            nonzeroes = [dig for dig in result if dig != 0]
            # Put all 0s in second place.
            result = nonzeroes[:1] + zeroes + nonzeroes[1:]
        # Convert array of digits back into num.
        print(''.join(map(str, result)))
    else:
        pos = len(digits) - 1
        # Array of (val, index) tuples that have been iterated past.
        past = []
        result = digits

        while pos > -1:
            curr = digits[pos]
            if past:
                # If last two values and ascending order, can swap and done.
                if len(past) == 1 and past[0][0] > curr:
                    result[pos], result[pos+1] = result[pos+1], result[pos]
                    break
                else:
                    # The past values that are bigger than curr value.
                    nums_bigger = {val: index for (val, index) in past if val > curr}
                    # If no bigger numbers, can't swap; continue.
                    if not nums_bigger: 
                        past.append((curr, pos))
                        pos -= 1
                        continue
                    else: 
                        # Swap smallest bigger number with curr.
                        smallest_bigger = min(nums_bigger)
                        # Make sure to swap with correct value.
                        small_big_pos = nums_bigger[smallest_bigger]
                        # Swap.
                        result[pos], result[small_big_pos] = smallest_bigger, curr
                        # Sort values past curr pos.
                        result = result[:pos+1] + sorted(result[pos+1:])
                        break
            else:
                past.append((curr,pos))
            pos -= 1
        
        print(''.join(map(str, result)))
