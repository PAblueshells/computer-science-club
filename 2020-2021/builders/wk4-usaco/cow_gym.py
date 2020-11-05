with open("gymnastics.in", "r") as fin:
    K, N = [int(i) for i in fin.readline().split()]
    sessions = [tuple(map(int, line.split())) for line in fin]

consistent_pairs = 0

# loop through the pairs of cows
for cow1 in range(1,N+1): # adjust indexing so that cow1 goes from 1...N instead of 0...N-1
    for cow2 in range(cow1+1, N+1):
        # print(f'pair: {cow1} {cow2}')

        cow1_wins = 0 # count the number of times cow 1 wins

        # loop through all K sessions
        for session in sessions:
            # determine the positions of the cows
            cow1_pos = session.index(cow1)
            cow2_pos = session.index(cow2)

            if cow1_pos < cow2_pos:
                cow1_wins += 1


        # check for consistency (cow1 should win either all the rounds or none of them)
        if cow1_wins in [0,K]:
            consistent_pairs += 1

with open("gymnastics.out", "w+") as fout:
    print(consistent_pairs, file=fout)
  