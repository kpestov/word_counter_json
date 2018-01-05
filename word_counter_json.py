def find_out_encoding(file):

    import chardet

    with open(file, 'rb') as f:
        data = f.read()
        result = chardet.detect(data)
        encode = result['encoding']

        return encode


def get_list_more_6_characters(file, encode):

    import json

    with open(file, encoding=encode) as f:
        news = json.load(f)
        list_ = news['rss']['channel']['items']
        counter = len(list_)
        raw_list = []
        keys = ['description', 'title']
        for j in keys:
            for i in range(counter):
                element = news['rss']['channel']['items'][i][j]
                b = element.split()
                for k in b:
                    if len(k) > 6:
                        raw_list.append(k)
        return raw_list


def common_words(raw_list):

    from collections import Counter

    raw_dict = Counter(raw_list) #dict {'word':number of times}
    word_list = raw_dict.most_common(10)
    raw_common_list = []
    for i in word_list:
        for j in i:
            raw_common_list.append(j)
    common_list = raw_common_list[::2]
    return common_list


def main():
    file_list = ['newsafr.json', 'newscy.json', 'newsfr.json', 'newsit.json']
    for file in file_list:
        func_1 = find_out_encoding(file)
        func_2 = get_list_more_6_characters(file, func_1)
        func_3 = common_words(func_2)
        print('Топ 10 самых часто встречающихся в новостях слов длиннее 6 символов в файле {0}: {1}'.format(file, ', '.join(func_3)))


main()




