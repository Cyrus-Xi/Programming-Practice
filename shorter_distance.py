#!/usr/bin/env python

from math import radians, cos, sin, asin, sqrt


def get_shorter_distance(ptA, ptB, ptC, ptD):
    """
    Return the shorter detour as a tuple.

    Specifically, shorter detour means whether it's a shorter
    distance to go from A to C to D to B or whether shorter to go
    from C to A to B to D.

    :param ptA: a tuple of latitude and longitude representing point A
    :param ptB: a tuple of latitude and longitude representing point B
    :param ptC: a tuple of latitude and longitude representing point C
    :param ptD: a tuple of latitude and longitude representing point D
    :return:    the tuple of the 4 pts in the shorter detour's order
    """
    # Flatten list of tuple points into list of coordinates.
    coords = [coord for pt in [ptA, ptB, ptC, ptD] for coord in pt]

    # Convert into radians and pack back into point tuples.
    pts = [tup for tup in zip(map(radians, coords)[::2],
                              map(radians, coords)[1::2])]
    # Round floats to 3 decimal places.
    ptA, ptB, ptC, ptD = [(round(pt[0], 3), round(pt[1], 3)) for pt in pts]

    # Radius of Earth in miles.
    radius = 3963.2

    detours = det1, det2 = (ptA, ptC, ptD, ptB), (ptC, ptA, ptB, ptD)
    dist1, dist2 = 0, 0

    for index, det in enumerate(detours):
        # Pairwise iterate for simplicity.
        for (lon1, lat1), (lon2, lat2) in zip(det[:-1], det[1:]):
            # Use haversine formula.
            dlon = lon2 - lon1
            dlat = lat2 - lat1
            a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
            c = 2 * asin(sqrt(a))
            dist = c * radius
            if index == 0:
                dist1 += dist
            else:
                dist2 += dist

    return det1 if dist1 < dist2 else det2


def main():
    ptA = 1, 3
    ptB = 3, 7
    ptC = 2, 5
    ptD = 1, 6

    print get_shorter_detour(ptA, ptB, ptC, ptD)


if __name__ == '__main__':
    main()