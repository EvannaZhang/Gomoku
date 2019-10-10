import numpy as np
import random

COLOR_BLACK = 1
COLOR_WHITE = -1
COLOR_NONE = 0
random.seed(0)


def get_possible_moves(chessboard, size):
    center = [size // 2, size // 2]
    circle = 0
    possible_moves = []
    for i in range(8):
        empty = True

        if i == 0:
            points_c = [[size // 2, size // 2]]
        else:
            points_c = [[7 - i, c] for c in range(7 - i, 7 + i)] + \
                       [[r, 7 + i] for r in range(7 - i, 7 + i)] + \
                       [[7 + i, c] for c in range(7 + i, 7 - i, -1)] + \
                       [[r, 7 - i] for r in range(7 + i, 7 - i, -1)]

        for points in points_c:
            if int(chessboard[points[0]][points[1]]) == 0:
                possible_moves.append(points)
            else:
                empty = False

        if empty == True:
            circle += 1
            if circle == 15:
                break
        else:
            circle = 0
    return possible_moves


def get_scores(chessboard, move, size, color):
        # print(move)
        x = move[0]
        y = move[1]
        sum_score = 0
        hang_c = 0
        hang_c_zuo = 0
        hang_c_you = 0
        hang_unc = 0
        hang_unc_zuo = 0
        hang_unc_you = 0
        hang_empty_c = 0
        hang_empty_unc = 0
        hang_tiao = 0
        hang_un_tiao = 0
        while y > 0:
            y = y - 1
            if int(chessboard[x][y]) == color:
                hang_c_zuo += 1
            elif int(chessboard[x][y]) == 0:
                hang_empty_c += 1
                if y == move[1] - 1:
                    hang_empty_unc += 1
                if y - 2 > -1:
                    if int(chessboard[x][y - 1]) == color and int(chessboard[x][y - 2]) != -color:
                        hang_tiao += 1
                    if int(chessboard[x][y - 1]) == -color and int(chessboard[x][y - 2]) != color:
                        hang_un_tiao += 1
                break
            elif int(chessboard[x][y]) == -color:
                if y == move[1] - 1:
                    hang_unc_zuo += 1
                    while y > 0:
                        y = y - 1
                        if int(chessboard[x][y]) == -color:
                            hang_unc_zuo += 1
                        elif int(chessboard[x][y]) == 0:
                            hang_empty_unc += 1
                            if y - 2 > -1:
                                if int(chessboard[x][y - 1]) == -color and int(chessboard[x][y - 2]) != color:
                                    hang_un_tiao += 1
                            break
                        else:
                            break
                break
        hang_c = hang_c_zuo
        hang_unc = hang_unc_zuo
        hang_unc += 1
        hang_c += 1
        x = move[0]
        y = move[1]
        while y < 14:
            y = y + 1
            if int(chessboard[x][y]) == color:
                hang_c_you += 1
            elif int(chessboard[x][y]) == 0:
                hang_empty_c += 1
                if y == move[1] + 1:
                    hang_empty_unc += 1
                if y + 2 < 15:
                    if int(chessboard[x][y + 1]) == color and int(chessboard[x][y + 2]) != -color:
                        hang_tiao += 1
                    if int(chessboard[x][y + 1]) == -color and int(chessboard[x][y + 2]) != color:
                        hang_un_tiao += 1
                break
            elif int(chessboard[x][y]) == -color:
                if y == move[1] + 1:
                    hang_unc_you += 1
                    while y < 14:
                        y = y + 1
                        if int(chessboard[x][y]) == -color:
                            hang_unc_you += 1
                        elif int(chessboard[x][y]) == 0:
                            hang_empty_unc += 1
                            if y + 2 < 15:
                                if int(chessboard[x][y + 1]) == -color and int(chessboard[x][y + 2]) != color:
                                    hang_un_tiao += 1

                            break
                        else:
                            break
                break
        hang_c += hang_c_you
        hang_unc += hang_unc_you

        lie_c = 0
        lie_c_zuo = 0
        lie_c_you = 0
        lie_unc = 0
        lie_unc_zuo = 0
        lie_unc_you = 0
        lie_empty_c = 0
        lie_empty_unc = 0
        lie_tiao = 0
        lie_un_tiao = 0
        x = move[0]
        y = move[1]
        while x > 0:
            x = x - 1
            if int(chessboard[x][y]) == color:
                lie_c_zuo += 1
            elif int(chessboard[x][y]) == 0:
                lie_empty_c += 1
                if x == move[0] - 1:
                    lie_empty_unc += 1
                if x - 2 > -1:
                    if int(chessboard[x - 1][y]) == color and int(chessboard[x - 2][y]) != -color:
                        lie_tiao += 1
                    if int(chessboard[x - 1][y]) == -color and int(chessboard[x - 2][y]) != color:
                        lie_un_tiao += 1
                break
            elif int(chessboard[x][y]) == -color:
                if x == move[0] - 1:
                    lie_unc_zuo += 1
                    while x > 0:
                        x = x - 1
                        if int(chessboard[x][y]) == -color:
                            lie_unc_zuo += 1
                        elif int(chessboard[x][y]) == 0:
                            lie_empty_unc += 1
                            if x - 2 > 0:
                                if int(chessboard[x - 1][y]) == -color and int(chessboard[x - 2][y]) != color:
                                    lie_un_tiao += 1
                            break
                        else:
                            break
                break
        x = move[0]
        y = move[1]
        lie_c = lie_c_zuo
        lie_unc = lie_unc_zuo
        lie_c += 1
        lie_unc += 1
        while x < 14:
            x = x + 1
            if int(chessboard[x][y]) == color:
                lie_c_you += 1
            elif int(chessboard[x][y]) == 0:
                lie_empty_c += 1
                if x == move[0] + 1:
                    lie_empty_unc += 1
                if x + 2 < 15:
                    if int(chessboard[x + 1][y]) == color and int(chessboard[x + 2][y]) != -color:
                        lie_tiao += 1
                    if int(chessboard[x + 1][y]) == -color and int(chessboard[x + 2][y]) != color:
                        lie_un_tiao += 1
                break
            elif int(chessboard[x][y]) == -color:
                if x == move[0] + 1:
                    lie_unc_you += 1
                    while x < 14:
                        x = x + 1
                        if int(chessboard[x][y]) == -color:
                            lie_unc_you += 1
                        elif int(chessboard[x][y]) == 0:
                            lie_empty_unc += 1
                            if x + 2 < 15:
                                if int(chessboard[x + 1][y]) == -color and int(chessboard[x + 2][y]) != color:
                                    lie_un_tiao += 1
                            break
                        else:
                            break
                break

        lie_c += lie_c_you
        lie_unc += lie_unc_you

        x = move[0]
        y = move[1]

        youxia_c = 0
        youxia_c_zuo = 0
        youxia_c_you = 0
        youxia_unc = 0
        youxia_unc_zuo = 0
        youxia_unc_you = 0
        youxia_empty_c = 0
        youxia_empty_unc = 0
        youxia_tiao = 0
        youxia_un_tiao = 0
        while x > 0 and y > 0:
            x = x - 1
            y = y - 1
            if int(chessboard[x][y]) == color:
                youxia_c_zuo += 1
            elif int(chessboard[x][y]) == 0:
                youxia_empty_c += 1
                if x == move[0] - 1 and y == move[1] - 1:
                    youxia_empty_unc += 1
                if x - 2 > -1 and y - 2 > -1:
                    if int(chessboard[x - 1][y - 1]) == color and int(chessboard[x - 2][y - 2]) != -color:
                        youxia_tiao += 1
                    if int(chessboard[x - 1][y - 1]) == -color and int(chessboard[x - 2][y - 2]) != color:
                        youxia_un_tiao += 1
                break
            elif int(chessboard[x][y]) == -color:
                if x == move[0] - 1 and y == move[1] - 1:
                    youxia_unc_zuo += 1
                    while x > 0 and y > 0:
                        x = x - 1
                        y = y - 1
                        if int(chessboard[x][y]) == -color:
                            youxia_unc_zuo += 1
                        elif int(chessboard[x][y]) == 0:
                            youxia_empty_unc += 1
                            if x - 2 > -1 and y - 2 > -1:
                                if int(chessboard[x - 1][y - 1]) == -color and int(chessboard[x - 2][y - 2]) != color:
                                    youxia_un_tiao += 1
                            break
                        else:
                            break
                break
        x = move[0]
        y = move[1]
        youxia_c = youxia_c_zuo
        youxia_unc = youxia_unc_zuo
        youxia_c += 1
        youxia_unc += 1
        while x < 14 and y < 14:
            x = x + 1
            y = y + 1
            if int(chessboard[x][y]) == color:
                youxia_c_you += 1
            elif int(chessboard[x][y]) == 0:
                youxia_empty_c += 1
                if x == move[0] + 1 and y == move[1] + 1:
                    youxia_empty_unc += 1
                if x + 2 < 15 and y + 2 < 15:
                    if int(chessboard[x + 1][y + 1]) == color and int(chessboard[x + 2][y + 2]) != -color:
                        youxia_tiao += 1
                    if int(chessboard[x + 1][y + 1]) == -color and int(chessboard[x + 2][y + 2]) != color:
                        youxia_un_tiao += 1
                break
            elif int(chessboard[x][y]) == -color:
                if x == move[0] + 1 and y == move[1] + 1:
                    youxia_unc_you += 1
                    while x < 14 and y < 14:
                        x = x + 1
                        y = y + 1
                        if int(chessboard[x][y]) == -color:
                            youxia_unc_you += 1
                        elif int(chessboard[x][y]) == 0:
                            youxia_empty_unc += 1
                            if x + 2 < 15 and y + 2 < 15:
                                if int(chessboard[x + 1][y + 1]) == -color and int(chessboard[x + 2][y + 2]) != color:
                                    youxia_un_tiao += 1
                            break
                        else:
                            break
                break

        youxia_c += youxia_c_you
        youxia_unc += youxia_unc_you

        x = move[0]
        y = move[1]
        youshang_c = 0
        youshang_c_zuo = 0
        youshang_c_you = 0
        youshang_unc = 0
        youshang_unc_zuo = 0
        youshang_unc_you = 0
        youshang_empty_c = 0
        youshang_empty_unc = 0
        youshang_tiao = 0
        youshang_un_tiao = 0
        while x > 0 and y < 14:
            x = x - 1
            y = y + 1
            if int(chessboard[x][y]) == color:
                youshang_c_zuo += 1
            elif int(chessboard[x][y]) == 0:
                youshang_empty_c += 1
                if x == move[0] - 1 and y == move[1] + 1:
                    youshang_empty_unc += 1
                if x - 2 > -1 and y + 2 < 15:
                    if int(chessboard[x - 1][y + 1]) == color and int(chessboard[x - 2][y + 2]) != -color:
                        youshang_tiao += 1
                    if int(chessboard[x - 1][y + 1]) == -color and int(chessboard[x - 2][y + 2]) != color:
                        youshang_un_tiao += 1
                break
            elif int(chessboard[x][y]) == -color:
                if x == move[0] - 1 and y == move[1] + 1:
                    youshang_unc_zuo += 1
                    while x > 0 and y < 14:
                        x = x - 1
                        y = y + 1
                        if int(chessboard[x][y]) == -color:
                            youshang_unc_zuo += 1
                        elif int(chessboard[x][y]) == 0:
                            youshang_empty_unc += 1
                            if x - 2 > -1 and y + 2 < 15:
                                if int(chessboard[x - 1][y + 1]) == -color and int(chessboard[x - 2][y + 2]) != color:
                                    youshang_un_tiao += 1
                            break
                        else:
                            break
                break
        x = move[0]
        y = move[1]
        youshang_c = youshang_c_zuo
        youshang_unc = youshang_unc_zuo
        youshang_c += 1
        youshang_unc += 1
        while x < 14 and y > 0:
            x = x + 1
            y = y - 1
            if int(chessboard[x][y]) == color:
                youshang_c_you += 1
            elif int(chessboard[x][y]) == 0:
                youshang_empty_c += 1
                if x == move[0] + 1 and y == move[1] - 1:
                    youshang_empty_unc += 1
                if y - 2 > -1 and x + 2 < 15:
                    if int(chessboard[x + 1][y - 1]) == color and int(chessboard[x + 2][y - 2]) != -color:
                        youshang_tiao += 1
                    if int(chessboard[x + 1][y - 1]) == -color and int(chessboard[x + 2][y - 2]) != color:
                        youshang_un_tiao += 1
                break
            elif int(chessboard[x][y]) == -color:
                if x == move[0] + 1 and y == move[1] - 1:
                    youshang_unc_you += 1
                    while x < 14 and y > 0:
                        x = x + 1
                        y = y - 1
                        if int(chessboard[x][y]) == -color:
                            youshang_unc_you += 1
                        elif int(chessboard[x][y]) == 0:
                            youshang_empty_unc += 1
                            if y - 2 > -1 and x + 2 < 15:
                                if int(chessboard[x + 1][y - 1]) == -color and int(chessboard[x + 2][y - 2]) != color:
                                    youshang_un_tiao += 1
                            break
                        else:
                            break
                break
        youshang_c += youshang_c_you
        youshang_unc += youshang_unc_you
        # scores_c = [2000, 50, 40, 4, 2, 2, 1, 1]
        # scores_unc = [500, 30, 19, 3, 1, 1, 0, 0]

        scores_c = [10000, 3000, 1700, 50, 70, 20, 5, 2]
        scores_unc = [4000, 1800, 1000, 40, 60, 10, 3, 1]
        num_c = [0, 0, 0, 0, 0, 0, 0, 0]
        num_unc = [0, 0, 0, 0, 0, 0, 0, 0]
        if hang_tiao == 2:
            hang_tiao = 1
        if lie_tiao == 2:
            lie_tiao = 1
        if youshang_tiao == 2:
            youshang_tiao = 1
        if youxia_tiao == 2:
            youxia_tiao = 1
        if hang_un_tiao == 2:
            hang_un_tiao = 1
        if lie_un_tiao == 2:
            lie_un_tiao = 1
        if youshang_un_tiao == 2:
            youshang_un_tiao = 1
        if youxia_un_tiao == 2:
            youxia_un_tiao = 1
        hang_c += hang_tiao
        lie_c += lie_tiao
        youshang_c += youshang_tiao
        youxia_c += youxia_tiao
        hang_unc += hang_un_tiao
        lie_unc += lie_un_tiao
        youshang_unc += youshang_un_tiao
        youxia_unc += youxia_un_tiao

        if hang_c >= 5:
            sum_score += 1000000
            if hang_c_zuo > 0 and hang_c_you > 0:
                sum_score += 3000000
        elif hang_empty_c > 0:
            num_c[(4 - hang_c) * 2 + 2 - hang_empty_c] += 1

        if lie_c >= 5:
            sum_score += 1000000
            if lie_c_zuo > 0 and lie_c_you > 0:
                sum_score += 3000000
        elif lie_empty_c > 0:
            num_c[(4 - lie_c) * 2 + 2 - lie_empty_c] += 1

        if youshang_c >= 5:
            sum_score += 1000000
            if youshang_c_zuo > 0 and youshang_c_you > 0:
                sum_score += 3000000
        elif youshang_empty_c > 0:
            num_c[(4 - youshang_c) * 2 + 2 - youshang_empty_c] += 1

        if youxia_c >= 5:
            sum_score += 1000000
            if youxia_c_zuo > 0 and youxia_c_you > 0:
                sum_score += 3000000
        elif youxia_empty_c > 0:
            num_c[(4 - youxia_c) * 2 + 2 - youxia_empty_c] += 1

        if hang_unc >= 5:
            sum_score += 30000
            if hang_unc_zuo > 0 and hang_unc_you > 0:
                sum_score += 50000
        elif hang_empty_unc > 0:
            num_unc[(4 - hang_unc) * 2 + 2 - hang_empty_unc] += 1

        if lie_unc >= 5:
            sum_score += 30000
            if lie_unc_zuo > 0 and lie_unc_you > 0:
                sum_score += 50000
        elif lie_empty_unc > 0:
            num_unc[(4 - lie_unc) * 2 + 2 - lie_empty_unc] += 1

        if youshang_unc >= 5:
            sum_score += 30000
            if youshang_unc_zuo > 0 and youshang_unc_you > 0:
                sum_score += 50000
        elif youshang_empty_unc > 0:
            num_unc[(4 - youshang_unc) * 2 + 2 - youshang_empty_unc] += 1

        if youxia_unc >= 5:
            sum_score += 30000
            if youxia_unc_zuo > 0 and youxia_unc_you > 0:
                sum_score += 50000
        elif youxia_empty_unc > 0:
            num_unc[(4 - youxia_unc) * 2 + 2 - youxia_empty_unc] += 1

        if hang_c == 4 and hang_empty_c == 2 and hang_c_zuo > 0 and hang_c_you > 0:
            sum_score += 5000
        if lie_c == 4 and lie_empty_c == 2 and lie_c_zuo > 0 and lie_c_you > 0:
            sum_score += 5000
        if youshang_c == 4 and youshang_empty_c == 2 and youshang_c_zuo > 0 and youshang_c_you > 0:
            sum_score += 5000
        if youxia_c == 4 and youxia_empty_c == 2 and youxia_c_zuo > 0 and youxia_c_you > 0:
            sum_score += 5000
        if hang_unc == 4 and hang_empty_unc == 2 and hang_unc_zuo > 0 and hang_unc_you > 0:
            sum_score += 2000
        if lie_unc == 4 and lie_empty_unc == 2 and lie_unc_zuo > 0 and lie_unc_you > 0:
            sum_score += 2000
        if youshang_unc == 4 and youshang_empty_unc == 2 and youshang_unc_zuo > 0 and youshang_unc_you > 0:
            sum_score += 2000
        if youxia_unc == 4 and youxia_empty_unc == 2 and youxia_unc_zuo > 0 and youxia_unc_you > 0:
            sum_score += 2000

        if hang_c == 3 and hang_empty_c == 2 and hang_c_zuo > 0 and hang_c_you > 0:
            sum_score += 700
        if lie_c == 3 and lie_empty_c == 2 and lie_c_zuo > 0 and lie_c_you > 0:
            sum_score += 700
        if youshang_c == 3 and youshang_empty_c == 2 and youshang_c_zuo > 0 and youshang_c_you > 0:
            sum_score += 700
        if youxia_c == 3 and youxia_empty_c == 2 and youxia_c_zuo > 0 and youxia_c_you > 0:
            sum_score += 700
        if hang_unc == 3 and hang_empty_unc == 2 and hang_unc_zuo > 0 and hang_unc_you > 0:
            sum_score += 400
        if lie_unc == 3 and lie_empty_unc == 2 and lie_unc_zuo > 0 and lie_unc_you > 0:
            sum_score += 400
        if youshang_unc == 3 and youshang_empty_unc == 2 and youshang_unc_zuo > 0 and youshang_unc_you > 0:
            sum_score += 400
        if youxia_unc == 3 and youxia_empty_unc == 2 and youxia_unc_zuo > 0 and youxia_unc_you > 0:
            sum_score += 400

        for i in range(0, 8):
            if num_c[i] <= 2:
                sum_score += scores_c[i] * num_c[i]
            else:
                sum_score += scores_c[i] * 2
            if num_unc[i] <= 2:
                sum_score += scores_unc[i] * num_unc[i]
            else:
                sum_score += scores_unc[i] * 2

        if num_c[1] >= 2:
            sum_score += 5000


        if move[0] == 7 and move[1] == 2:
            print move[0], move[1]
            print 'hang_c =', hang_c
            print 'lie_c =', lie_c
            print 'youxia_c =', youxia_c
            print 'youshang_c =', youshang_c
            print 'hang_emp =', hang_empty_c
            print 'lie_emp =', lie_empty_c
            print 'youxia_emp =', youxia_empty_c
            print 'youshang_emp =', youshang_empty_c
            print
            print 'hang_unc =', hang_unc
            print 'lie_unc =', lie_unc
            print 'youxia_unc =', youxia_unc
            print 'youshang_unc =', youshang_unc
            print 'hang_emp_unc =', hang_empty_unc
            print 'lie_emp_unc =', lie_empty_unc
            print 'youxia_emp_unc =', youxia_empty_unc
            print 'youshang_emp_unc =', youshang_empty_unc
            print "sum_score", sum_score

        return sum_score


class AI(object):
    # chessboard_size, color, time_out passed from agent
    def __init__(self, chessboard_size, color, time_out):
        self.chessboard_size = chessboard_size
        # You are white or black
        self.color = color
        # the max time you should use, your algorithm's run time must not exceed the time limit.
        self.time_out = time_out
        # You need add your decision into your candidate_list. System will get the end of your candidate_list as your decision .
        self.candidate_list = []

    def go(self, chessboard):
        # Clear candidate_list
        self.candidate_list.clear()

        '''
        input:
        chessboard, self.chessboard_size, self.color, self.time_out
        output:
        new_pos = [x,y]
        assert chessboard[new_pos[0],new_pos[1]]== COLOR_NONE
        self.candidate_list.append(new_pos) 
        '''
        possible_moves = get_possible_moves(chessboard, self.chessboard_size)

        scores = []
        for moves in possible_moves:
            s = get_scores(chessboard, moves, self.chessboard_size, self.color)
            scores.append(s)

        max_score = max(scores)
        best_move = possible_moves[scores.index(max_score)]
        # print(best_move[0], best_move[1])

        # assert chessboard[best_move[0], best_move[1]] == COLOR_NONE

        self.candidate_list.append(best_move)

    # Write your algorithm here
    # Here is the simplest sample:Random decision.
    '''
        idx = np.where(chessboard == COLOR_NONE) #return index
        idx = list(zip(idx[0], idx[1]))
        pos_idx = random.randint(0, len(idx)-1)
        new_pos = idx[pos_idx]
        assert chessboard[new_pos[0],new_pos[1]]== COLOR_NONE

    #Add your decision into candidate_list, Records the chess board
        self.candidate_list.append(new_pos)
    '''


def main():

    chessboard = np.zeros((15, 15), dtype=np.int)
    chessboard[2, 3] = 1
    chessboard[2, 6] = -1
    chessboard[3, 3] = 1
    chessboard[3, 5:7] = 1
    chessboard[4, 4] = 1
    chessboard[4, 5] = -1
    chessboard[5, 2:4] = 1
    chessboard[5, 4] = -1
    chessboard[6, 2:4] = -1
    possible_moves = get_possible_moves(chessboard, 15)
    scores = []
    for moves in possible_moves:
        s = get_scores(chessboard, moves, 15, -1)
        scores.append(s)

    max_score = max(scores)
    number = len(scores)
    if number == 225:
        best_move = list([7,7])

    best_move = list(possible_moves[scores.index(max_score)])
    print("Color is: white")
    print('Move is: ')
    print(best_move)


if __name__ == '__main__':
    main()
