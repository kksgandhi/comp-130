"""
This program analyses (spelling is hard) text files.
It has a function to find any word with sl
It has a function that finds words with triple vowel
It has a function that counts distinct words in a file
It has a markhov chain generator, and a frequency generator
"""
import re
import urllib2
import codeskulptor
from collections import defaultdict
from collections import Counter


def findall_sl(text):
    """
    Finds words that begin with sl
    """
    return re.findall(r"\b[sS]l\S+\b", text)


def findall_triple_vowel(text):
    """
    Finds words with triple vowels
    """
    return re.findall(r"\b\S*(?:aaa+|eee+|iii+|ooo+|uuu+)\S*\b", text, re.IGNORECASE)


def findall_80s(text):
    """
    Finds words that reference the eighties
    """
    return re.findall(r"\b(?:eighties|198\d|(?:19|)80s)\b", text, re.IGNORECASE)


def count_distinct_words(filename):
    """
    Counts the number of words in a file
    """
    list_of_words = get_word_list(filename, False, False)
    temp_set = set()
    for word in list_of_words:
        temp_set.add(word.lower())
    return len(temp_set)


def get_word_list(filename, include_punc, case_sensitive):
    """
    Helper function I wrote, returns a list of words out of a file
    Options to include_punctuation or return words case sensitive
    """
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
    """
    Returns the word that is mentioned a median amount of times in a file
    """
    list_of_words = get_word_list(filename, False, False)
    # Yes I know this should be a Counter. Oh well
    temp_dict = {}
    for word in list_of_words:
        if word in temp_dict:
            temp_dict[word] += 1
        else:
            temp_dict[word] = 1
    value_list = []
    for key in temp_dict:
        value_list.append((key, temp_dict[key]))
    value_list.sort(key=lambda x: x[1])
    return value_list[(len(value_list) / 2) - 1][0]


def wordseq_successor_counts(
    filename_list,
     seq_size,
     include_punc,
     is_case_sensitive):
    """
    Creates a markhov chain using a list of files.
    The chain consists of a dictionary mapping tuples to counters
    The counter matches single word strings to
    the amount of times that word has been mentioned after the tuple
    """
    list_of_word_lists = []
    return_dict = defaultdict(Counter)
    for single_file in filename_list:
        list_of_word_lists.append(
            get_word_list(single_file, include_punc, is_case_sensitive))
    for word_list in list_of_word_lists:
        for index in range(0, len(word_list) - seq_size):
            temp_list = []
            for second_index in range(0, seq_size):
                temp_list.append(word_list[index + second_index])
            return_dict[tuple(temp_list)][word_list[index + seq_size]] += 1
    return return_dict


# print(wordseq_successor_counts(['comp130_AmericanPie.txt'], 1, False, False))


def wordseq_successor_frequencies(
    filename_list,
     seq_size,
     include_punc,
     is_case_sensitive):
    """
    calls wordseq_successor_counts and converts the counts into frequencies
    """
    counts_dict = wordseq_successor_counts(
        filename_list,
        seq_size,
     include_punc,
     is_case_sensitive)
    return_dict = defaultdict(dict)
    for key in counts_dict:
        total_count = 0.0
        for inner_key in counts_dict[key]:
            total_count += float(counts_dict[key][inner_key])
        for inner_key in counts_dict[key]:
            return_dict[key][inner_key] = float(
                counts_dict[key][inner_key]) / float(total_count)
    return return_dict
