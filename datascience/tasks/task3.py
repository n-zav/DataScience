def init_rivals_matrix(n):
    """
    Initializes the matrix n x n, where n[i] is a list of possible rivals for player i.
    If n[i] == i, value is set to 0.
    """
    possible_rivals = []

    for i in xrange(1, n + 1):
        players = range(1, n + 1)
        players[i - 1] = 0
        possible_rivals.append(players)

    return possible_rivals


def choose_rivals(matrix, n, round_number):
    """
    Creates a list of possible rivals for one round.
    """
    rival_pairs = []
    rival_in_pairs_number = n // 2 * 2  # amount of possible rival pairs in one round.
    black_list = []

    # initialize a black list if we need to go one step back and try to find another solution.
    for i in xrange(0, n):
        black_list.append([])

    # choose rivals from the end of the list if round_number is odd
    # vice versa when round_number is even
    # this is to avoid dead end in case when n is even
    if n % 2 == 1 and round_number % 2 == 0:
        start = n
        end = 1
        step = -1
    else:
        start = 1
        end = n
        step = 1

    # while amount of rival pairs is less than possible amount, we look for pairs.
    while len(rival_pairs) < rival_in_pairs_number:
        for x in xrange(start, end, step):
            if x not in rival_pairs:
                matrix, rival_pairs = find_rival(matrix, x, rival_pairs, black_list[x - 1])

        if len(rival_pairs) < rival_in_pairs_number:
            last_step_back_reached, rival_pairs, matrix, black_list = go_one_step_back(rival_pairs, matrix, black_list)
            if last_step_back_reached:
                for x in xrange(start, end, step):
                    if x not in rival_pairs:
                        matrix, rival_pairs = find_rival(matrix, x, rival_pairs, [])
                break

    return rival_pairs


def go_one_step_back(rival_pairs, matrix, black_list):
    """
    initializes the matrix and the black list as it was one round back
    """
    if len(rival_pairs) > 0:
        y = rival_pairs[-1]
        x = rival_pairs[-2]
        rival_pairs = rival_pairs[0:-2]
        matrix[x - 1][y - 1] = y
        matrix[y - 1][x - 1] = x
        black_list[x - 1].append(y)

        count = 0
        for item in matrix[x-1]:
            if item != 0:
                count += 1
        if count <= len(black_list[x - 1]):
            black_list[x - 1] = []
            return go_one_step_back(rival_pairs, matrix, black_list)
    else:
        return True, rival_pairs, matrix, black_list

    return False, rival_pairs, matrix, black_list


def find_rival(matrix, x, rival_pairs, black_list):
    """
    updates the matrix and rival pairs, when round is played
    """
    for y in matrix[x - 1]:
        if y != 0 and y not in rival_pairs and y not in black_list:
            rival_pairs.append(x)
            rival_pairs.append(y)
            matrix[x - 1][y - 1] = 0
            matrix[y - 1][x - 1] = 0
            break

    return matrix, rival_pairs


def create_list_of_round_pairs(n):
    """
    appends lists of rival pairs after each round until the matrix of possible rivals is empty
    """

    round_number = 1
    matrix = init_rivals_matrix(n)
    round_pairs_list = []

    while sum(sum(matrix, [])) > 0:
        round_pairs = choose_rivals(matrix, n, round_number)
        round_pairs_list.append(round_pairs)
        round_number += 1

    return round_pairs_list


def reverse_round_pairs_list(round_pairs_list):
    """
    creates a reversed list of pairs, which we will use for the second team.
    """

    reversed_round_pairs_list = []

    for i in round_pairs_list:
        reversed_list = i[::-1]
        reversed_round_pairs_list.append(reversed_list)

    return reversed_round_pairs_list


def make_tournament_pairs(n):
    """
    creates a schedule for the tournament
    """

    round_pairs_list = create_list_of_round_pairs(n)
    reversed_round_pairs_list = reverse_round_pairs_list(round_pairs_list)

    pairs = []
    tournament_pairs = []
    for f, b in zip(round_pairs_list, reversed_round_pairs_list):
        for i, j in zip(f, b):
            pairs. append(['a_' + str(i), 'b_' + str(j)])

    for i in xrange(0, len(pairs) - 1, 2):
        tournament_pairs.append([pairs[i], pairs[i + 1]])

    return tournament_pairs
