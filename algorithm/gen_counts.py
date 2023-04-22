from algo import load_word_table
import time
import json
import sys

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def build_pcts(word_set):
    count_dict = add_entry('', word_set, {})
    return count_dict

def add_entry(incoming, word_set, count_dict):
    if incoming:
        count = len(list(filter(lambda x: x.startswith(incoming), word_set)))
        if count:
            count_dict[incoming] = count
        else:
            return count_dict
    for letter in alphabet:
        add_entry(incoming+letter, word_set, count_dict)
    return count_dict

if __name__ == "__main__":
    min_length = int(sys.argv[1])
    word_list_size = sys.argv[2]
    word_lists = {
        '1000': './data/1000_common_words.txt'
    }
    word_set = load_word_table(word_lists[word_list_size], min_length)
    start = time.time()
    count_dict = build_pcts(word_set)
    end = time.time()
    print("Length of Alphabet: ", len(alphabet))
    print("Time: ", end-start)
    print("Length of Output Dict: ", len(count_dict))
    # maxstr = max(count_dict, key=count_dict.get)
    # print("Highest Counts: ", gen_maxes(count_dict))
    # print(count_dict)

    count_json = json.dumps(count_dict)
    with open(f"./count_dicts/count_dict_{word_list_size}_{min_length}", 'w') as f:
        f.write(count_json)