import re
import random
# from sets import Set


def pick_key_random(keys):
    """Returns a random one of the given keys."""
    return random.choice(keys)


def pick_key_context(keys):
    """Returns a key on the topic of cars."""
    for key in keys:
        for word in key:
            if word in ["car", "cars", "truck", "trucks", "auto", "autos", "automobile", "automobiles"]:
                # Found a key on the desired topic.
                return key
    # Didn't find any key on the desired topic, so return a random key.
    return random.choice(keys)


def pick_key_first(keys):
    """Returns alphabetically first of the given keys."""
    return sorted(keys)[0]


def stop_generating_sentence(strings):
    if len(strings) < 1:
        return False
    if re.match(r"(?:\.|!+|\?+)", strings[-1]):
        return True
    return False


def stop_generating_20(strings):
    return len(strings) >= 20


def pick_successor_first(successor_dict):
    """Returns alphabetically first successor from the successor dictionary."""
    if dict:
        return sorted(successor_dict.keys())[0]
    else:
        return None


def stop_generating_random(strings):
    probability = 0.1
    return random.random() < probability


def pick_successor_random(successor_dict):
    rand_num = random.random()
    for key in successor_dict:
        if(successor_dict[key] > rand_num):
            return key
        rand_num -= successor_dict[key]


def form_utterance_simple(strings):
    """Returns a single utterance made of the given strings."""
    return " ".join(strings)


def form_utterance_nice(strings):
    if(len(strings) < 1):
        return ""
    string_list = []
    # Prevent mutation
    for word in strings:
        string_list.append(word)
    if(not stop_generating_sentence(string_list)):
        string_list.append(".")
    try:
        string_list[0] = string_list[0][0].upper() + string_list[0][1:]
    except AttributeError:
        pass
    for i in range(0, len(string_list) - 1):
        if(re.match(r"(?:\.+|!+|\?+)", string_list[i])):
            string_list[i + 1] = string_list[
                i + 1][0].upper() + string_list[i + 1][1:]
    return " ".join(string_list)


def neural_net(input_node_set, num_hidden_nodes, output_node_set):
    return_dict = {}
    intersection_set = input_node_set.intersection(output_node_set)
    print(intersection_set)
    if(len(intersection_set) > 0 or len(input_node_set) == 0 or len(output_node_set) == 0 or num_hidden_nodes < 1):
        return None
    temp_list = []
    for word in input_node_set:
        temp_list = []
        for i in range(num_hidden_nodes):
            temp_list.append(i)
        return_dict[word] = set(temp_list)
    for i in range(num_hidden_nodes):
        temp_list = []
        for word in output_node_set:
            temp_list.append(word)
        return_dict[i] = set(temp_list)
    for word in output_node_set:
        return_dict[word] = set([])
    return return_dict
print(
    neural_net(set(['input_one', 'not_disjoint_one']), 10, set(['output_one', 'not_disjoint_one'])))


def generate_text(
    chain,
     pick_starting_key,
     stop_generating,
     pick_successor,
     form_utterance):
    string_list = []
    size_of_seq = len(chain.keys()[0])
    for word in pick_starting_key(chain.keys()):
        string_list.append(word)
    while(not stop_generating(string_list)):
        temp_list = []
        for word in string_list[-size_of_seq:]:
            temp_list.append(word)
        temp_tuple = tuple(temp_list)
        try:
            string_list.append(pick_successor(chain[temp_tuple]))
        except KeyError:
            break
    return form_utterance(string_list)


print(generate_text(
    {('test',
     '.',
      'Here'): {'is': 1.0},
     ('is',
     'another',
      'line'): {'after': 1.0},
     ('after',
     'a',
      'blank'): {'.': 1.0},
     ('a',
     'test',
      '.'): {'Here': 1.0},
     ('.',
     'Here',
      'is'): {'another': 1.0},
     ('This',
     'is',
      'a'): {'test': 1.0},
     ('line',
     'after',
      'a'): {'blank': 1.0},
     ('Here',
     'is',
      'another'): {'line': 1.0},
     ('is',
     'a',
      'test'): {'.': 1.0},
     ('another',
     'line',
      'after'): {'a': 1.0}},
     pick_key_first,
     stop_generating_20,
     pick_successor_first,
     form_utterance_nice))
