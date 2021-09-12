'''
Cinderella's stepmother has newly bought n bolts and n nuts. 
The bolts and the nuts are of different sizes, each of them is from size 1 to size n. 
So, each bolt has exactly one nut just fitting it. 
These bolts and nuts have the same appearance so that we cannot distinguish a bolt from another bolt, 
or a nut from another nut, just by looking at them. 
Fortunately, we can compare a bolt with a nut by screwing them together, to see if the size of the bolt is too large, 
or just fitting, or too small, for the nut. Cinderella wants to join the ball held by Prince Charming. 
But now, her wicked stepmother has mixed the bolts, and mixed the nuts, and tells her that she can go to the ball unless she can find the largest bolt 
and the largest nut in time. An obvious way is to compare each bolt with each nut, but that will take n2 comparisons (which is too long). 
Can you help Cinderella to find  an algorithm requiring only o(n2) comparisons? For instance, O(n) comparisons?
'''


def find_largest_match(nuts, bolts):
    # Starting with first nut and bolt.
    index_nuts = 0
    index_bolts = 0
    match = {
        "nut": 0,
        "bolt": 0
    }

    # Go through nuts and bolts but stop when you get to last one.
    while index_nuts < len(nuts) and index_bolts < len(bolts):

        # If one is smaller than the other.
        # Set aside the smallest item and pick up another one
        if nuts[index_nuts] < bolts[index_bolts]:
            index_nuts += 1
        elif bolts[index_bolts] < nuts[index_nuts]:
            index_bolts += 1
        else:
            # If they are equal, mark as the match, set aside the nut and pick up another
            match = {
                "nut": nuts[index_nuts],
                "bolt": bolts[index_bolts]
            }
            index_nuts += 1

    return match


if __name__ == "__main__":
    nuts = [0, 1, 2, 3, 4, 5, 6, 15, 7, 12, 8, 16, 9, 10, 14]
    bolts = [8, 7, 6, 12, 5, 16, 9, 10, 15, 14, 4, 3, 2, 1, 0]

    print(find_largest_match(nuts, bolts))
