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
    list_of_words=getWords(filename)
    temp_set = set()
    for word in list_of_words:
        temp_set.add(word.lower())
    return len(temp_set)

def getWords(filename):
    url_file=urllib2.urlopen(codeskulptor.file2url(filename))
    list_of_words=[]
    for line in url_file.readlines():
        for word in re.findall(r"\b[\S']+\b",line):
            list_of_words.append(word)
    return list_of_words

def median_word(filename):
    list_of_words=[]
    for word in getWords(filename):
        print(word)
        list_of_words.append(word.lower())
    dict={}
    for word in list_of_words:
        if word in dict:
            dict[word]+=1
        else:
            dict[word]=1
    value_list=[]
    for key in dict:
        value_list.append((key,dict[key]))
    value_list.sort(key=lambda x: x[1])
    return value_list[len(value_list)/2][0]
def wordseq_successor_counts(filename_list, seq_size, include_punc, is_case_sensitive):
    list_of_lists=[]
    for file in filename_list:
        url_file=urllib2.urlopen(codeskulptor.file2url(file))
        list_of_words=[]
        for line in url_file.readlines():
            print(line)
            if(include_punc):
                for word in re.findall(r"\b[\S']+\b|[!,.:;?][^.]",line):
                    list_of_words.append(word)
            else:
                for word in re.findall(r"\b[\S']+(?:\b|')",line):
                    print(word)
                    list_of_words.append(word)
        if(is_case_sensitive):
            temp_list=[]
            for word in list_of_words:
                temp_list.append(word.lower())
            list_of_words=temp_list
        list_of_lists.append(list_of_words)


print(wordseq_successor_counts(['comp130_AmericanPie.txt'], 1, False, False))
def wordseq_successor_frequencies(filename_list, seq_size, include_punc, is_case_sensitive):
    pass


