import copy


def init_rivals_matrix(n):
    possible_rivals = []

    for i in xrange(1, n + 1):
        players = range(1, n + 1)
        players.remove(i)
        possible_rivals.append(players)
    return possible_rivals


def choose_rivals(matrix, n):
    rival_pairs = []
    rival_pairs_number = n // 2 * 2
    new_matrix = copy.deepcopy(matrix)

    while len(rival_pairs) < rival_pairs_number:
        for x in xrange(1, n):
            if x not in rival_pairs:
                rival_pairs, new_matrix = find_rival(matrix, x, rival_pairs, new_matrix, [])

        if len(rival_pairs) < rival_pairs_number:
            y = rival_pairs[-1]
            x = rival_pairs[-2]
            black_list = [y]
            rival_pairs.remove(y)
            rival_pairs.remove(x)
            # new_matrix[x - 1].append(y)
            new_matrix[x - 1][y - 1] = y
            new_matrix[y - 1][x - 1] = x
            rival_pairs, new_matrix = find_rival(matrix, x, rival_pairs, new_matrix, black_list)

    return rival_pairs, new_matrix


def find_rival(matrix, x, rival_pairs, new_matrix, black_list):

    for y in matrix[x - 1]:
        if y not in rival_pairs and y not in black_list:
            rival_pairs.append(x)
            rival_pairs.append(y)
            new_matrix[x - 1].remove(y)
            new_matrix[y - 1].remove(x)
            break
    return rival_pairs, new_matrix


n = 6
possible_rivals = init_rivals_matrix(n)
round1_pairs, matrix1 = choose_rivals(possible_rivals, n)
print(round1_pairs)
print(matrix1)
round2_pairs, matrix2 = choose_rivals(matrix1, n)
print(round2_pairs)
print(matrix2)

round3_pairs, matrix3 = choose_rivals(matrix2, n)
print(round3_pairs)
print(matrix3)

round4_pairs, matrix4 = choose_rivals(matrix3, n)
print(round4_pairs)
print(matrix4)

round5_pairs, matrix5 = choose_rivals(matrix4, n)
print(round5_pairs)
print(matrix5)
