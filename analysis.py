import re
import urllib2
import codeskulptor
from collections import defaultdict
from collections import Counter


def findall_sl(text):
    return re.findall(r"\b[sS]l\S+\b", text)


def findall_triple_vowel(text):
    return re.findall(r"\b\S*(?:aaa+|eee+|iii+|ooo+|uuu+)\S*\b", text, re.IGNORECASE)


def findall_80s(text):
    return re.findall(r"\b(?:eighties|198\d|(?:19|)80s)\b", text, re.IGNORECASE)


def count_distinct_words(filename):
    list_of_words = getWords(filename, False, False)
    temp_set = set()
    for word in list_of_words:
        temp_set.add(word.lower())
    return len(temp_set)


def getWords(filename, include_punc, case_sensitive):
    url_file = urllib2.urlopen(codeskulptor.file2url(filename))
    list_of_words = []
    for line in url_file.readlines():
        for word in re.findall(r"[?!]+|-+|\.+|[,:;\"'`()/&#]|-?[A-Za-z0-9]+(?:['\-.@/][A-Za-z0-9]+)*|-?\$?\d{1,3}(?:,?\d{3})*(?:\.\d+)?", line):
            if(case_sensitive):
                list_of_words.append(word)
            else:
                list_of_words.append(word.lower())
    if(not include_punc):
        temp_list = []
        for word in list_of_words:
            if re.match("[a-zA-Z]", word):
                temp_list.append(word)
        return temp_list
    return list_of_words


def median_word(filename):
    list_of_words = []
    for word in getWords(filename, False, False):
        print(word)
        list_of_words.append(word.lower())
    dict = {}
    for word in list_of_words:
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1
    value_list = []
    for key in dict:
        value_list.append((key, dict[key]))
    value_list.sort(key=lambda x: x[1])
    return value_list[len(value_list) / 2][0]


def wordseq_successor_counts(
    filename_list,
     seq_size,
     include_punc,
     is_case_sensitive):
    list_of_word_lists = []
    return_dict = defaultdict(Counter)
    for file in filename_list:
        list_of_word_lists.append(
            getWords(file, include_punc, is_case_sensitive))
    for word_list in list_of_word_lists:
        for index in range(0, len(word_list) - seq_size):
            temp_list = []
            for second_index in range(0, seq_size):
                temp_list.append(word_list[index + second_index])
            return_dict[tuple(temp_list)][word_list[index + seq_size]] += 1
    return return_dict


print(wordseq_successor_counts(['comp130_AmericanPie.txt'], 1, False, False))


def wordseq_successor_frequencies(
    filename_list,
     seq_size,
     include_punc,
     is_case_sensitive):

