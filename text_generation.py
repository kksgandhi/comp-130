import re
import random


def stop_generating_sentence(strings):
    if len(strings) < 1:
        return False
    if re.match(r"(?:\.|!+|\?+)", strings[-1]):
        return True
    return False


def pick_successor_random(successor_dict):
    rand_num = random.random()
    for key in successor_dict:
        if(successor_dict[key] > rand_num):
            return key
        rand_num -= successor_dict[key]


def form_utterance_nice(strings):
    if(len(strings) < 1):
        return ""
    string_list = []
    # Prevent mutation
    for word in strings:
        string_list.append(word)
    if(not stop_generating_sentence(string_list)):
        string_list.append(".")
    string_list[0] = string_list[0][0].upper() + string_list[0][1:]
    for i in range(0, len(string_list) - 1):
        if(re.match(r"(?:\.+|!+|\?+)", string_list[i])):
            string_list[i + 1] = string_list[
                i + 1][0].upper() + string_list[i + 1][1:]
    return " ".join(string_list)


def generate_text(chain, pick_starting_key, stop_generating, form_utterance):
    pass


def neural_net(input_node_set, num_hidden_nodes, output_node_set):
    pass

print(form_utterance_nice(["Hello", "my", ".", "baby"]))
