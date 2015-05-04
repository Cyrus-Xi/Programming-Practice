# Takes in ordered lists and outputs a top 25 ranking of all the names voted for.

from fileinput import input
from operator import itemgetter

# Handle mapped to list of [ranking points, list of [ranks], and number of ballots appeared on].
pts_dict = {}
discarded = []
num_ballots = 0.0

# Ignore empty lines and delimiters.
for line in [line.strip() for line in input() if line != "\n" and line != "-\n"]:
    count = 1
    pts = 25
    num_ballots += 1

    # Lowercase names to reduce redundancy.
    for name in [name.lower() for name in line.split()]:
        # Stop including votes after 25 posters.
        if count > 25 and name not in discarded: 
            discarded.append(name)

        # If not tied.
        if not "/" in name:
            # Add ranking points if poster already in dict, else set to 0.
            # Add rank (purely a function of pts, 26-pts) to list of ranks.
            # Add 1 to number of ballots if already in, else set to 1.
            if name in pts_dict:
                pts_dict[name][0] += pts
                pts_dict[name][1].append(26-pts)
                pts_dict[name][2] += 1
            else:
                # Initialize value list.
                pts_dict[name] = [pts, [26-pts], 1]
            pts -= 1
        else:
            tied = name.split("/")
            sum_pts = 0
            # If n is number of posters tied at x, each gets 
            # (x + (x-1) + .. + (x-(n-1))) / n pts.
            for poster in tied:
                sum_pts += pts
                pts -= 1 
            avg_pts = sum_pts / len(tied)
            for poster in tied:
                # Same process as non-tied.
                if poster in pts_dict: 
                    pts_dict[poster][0] += avg_pts
                    pts_dict[poster][1].append(26-avg_pts)
                    pts_dict[poster][2] += 1
                else: 
                    pts_dict[poster] = [avg_pts, [26-avg_pts], 1]

        count += 1

# Flatten the list of ranks to get an average rank.
the_dict = {}
for k, v in pts_dict.iteritems():
    real_v = []
    avg_rank = 0
    rank_accum = 0.0
    # Iterate through ranks.
    for rank in v[1]:
        rank_accum += float(rank)
    avg_rank = rank_accum / len(v[1])
    # Round and make pretty.
    avg_rank = float("{0:.1f}".format(avg_rank))
    percent = "{0:.0f}%".format(v[2] / num_ballots * 100)
    # Don't change the other values.
    the_dict[k] = [v[0], avg_rank, v[2], percent]

# Sort by ranking points descending.
real_sorted = sorted(the_dict.items(), key=itemgetter(1), reverse=True)

print "x) handle: RankingPts (AvgRank, NumBallots, %Ballots)\n"
for rank, tup in enumerate(real_sorted):
    # Convert to string and remove brackets.
    output = str(tup[1])[1:-1]
    # Remove first comma.
    output = output.replace(",", "", 1)
    # Surround average ranking and number of ballots with parentheses.
    output = output.replace(" ", " (", 1)
    # Remove single quotes from percent.
    output = output.replace("'", "")
    output += ")"

    print str(rank+1) + ") " + tup[0] + ": " + output
