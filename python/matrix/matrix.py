def convert_into_list_of_int(numstring_list):
    return list(map(int, numstring_list))


class Matrix(object):
    def __init__(self, matrix_string):
        self.all_rows_as_str = matrix_string.split('\n')

    def row(self, i):
        one_row_as_str = self.all_rows_as_str[i]
        return convert_into_list_of_int(one_row_as_str.split())

    def column(self, i):
        return [convert_into_list_of_int(this_row.split())[i] for this_row in self.all_rows_as_str]
