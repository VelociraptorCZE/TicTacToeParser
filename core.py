"""
    TicTacToeParser
    Copyright(C) Simon Raichl 2018
    MIT License
"""


class Core:
    @staticmethod
    def get_board():
        filename = input("Specify the path to your file:\n")
        try:
            return Core().parse_file(filename)
        except FileNotFoundError:
            print("File not found! Try it again.")
            return Core().get_board()

    def parse_file(self, filename):
        file = open(filename, "r")
        content = file.read()
        print("\nBoard:\n\n" + content + "\n")
        lines = content.split()
        field = []
        line_id = 0
        for line in lines:
            char_id = 0
            row = []
            while char_id < len(line):
                row.append(line[char_id])
                char_id += 1
            field.append(row)
            line_id += 1
        return Core().get_results(field)

    def get_results(self, field):
        result = "No winner"
        row_id = 0
        while row_id < len(field):
            char_id = 0
            temp_res = []
            length = len(field[row_id])
            while char_id < length:
                char = field[row_id][char_id]
                params = [field, char, [row_id, char_id]]
                "checking row"
                temp_res.append(Core().check(params, 0, 1))
                "checking column"
                temp_res.append(Core().check(params, 1, 0))
                "checking diagonal from left to right bottom"
                temp_res.append(Core().check(params, 1, 1))
                "checking diagonal from left to right top"
                temp_res.append(Core().check(params, -1, 1))
                if True in temp_res:
                    result = char + " won!"
                    break
                char_id += 1
            row_id += 1
        return result

    def check(self, params, x, y):
        i = 0
        "[0] field"
        "[1] char"
        "[2] coords => array[x, y]"
        new_x = params[2][0]
        new_y = params[2][1]
        result = True
        while i < 4:
            new_x += x
            new_y += y
            try:
                if params[1] != params[0][new_x][new_y]:
                    result = False
                    break
            except IndexError:
                result = False
                break
            i += 1

        return result
