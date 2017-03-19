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
