matrix_string = "1 2\n3 4"
i=1

selfvalues = []

rows = matrix_string.split('\n')

for rownum, row in enumerate(rows):
    selfvalues.append([])
    one_row_as_str = row.split()
    one_row_as_int = list(map(int, one_row_as_str))
    selfvalues[rownum].extend(one_row_as_int)
# flatten list if necessary
if len(one_row_as_str) == 1:
    selfvalues = [[item for sublist in selfvalues for item in sublist]]

print(selfvalues[i])
