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
