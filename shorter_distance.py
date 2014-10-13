#!/usr/bin/env python

"""
Adapted from shorter_detour to be more general.

Returns the shorter route. Each route can contain an
arbitary number of longitude-latitude point tuples.

By Cyrus Xi.
"""

from math import radians, cos, sin, asin, sqrt


def get_shorter_distance(route1, route2):
    """
    Return the shorter route.

    Each route is a tuple containing point tuples of longitude
    and latitude. Uses the haversine formula.

    :param route1 tuple that contains lon-lat point tuples
    :param route2 tuple that contains lon-lat point tuples
    :return:      the tuple that represents the shorter route
    """
    # Save more reader-friendly versions for output later.
    out_rt1, out_rt2 = route1, route2

    # For each route.
    for index, route in enumerate([route1, route2]):
        # Flatten list of tuple points into list of coordinates.
        coords = [coord for pt in route for coord in pt]
        # Convert into radians and pack back into point tuples.
        pts = [pt for pt in zip(map(radians, coords)[::2],
                                map(radians, coords)[1::2])]
        # Round floats to 3 decimal places.
        pts = [(round(pt[0], 3), round(pt[1], 3)) for pt in pts]
        # Put back into route tuple.
        if index == 0:
            route1 = pts
        else:
            assert index == 1
            route2 = pts

    # Radius of Earth in miles.
    radius = 3963.2

    routes = route1, route2
    dist1, dist2 = 0, 0

    for index, route in enumerate(routes):
        # Pairwise iterate for simplicity.
        for (lon1, lat1), (lon2, lat2) in zip(route[:-1], route[1:]):
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

    return out_rt1 if dist1 < dist2 else out_rt2


def main():
    """Testing."""
    ptA = 1, 3
    ptB = 3, 7
    ptC = 2, 5
    ptD = 1, 6
    route1 = (ptA, ptB, ptC, ptD)

    ptE = 1, 8
    ptF = 2, 3
    ptG = 4, 2
    route2 = (ptE, ptF, ptG)

    print get_shorter_distance(route1, route2)


if __name__ == '__main__':
    main()