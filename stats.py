def get_num_words(contents):
    list_of_words = contents.split()
    return len(list_of_words)

def get_characters(contents):
    dic = {}
    for word in contents.lower():
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1
    return dic

def sorted_dict(dic):
    result = []
    for key, value in dic.items():
        result.append({"char": key, "num": value})
    result.sort(reverse=True, key=sort_on)
    return result

def sort_on(item):
    return item["num"]