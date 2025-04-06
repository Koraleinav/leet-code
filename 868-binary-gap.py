"""
A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.

For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no binary gaps. The number 32 has binary representation 100000 and has no binary gaps.

Write a function:

def solution(N)

that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.

For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5. Given N = 32 the function should return 0, because N has binary representation '100000' and thus no binary gaps.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..2,147,483,647].

"""

"""
We need to find the longest sequence of 0s in a binary number that is:

Surrounded by 1s on both sides.

This means:

The gap must start after a 1.

The gap must end before the next 1.

Gaps at the start or end don't count if not closed by another 1.

"""

def solution(N):
    binary_num = bin(N)[2:]
    max_gap = 0
    current_gap = 0
    isGapCurrent = False

    for digit in binary_num:
        if digit == '1':
            if isGapCurrent:
                max_gap = max(current_gap, max_gap )
            isGapCurrent = True
            current_gap = 0
        elif isGapCurrent:
            current_gap += 1
    return max_gap


print(solution(1041))



# return a list of all binary gap lengths, not just the longest one.

def get_all_binary_gaps(N):
    gaps = []
    current_gap = 0
    found_one = False

    while N > 0:
        if N & 1:  # &1 is a way to fins the last bit in a binary , like % 10 in decimal
            if found_one and current_gap > 0:
                gaps.append(current_gap)
            found_one = True
            current_gap = 0
        elif found_one:
            current_gap += 1
        N >>= 1  # move to the next bit

    return gaps


# return the position (start & end indexes) of each gap

def get_binary_gap_positions(N):
    binary_str = bin(N)[2:]
    gaps = []
    start = None

    for i, bit in enumerate(binary_str):
        if bit == '1':
            if start is not None and i - start - 1 > 0:
                gaps.append({
                    'start': start,
                    'end': i,
                    'length': i - start - 1
                })
            start = i

    return gaps
