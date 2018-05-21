import unittest


# Q1
def half(matrix, k=1):
    return [matrix[j][:j + 1] if k == 1 else matrix[j][j:] for j in range(len(matrix))]


# Q2
def decrypt(string='vrorqjdqgwkdqnviruwkhilvk', key=3):
    res = ''
    for letter in string:
        res += chr((ord(letter) - key - ord('a')) % (ord('z') + 1 - ord('a')) + ord('a'))
    return res


# Q3
def merge_sorted_lists(list1, list2):
    first = iter(list1)
    second = iter(list2)
    first_temp = next(first, -1)
    second_temp = next(second, -1)

    while first_temp != -1 and second_temp != -1:
        if first_temp <= second_temp:
            yield first_temp
            first_temp = next(first, -1)
        else:
            yield second_temp
            second_temp = next(second, -1)

    if first_temp != -1:
        while first_temp != -1:
            yield first_temp
            first_temp = next(first, -1)
    if second_temp != -1:
        while second_temp != -1:
            yield second_temp
            second_temp = next(second, -1)


# Q4
def rank(file_name, how_to_rank='total'):
    dictionary = {}
    res = []
    with open(file_name) as f:
        for line in f:
            nation, medal_list = line.split(" ", 1)
            dictionary[nation] = [int(i) for i in medal_list.split()]
    if how_to_rank == 'total':
        for key, value in sorted(dictionary.items(), key=lambda i: sum(i[1]), reverse=True):
            res.append(key + " : " + str(sum(value)))
    elif how_to_rank == 'weighted':
        for key, value in sorted(dictionary.items(), key=lambda i: i[1][0] * 3 + i[1][1] * 2 + i[1][2], reverse=True):
            res.append(key + " : " + str(value[0] * 3 + value[1] * 2 + value[2]))
    elif how_to_rank == 'gold':
        for key, value in sorted(dictionary.items(), key=lambda i: i[1][0] * 3, reverse=True):
            res.append(key + " : " + str(value[0] * 3))
    return res


class Test(unittest.TestCase):
    def test_half(self):
        my_matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, "spam"], [11, 12, 13, 14, 15], [16, "stam", 18, 19, 20]]
        self.assertEqual(half(my_matrix, 0), [[1, 2, 3, 4, 5], [7, 8, 9, 'spam'], [13, 14, 15], [19, 20]])
        self.assertEqual(half(my_matrix, 1), [[1], [6, 7], [11, 12, 13], [16, 'stam', 18, 19]])

    def test_encrypt(self):
        self.assertEqual(decrypt(), 'solongandthanksforthefish')
        self.assertEqual(decrypt('aaa', 1), 'zzz')
        self.assertEqual(decrypt('tqbn', 1), 'spam')

    def test_merge_sorted_lists(self):
        outputs1 = [0, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 15, 24, 35, 40]
        outputs2 = [0, 1, 2, 3, 4, 10, 12, 14, 16, 18]
        outputs3 = [0, 1, 3, 5, 12, 22, 33, 43]
        for output in merge_sorted_lists(range(0, 10, 1), [1, 15, 24, 35, 40]):  # first test
            self.assertEqual(output, outputs1.pop(0))
        for output in merge_sorted_lists(range(10, 20, 2), range(0, 5, 1)):  # second test
            self.assertEqual(output, outputs2.pop(0))
        for output in merge_sorted_lists([0], [1, 3, 5, 12, 22, 33, 43]):  # third test
            self.assertEqual(output, outputs3.pop(0))

    def test_rank(self):
        self.assertEqual(rank('winners.txt', 'total'), ['USA : 2521', 'Great-Britain : 847', 'Israel : 9'])
        self.assertEqual(rank('winners.txt', 'weighted'), ['USA : 5359', 'Great-Britain : 1668', 'Israel : 12'])
        self.assertEqual(rank('winners.txt', 'gold'), ['USA : 3066', 'Great-Britain : 789', 'Israel : 3'])


if __name__ == '__main__':
    unittest.main()
