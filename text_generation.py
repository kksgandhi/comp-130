import re


def stop_generating_sentence(strings):
    if len(strings) < 1:
        return False
    if re.match(r"(?:\.|!+|\?+)", strings[-1]):
        return True
    return False


def pick_successor_random(successor_dict):
    pass


def form_utterance_nice(strings):
    pass


def generate_text(chain, pick_starting_key, stop_generating, form_utterance):
    pass


def neural_net(input_node_set, num_hidden_nodes, output_node_set):
    pass
print(stop_generating_sentence(["Hello", "darkness", "my", "."]))
