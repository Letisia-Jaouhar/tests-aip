def task_1(two_dim_words):
    sorted_words = []
    for d in two_dim_words:
       sorted_words.extend(d)
    print(sorted_words)
    sorted_words.sort()
    sorted_words(key=len, reverse = True)
    print(sorted_words)
 

    return sorted_words



def task_4_1(words):
    words1 = str(words).lower()
    words2 = words1.split(', ')
    res = tuple([i.count('a') ** 2 for i in words2 if i.count('a') >= 2])

    return res


def task_4_2(words):  # можно сделать тесты
    res = {len(i) for i in words if len(i) > 3}

    return res


def task_4_3(words):
    letter = "eyuioa"
    func = str(words).lower()
    for i in func:
        if i.endswith('a') is True:
            for chr in func:
                if chr in letter:
                    func = func.replace(chr,'')
                    res = func

    return res


def task_5(lst1, lst2):
    lst1.difference_update(n2)
    print(list(lst1))

    return lst1


def task_6(lst):
    lst = list(input())
    a = set(lst)
    res = tuple(sorted(a))
    print(res)

    return res

