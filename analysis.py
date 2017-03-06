import re
import urllib2
import codeskulptor

def findall_sl(text):
    return re.findall(r"\b[sS]l\S+\b",text)

def findall_triple_vowel(text):
    return re.findall(r"\b\S*(?:aaa+|eee+|iii+|ooo+|uuu+)\S*\b",text,re.IGNORECASE)

def findall_80s(text):
    return re.findall(r"\b(?:eighties|198\d|(?:19|)80s)\b",text,re.IGNORECASE)

def count_distinct_words(filename):
    url_file=urllib2.urlopen(codeskulptor.file2url(filename))
    list_of_words=[]
    for line in url_file.readlines():
        for word in re.findall(r"\b\S+\b",line):
            list_of_words.append(word)
    temp_set = set()
    for word in list_of_words:
        temp_set.add(word.lower())
    return len(temp_set)

def median_word(filename):
    pass

def wordseq_successor_counts(filename_list, seq_size, include_punc, is_case_sensitive):
    pass

def wordseq_successor_frequencies(filename_list, seq_size, include_punc, is_case_sensitive):
    pass
print(findall_triple_vowel("aaaabb hello therre eeeeemo quaaaaaality"))


