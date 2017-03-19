==> 01_stock_prices.py <==
#!/usr/bin/env python

def get_max_profit(prices):
    if len(prices) < 2:
        raise IndexError('Getting a profit requires at least 2 prices')
    
    max_profit = prices[1] - prices[0]
    min_price = prices[0]
    
    # At i=0, would buy and sell at the same time.
    for price in prices[1:]:
        curr_profit = price - min_price
        max_profit = max(max_profit, curr_profit)
        min_price = min(min_price, price)
        
    return max_profit

stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
print get_max_profit(stock_prices_yesterday)
neg_prices = [5, 4, 3]
print get_max_profit(neg_prices)

==> 02_prods_of_all_except_i.py <==
#!/usr/bin/env python

def get_products_of_all_except_at(list_ints):
    """
    Naive solution is to, for each number, iterate through the rest of the 
    list and multiply. O(N^2)
    If allowed division, could get product of all ints then just divide by each num.
    Intuition: the product at index i is just the product of the nums before it 
    times the product of the nums after it.
    """
    if len(list_ints) < 2: 
        raise Exception('list_ints needs at least 2 elements')
    
    prev_prod = 1
    prods_before = []
    for num in list_ints:
        prods_before.append(prev_prod)
        prev_prod *= num
        
    prod_after = 1
    i = len(prods_before) - 1    
    while i >= 0:
        prods_before[i] = prods_before[i] * prod_after
        prod_after *= list_ints[i]
        i -= 1
        
    return prods_before

print get_products_of_all_except_at([1, 7, 3, 4])
print get_products_of_all_except_at([1, 2, 6, 5, 9])
print get_products_of_all_except_at([2])


==> 03_highest_prod_3.py <==
#!/usr/bin/env python

def highest_product_three(lst_ints):
    # Naive is sort but doesn't handle negatives well and is at least O(N log N).
    # We have a O(N) greedy solution. Just need to store some state.
    highest_prod_3 = highest_prod_2 = lowest_prod_2 = 1
    highest = lowest = lst_ints[0]
    
    for i, num in enumerate(lst_ints[1:]):
        # Need 3 nums.
        # lowest_prod_2 in the case of negatives.
        if i > 0:
            highest_prod_3 = max(highest_prod_3, num * highest_prod_2, num * lowest_prod_2)
        # Update the prod_2's.
        highest_prod_2 = max(highest_prod_2, num * highest, num * lowest)
        lowest_prod_2 = min(lowest_prod_2, num * lowest, num * highest)
        # Then highest/lowest.
        highest = max(highest, num)
        lowest = min(lowest, num)

    return highest_prod_3

print highest_product_three([2, 3, 6, 5])
print highest_product_three([-10, -10, 1, 3, 2])
print highest_product_three([1, 10, -5, 1, -100])

==> 04_merge_ranges.py <==
#!/usr/bin/env python

def merge_ranges(list_ranges):
    if not list_ranges: raise Exception("Need to provide a non-empty list.")
    if any(x < 0 or y < 0 for (x, y) in list_ranges):
        raise Exception("Negative start/end times don't make sense.")
    if any(y < x for (x, y) in list_ranges):
        raise Exception("End times have to be greater than start times.")
    
    list_ranges.sort(key=lambda x: x[0])
    
    copy_ranges = list_ranges
    prev = list_ranges[0]
    
    # Another method of doing this would be to build up the copy element by element.
    # So could just modify the last element of the merged list.
    for i, (start, end) in enumerate(list_ranges[1:]):
        if start <= prev[1]:
            new_meet = (prev[0], max(prev[1], end))
            copy_ranges[i+1] = new_meet
            copy_ranges[i] = ('del', 'del')
            prev = new_meet
        else:
            prev = (start, end)
        
    return [(x, y) for (x, y) in copy_ranges if x != 'del']
        
          
print merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
print merge_ranges([(1, 10), (2, 6), (3, 5), (7, 9), (20, 23)])
print merge_ranges([(1,5), (2,3)])

==> 05_coin_change.py <==
#!/usr/bin/env python

"""Top-down takes additional O(m) space."""

def change_possibilities_bottom_up(amount, denominations):
    ways_of_doing_n_cents = [0] * (amount + 1)
    ways_of_doing_n_cents[0] = 1

    for coin in denominations:
        for higher_amount in xrange(coin, amount + 1):
            higher_amount_remainder = higher_amount - coin
            ways_of_doing_n_cents[higher_amount] += ways_of_doing_n_cents[higher_amount_remainder]

    return ways_of_doing_n_cents[amount]

print change_possibilities_bottom_up(4, [1, 2, 3])


==> 06_rect_love.py <==
#!/usr/bin/env python

def rect_intersect(r1, r2):
    lx_1, by_1, w_1, h_1 = r1['left_x'], r1['bottom_y'], r1['width'], r1['height']
    lx_2, by_2, w_2, h_2 = r2['left_x'], r2['bottom_y'], r2['width'], r2['height']
    
    # No possible intersection.
    if lx_1 > lx_2 + w_2 or lx_2 > lx_1 + w_1 or by_1 > by_2 + h_2 or by_2 > by_1 + h_1:
        return None
    
    r3 = {}
    
    r3['left_x'], r3['bottom_y']  = max(lx_1, lx_2), max(by_1, by_2)
    
    rx_1, rx_2 = lx_1 + w_1, lx_2 + w_2
    ty_1, ty_2 = by_1 + h_1, by_2 + h_2
    
    # Just "touching" counts as an (0 width/height) intersection.
    rx_3, ty_3 = min(rx_1, rx_2), min(ty_1, ty_2)
    
    r3['width']  = rx_3 - r3['left_x']
    r3['height'] = ty_3 - r3['bottom_y']
    
    return r3
    
r1 = { 
    'left_x'  : 1, 'bottom_y' : 2,
    'width': 5, 'height': 5
}

r2 = {
    'left_x'  : 6, 'bottom_y'  : 3,
    'width': 1, 'height': 2
}

print rect_intersect(r1, r2)

==> 07_temp_tracker.py <==
#!/usr/bin/env python

class TempTracker:
    """Optimize for time and space complexity by precomputing variance values.
    
    All methods are O(1) running time and O(1) space (assuming realistically bounded input).
    """
    
    def __init__(self, list_temps=None):
        """Can't use an optional mutable argument because would share state."""
        # Don't actually need to store an instance list of temps.
        list_t = list_temps if list_temps else []
        
        if list_t: self.max_temp, self.min_temp = max(list_t), min(list_t)
        else: self.max_temp, self.min_temp = None, None
            
        self.num_temps = len(list_t)
        if not list_t: self.avg_temp = None
        else: self.avg_temp = float(sum(list_t)) / self.num_temps
        
        # Technically, since our input list is bounded to temps[0-110] we could 
        # just use an array. But this is more universal.
        self.freqs_t = {}
        self.mode = self.max_freq = 0
        for k in list_t:
            val = self.freqs_t.get(k, 0) + 1
            # Update mode.
            if val > self.max_freq:
                # Don't need to update mode if same one.
                if k != self.mode: self.mode = k
                self.max_freq = val
            self.freqs_t[k] = val
            
    def insert(self, temp):
        self.num_temps += 1
        
        if not self.num_temps:
            self.max_temp = temp
            self.min_temp = temp
        else:
            self.max_temp = max(temp, self.max_temp)
            self.min_temp = min(temp, self.min_temp)
        
        # New mean is the old mean plus the (difference between the new value 
        # and the previous mean) divided by the (new number of values). 
        # Have to "spread out" the new value's contribution.
        if not self.avg_temp: self.avg_temp = float(temp)
        else: self.avg_temp += (temp - self.avg_temp) / self.num_temps
        
        # Update mode if new frequency of temp is greater.
        curr_freq = self.freqs_t.get(temp, 0) + 1
        if curr_freq > self.max_freq:
            if temp != self.mode: self.mode = temp
            self.max_freq = curr_freq
        self.freqs_t[temp] = curr_freq
        
    def get_max(self):
        return self.max_temp
    
    def get_min(self):
        return self.min_temp
    
    def get_mean(self):
        """Mean is iteratively updated on each insert."""
        return round(self.avg_temp, 1) if self.avg_temp else self.avg_temp
        
    def get_mode(self):
        return self.mode if self.num_temps else None
        

test1 = TempTracker()
test1.insert(1)
test1.insert(6)
test1.insert(1)
print test1.get_max(), test1.get_min(), test1.get_mean(), test1.get_mode()

test2 = TempTracker()
print test2.get_max(), test2.get_min(), test2.get_mean(), test2.get_mode()

test3 = TempTracker(list_temps=[1, 1, 6])
print test3.get_max(), test3.get_min(), test3.get_mean(), test3.get_mode()
test3.insert(21)
test3.insert(6)
test3.insert(6)
print test3.get_max(), test3.get_min(), test3.get_mean(), test3.get_mode()

==> 08_superbalanced_tree.py <==
#!/usr/bin/env python

def is_balanced(root):
    if not root: return True

    # Short-circuit as soon as we find >2.
    depths = []

    # Stack that will hold tuples of (node, depth).
    nodes = []
    nodes.append((tree_root, 0))

    while len(nodes):
        node, depth = nodes.pop()

        # Case: we found a leaf.
        if (not node.left) and (not node.right):
            if depth not in depths:
                depths.append(depth)

                # Two ways we might now have an unbalanced tree:
                #   1) more than 2 different leaf depths
                #   2) 2 leaf depths that are more than 1 apart.
                if ((len(depths) > 2) or
                        (len(depths) == 2 and abs(depths[0] - depths[1]) > 1)):
                    return False

        # Case: not a leaf, keep going.
        else:
            if node.left:
                nodes.append((node.left, depth + 1))
            if node.right:
                nodes.append((node.right, depth + 1))

    return True

==> 09_is_bst.py <==
#!/usr/bin/env python

def is_bst(root, high=float('inf'), low=float('-inf')):
    if not root: return True
    if value > high or value < low: return False
    return (is_bst(node.left, high=root.value, low=low) 
            and is_bst(node.right, high=high, low=root.value))

==> 10_second_largest_bst.py <==
#!/usr/bin/env python

def get_largest_bst(root):
    if not root: return None
    
    curr = root
    while curr:
        if not curr.right: return curr.value
        else: curr = curr.right

def get_second_largest_bst(root):
    if not root or not curr.left and not curr.right: return None
    
    curr = root
    while curr:
        if curr.left and not curr.right:
            return get_largest_bst(curr.left)
           elif curr.right and not curr.right.left and not curr.right.right:
            return curr.value
        curr = curr.right
    return None

==> 11_web_crawler_trie.py <==
#!/usr/bin/env python

class Trie:

    def __init__(self):
        self.root_node = {}

    def check_present_and_add(self, word):

        current_node = self.root_node
        is_new_word = False

        # Work downwards through the trie, adding nodes
        # as needed, and keeping track of whether we add
        # any nodes.
        for char in word:
            if char not in current_node:
                is_new_word = True
                current_node[char] = {}
            current_node = current_node[char]

        # Explicitly mark the end of a word.
        # Otherwise, we might say a word is
        # present if it is a prefix of a different,
        # longer word that was added earlier.
        if "End Of Word" not in current_node:
            is_new_word = True
            current_node["End Of Word"] = {}

        return is_new_word

==> 12_item_in_list_binary_search.py <==
#!/usr/bin/env python

def is_in_list(arr, num):
    if arr[0] > num or num > arr[-1]: return False
    low, high = 0, len(arr) - 1
    while low < high:
        mid = low + ((high - low) / 2)
        if num == arr[mid]: return True
        elif num > arr[mid]: low = mid + 1
        elif num < arr[mid]: high = mid
    
    return False

==> 13_find_rotation_point.py <==
#!/usr/bin/env python

def find_rotation_pt(arr):
    if not arr: return None
    low, high = 0, len(arr) - 1
    # Check if fully sorted / not rotated.
    if arr[low] <= arr[high]: return 0
    
    while low < high:
        mid = low + (high - low) / 2
        if arr[low] <= arr[mid]: low = mid + 1
        else: high = mid
    
    return low
        
words = [
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'asymptote', # <-- rotates here!
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'othellolagkage',
]

nums = [4, 5, 6, 7, 8, 1, 2, 3]
nums2 = [1, 2, 3, 4, 5, 6, 7, 8]
assert find_rotation_pt(words) == 4
assert find_rotation_pt(nums) == 5
assert find_rotation_pt(nums2) == 0
print "Tests pass!"


==> 14_inflight_entertainment_twosum.py <==
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

==> 15_nth_fibonacci.py <==
#!/usr/bin/env python

def fib_rec(n, memo=None):
    if not memo: memo = [0, 1]
    # fib number already cached
    if n < len(memo): return memo[n]
    else:
        f = fib_rec(n-2, memo) + fib_rec(n-1, memo)
        memo.append(f)
        return f

def fib(n):
    if n in [0, 1]: return n
    prevprev, prev = 0, 1
    for i in xrange(n-1):
        f = prevprev + prev
        prevprev, prev = prev, f
    return f

print fib(8), fib_rec(8)
print fib(1), fib_rec(1)

==> 16_cake_thief_knapsack.py <==
#!/usr/bin/env python

def max_duffel_bag_value(cake_tuples, cap):
    max_value_at = [0] * cap + 1

    for c in xrange(cap + 1):
        for cake_weight, cake_value in cake_tuples:
            # Return infinity if cake exists with 0 weight and positive value.
            if not cake_weight and cake_value: return float('inf')
            curr_max = max_value_at[c]
            if cake_weight == c:
                max_value_at[c] = max(curr_max, cake_value)
            elif cake_weight < c:
                cand_max = cake_value + max_value_at[c - cake_weight]
                max_value_at[c] = max(curr_max, cand_max) 

    return max_value_at[cap]

==> 19_queue_w_stacks.py <==
#!/usr/bin/env python

class QueueTwoStacks:

    def __init__(self):
        self.in_stack  = []
        self.out_stack = []

    def enqueue(self, item):
        self.in_stack.append(item)

    def dequeue(self):
        if len(self.out_stack) == 0:
            # Move items from in_stack to out_stack, reversing order
            while len(self.in_stack) > 0:
                newest_in_stack_item = self.in_stack.pop()
                self.out_stack.append(newest_in_stack_item)
            # If out_stack is still empty, raise an error
            if len(self.out_stack) == 0:
                raise IndexError("Can't dequeue from empty queue!")
        return self.out_stack.pop()

==> 20_stack_max.py <==
#!/usr/bin/env python

class Stack:

    # initialize an empty list
    def __init__(self):
        self.items = []

    # push a new item to the last index
    # at each position in the stack, keep track of the max element
    # from there down
    def push(self, item):
        if not self.items: tup = (item, item)
        else: tup = (item, max(item, self.items[-1][1]))
        self.items.append(tup)

    # remove the last item
    def pop(self):
        # if the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items: return None
        return self.items.pop()

    # see what the last item is
    def peek(self):
        if not self.items: return None
        return self.items[-1]
    
    # max of the whole stack equals the max of the top element
    def get_max(self):
        if not self.items: return None
        return self.items[-1][1]
    

s = Stack()
s.push(3)
s.push(5)
print s.get_max()
s.push(4)
print s.get_max()
s.push(11)
s.push(2)
print s.get_max()
s.pop()
s.pop()
print s.get_max()

==> 21_unique_int_dupes.py <==
#!/usr/bin/env python

def get_uniq(arr):
    return reduce(lambda x, y: x ^ y, arr, 0)

==> 22_delete_node.py <==
#!/usr/bin/env python

class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next  = None

def delete_node(node):
    if not node: return None
    if not node.next: raise Exception("Can't delete the last node.")
    node.value = node.next.value
    node.next = node.next.next
    return node

==> 23_cycle_in_ll.py <==
#!/usr/bin/env python

class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next  = None
        
def is_cycle(root):
    if not root.next: return True
    c1, c2 = root, root.next
    while c2 and c2.next:
        if c1 == c2: return True
        c1, c2 = c1.next, c2.next.next
    return False


==> 24_reverse_ll.py <==
#!/usr/bin/env python

class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next  = None
 
def reverse_ll(head):
    curr, prev = head, None
    while curr:
        curr.next, prev, curr = prev, curr,  curr.next
    return prev

a = LinkedListNode(1)
b = LinkedListNode(2)
c = LinkedListNode(3)

a.next = b
b.next = c

r = reverse_ll(a)
assert r.value == 3
assert r.next.value == 2
assert r.next.next.value == 1
assert not r.next.next.next

# Edge cases: empty linked list and single node linked list.
assert not reverse_ll(None)
assert reverse_ll(LinkedListNode(5)).value == 5
print 'Tests passed!'

==> 25_kth_to_last_node.py <==
#!/usr/bin/env python

class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next  = None

def kth_to_last_node(k, head):
    prev, curr = head, head
      # Move curr k-1 nodes ahead of head/prev.
    for _ in xrange(k - 1):
        if not curr.next: raise Exception("List is too short to get the kth to last node.")
        curr = curr.next
    # Not `while curr` since then would go one node too far.
    while curr.next:
        prev, curr = prev.next, curr.next
    return prev
        
a = LinkedListNode("Angel Food")
b = LinkedListNode("Bundt")
c = LinkedListNode("Cheese")
d = LinkedListNode("Devil's Food")
e = LinkedListNode("Eccles")

a.next = b
b.next = c
c.next = d
d.next = e

assert kth_to_last_node(3, a).value == 'Cheese'
print 'Test passed!'

==> 26_reverse_chars_inplace.py <==
#!/usr/bin/env python

def reverse_str(s):
    # Convert to list since Python strings are immutable.
    lst_s = list(s)
    l, r = 0, len(lst_s) - 1
    while l < r:
        lst_s[l], lst_s[r] = lst_s[r], lst_s[l]
        l, r = l + 1, r - 1
    return ''.join(lst_s)

assert reverse_str('reversed') == 'desrever'
print 'Test passed!'

==> 27_reverse_words_inplace.py <==
#!/usr/bin/env python

import string

def reverse_chars(s_lst, l, r):
    while l < r:
        s_lst[l], s_lst[r] = s_lst[r], s_lst[l]
        l, r = l + 1, r - 1
    return s_lst

def reverse_words(sentence):
    sentence = list(sentence)
    space = set(string.whitespace)
    # Reverse all chars.
    reverse_chars(sentence, 0, len(sentence) - 1)
    l = 0
    # (Re-)reverse chars in words.
    # Go one further to ensure we reverse the last word too.
    for i in xrange(len(sentence) + 1):
        if i == len(sentence) or sentence[i] in space:
            reverse_chars(sentence, l, i - 1)
            l = i + 1
    return ''.join(sentence)
        
assert reverse_words('Jack climbed the beanstalk') == 'beanstalk the climbed Jack'
print 'Test passed!'

==> 28_get_matching_paren.py <==
#!/usr/bin/env python

def get_matching_paren(s, pos):
    # Proxy stack variable.
    num_l = 0
    for i, ch in enumerate(s):
        # Can skip ahead past the position of the left paren I'm given.
        if i <= pos: continue
        if ch == '(': 
            num_l += 1
        elif ch == ')':
            if not num_l: return i
            else: num_l -= 1
    return None

s = ("Sometimes (when I nest them (my parentheticals) too much "
     + "(like this (and this))) they get confusing.")
assert s[10] == '(' and s[28] == '('
assert get_matching_paren(s, 10) == 79
assert get_matching_paren(s, 28) == 46
assert s[79] == ')' and s[46] == ')'
assert not get_matching_paren('( just 1 lonely paren', 0)
print 'Tests passed!'

==> 29_bracket_validator.py <==
#!/usr/bin/env python

def is_valid_brackets(s):
    mp = {')': '(', '}': '{', ']': '['}
    # Separate vals set for O(1) membership checking.
    vals = set(mp.values())
    stk = []
    
    for ch in s:
        if ch in vals:
            stk.append(ch)
        elif ch in mp:
            # Don't pop unless we know it's a match.
            if not stk or stk[-1] != mp[ch]: return False
            stk.pop()
    
    return not stk

assert is_valid_brackets('{[]()}')
assert not is_valid_brackets('{[(])}')
assert not is_valid_brackets('{[}')
print 'Tests passed!'

==> 30_permutation_palindrome.py <==
#!/usr/bin/env python

def is_permutation_palindrome(s):
    if len(s) < 2: return True
    odds = set()
    for ch in s:
        if ch in odds: odds.remove(ch)
        else: odds.add(ch)
    # For a permutation to be a palindrome, can only have 0-1 chars
    # with an odd frequency.
    return len(odds) < 2
            
s1, s2, s3, s4, s5 = 'civic', 'ivicc', 'civil', 'livci', 'aaa'
assert is_permutation_palindrome(s1)
assert is_permutation_palindrome(s2)
assert not is_permutation_palindrome(s3)
assert not is_permutation_palindrome(s4)
assert is_permutation_palindrome(s5)
print 'Tests passed!'

==> 31_recursive_str_permutations.py <==
#!/usr/bin/env python

def gen_permutes(s):
    if len(s) < 2: return set([s])
    new_perms = gen_permutes(s[1:])
    perms = set()
    for p in new_perms:
        # Add the first character at each position in the permutation.
        for i in xrange(len(p) + 1):
            new_p = p[:i] + s[0] + p[i:]
            perms.add(new_p)
    return perms
                         
def gen_permutes2(s, st, end):
    if st == end: return set([s])
    perms, s = set(), list(s)
    for i in xrange(st, end + 1):
        s[st], s[i] = s[i], s[st]
        perms.update(gen_permutes2(''.join(s), st + 1, end))
        # Backtrack.
        s[i], s[st] = s[st], s[i]
    return perms


if __name__ == '__main__':
    from timeit import timeit

    def wrapper(func, *args, **kwargs):
        def wrapped():
            return func(*args, **kwargs)
        return wrapped

    s = 'aabfcd'
    wrapped = wrapper(gen_permutes, s)
    wrapped2 = wrapper(gen_permutes2, s, 0, 5)

    g1 = round(timeit(wrapped, number=10000), 3)
    print 'gen_permutes of {} took {} seconds to get:'.format(s, str(g1))
    print gen_permutes('aabcd')

    print
    g2 = round(timeit(wrapped2, number=10000) * 1000, 3)
    print 'gen_permutes2 of {} took {} seconds to get:'.format(s, str(g1))
    print gen_permutes2('aabcd', 0, 4)



==> 32_top_scores_counting_sort.py <==
#!/usr/bin/env python

import itertools

def sort_scores(scores, max_score):
    # Use counting sort to get O(n) time at the expense of O(n) space.
    arr = [0] * (max_score + 1)
    for sc in scores:
        arr[sc] += 1
    # Need to handle multiple players with the same score.
    srted = [[i] * n for i, n in enumerate(arr) if n]
    # Flatten.
    return list(itertools.chain(*srted))

unsorted_scores = [37, 89, 91, 41, 65, 91, 53]
MAX_SCORE = 100
assert sort_scores(unsorted_scores, MAX_SCORE) == [37, 41, 53, 65, 89, 91, 91]
print 'Test passed!'

==> 33_which_num_to_n_is_dupe.py <==
#!/usr/bin/env python

def get_dupe_num_to_n(nums, n):
    # Use sum of nums to n formula to get O(1) space.
    return sum(nums) - n * (n + 1) / 2
    
assert get_dupe_num_to_n([1, 2, 3, 3, 4, 5], 5) == 3
print 'Test passed!'

==> 34_word_cloud.py <==
#!/usr/bin/env python

import string

def build_word_cloud_dict(s, freqs=None):
    # Lowercase and remove extraneous whitespace and punctuation.
    if not freqs: freqs = {}
    for w in s.split():
        if w in string.whitespace: continue
        # Remove punctuation from ends of word.
        w = ''.join(c for i, c in enumerate(w.lower()) 
                    if 0 < i < len(w) - 1 or c not in string.punctuation)
        freqs[w] = freqs.get(w, 0) + 1
    return freqs
           
s1 = 'After making a real gung-ho effort to beat the eggs, Dana read the next step: '
s2 = 'Add milk and eggs, then add flour and sugar.'
d1 = build_word_cloud_dict(s1)
d2 = build_word_cloud_dict(s2, d1)
print d2

s3 = "We came, we saw, we conquered ... then we ate Bill's (Mille-Feuille) cake."
s4 = 'The bill came to five dollars.'
d3 = build_word_cloud_dict(s3)
d4 = build_word_cloud_dict(s4, d3)
print d4

==> 35_inplace_shuffle.py <==
#!/usr/bin/env python

import random

def inplace_shuffle(lst):
    n = len(lst)
    if n < 2: return lst
    for i in xrange(n - 1):
        repl = random.randint(i, n - 1)
        if i != repl: lst[i], lst[repl] = lst[repl], lst[i]
        
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
inplace_shuffle(lst)
print lst

==> 36_single_riffle_check.py <==
#!/usr/bin/env python

def is_single_riffle(shuffled_d, h1, h2):
    if len(shuffled_d) < 2: return True
    # To adhere to DRY.
    h_arr = [h1, h2]
    h_idxes = [0, 0]
        
    for s in shuffled_d:
        if s not in h1 and s not in h2: return False
        h_idx = 0 if s in h1 else 1
        idx = h_arr[h_idx].index(s)
        # Shuffled deck can't have cards from a given half out of order.
        if idx < h_idxes[h_idx]: return False
        h_idxes[h_idx] += 1
    
    # Both halves have to be "exhausted."
    return h_idxes[0] == len(h1) and h_idxes[1] == len(h2)
    
assert is_single_riffle([2, 3, 1, 4, 5], [3, 4, 5], [2, 1])
assert not is_single_riffle([2, 3, 1, 4, 5], [3, 4, 2], [2, 5])
assert not is_single_riffle([1, 2, 3], [2], [3, 1])
print 'Tests passed!'

==> 37_simulate_5sided_die.py <==
#!/usr/bin/env python

from random import randint

def rand7():
    return randint(1, 7)

def rand5():
    acc = 0
    for _ in xrange(5):
        acc += rand7()
    return acc % 5 + 1

def rand5_recursive():
    roll = rand7()
    return roll if roll <= 5 else rand5_recursive()

def driver(n, rand5_func):
    """Test if rand5 returns evenly distributed int from 1 to 5."""
    results = [0] * 5
    for _ in xrange(n):
        res = rand5_func() - 1
        results[res] += 1
    # Also return the proportion.
    return [(r, round(float(r) / sum(results), 3)) for r in results]


if __name__ == '__main__':
    rand5_res = driver(100000, rand5)
    print 'rand5 results: {}'.format(rand5_res)
    diff =  max(rand5_res, key=lambda x: x[1])[1] - min(rand5_res, key=lambda x: x[1])[1]
    print 'max proportion diff: {}'.format(diff)
    rand5_rec_res = driver(100000, rand5_recursive)
    print 'rand5_recursive results: {}'.format(rand5_rec_res)
    diff_rec = max(rand5_rec_res, key=lambda x: x[1])[1] - min(rand5_rec_res, key=lambda x: x[1])[1]
    print 'max proportion diff: {}'.format(diff_rec)

    from timeit import Timer

    import_stmt = 'from __main__ import driver, rand5, rand5_recursive, rand7;'
    setup = import_stmt + 'n = 1000; rand5_func = '

    # min recommended: http://stackoverflow.com/questions/8220801/how-to-use-timeit-module
    rand5_time = round(min(Timer('driver(n, rand5_func)', setup=setup + 'rand5').repeat(3, 100)), 2)
    rand5_rec_time = round(min(Timer('driver(n, rand5_func)', setup=setup + 'rand5_recursive').repeat(3, 100)), 2)

    print 'rand5 time: {}s'.format(rand5_time)
    print 'rand5_recursive time: {}s'.format(rand5_rec_time)

==> 38_simulate_7sided_die.py <==
#!/usr/bin/env python

from random import randint

def rand5():
    return randint(1, 5)

def rand7():
    acc = 0
    for _ in xrange(7):
        acc += rand5()
    return acc % 7 + 1

def rand7_alt():
    while True:
        outcome = (rand5() - 1) * 5 + (rand5() - 1) + 1
        # Get rid of last 4 numbers, since 25 isn't divisible by 7, but 21 is.
        if outcome > 21: continue
        return outcome % 7 + 1

def driver(n, rand7_func):
    """Test if rand7 returns evenly distributed int from 1 to 7."""
    results = [0] * 7
    for _ in xrange(n):
        res = rand7_func() - 1
        results[res] += 1
    # Also return the proportion.
    return [(r, round(float(r) / sum(results), 3)) for r in results]

print driver(10000, rand7)
print driver(10000, rand7_alt)

if __name__ == '__main__':
    from timeit import Timer

    import_stmt = 'from __main__ import driver, rand5, rand7, rand7_alt;'
    setup = import_stmt + 'n = 1000; rand7_func = '

    # min recommended: http://stackoverflow.com/questions/8220801/how-to-use-timeit-module
    rand7_time = round(min(Timer('driver(n, rand7_func)', setup=setup + 'rand7').repeat(3, 100)), 2)
    rand7_alt_time = round(min(Timer('driver(n, rand7_func)', setup=setup + 'rand7_alt').repeat(3, 100)), 2)

    print 'rand7 time: {}s'.format(rand7_time)
    print 'rand7_alt time: {}s'.format(rand7_alt_time)
