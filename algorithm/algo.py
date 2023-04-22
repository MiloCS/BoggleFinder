import networkx as nx

def load_word_table(path, length_needed):
    table = set()
    with open(path, "r+") as f:
        for line in f:
            val = line.strip()
            if len(val) >= length_needed:
                table.add(line.strip())
    return table

def build_grid(grid_string, dimension):
    return [grid_string[i:i+dimension] for i in range(0, len(grid_string), dimension)]

def pretty_print_grid(grid):
    for l in grid:
        for v in l:
            print(v, end=' ')
        print()

def build_neighbors_list(letter_string, dimension):
    pass

def build_graph(letter_string):
    G = nx.Graph()
    nodes = [(i, {"l": x}) for i, x in enumerate(letter_string)]
    G.add_nodes_from(nodes)

    
if __name__ == '__main__':
    letter_string = "abcdefghi"
    word_table = load_word_table("../data/1000_common_words.txt", 3)
    grid = build_grid(letter_string, 3)
    pretty_print_grid(grid)

