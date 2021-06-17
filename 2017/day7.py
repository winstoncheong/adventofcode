from collections import Counter

weight = {}
tree_weight = {}
tree = {}

with open('day7input.txt') as f:
    lines = f.readlines()

lines = [line.strip().split(' ') for line in lines]

for line in lines:
    weight[line[0]] = int(line[1][1:-1])

    if len(line) > 2:
        # handle child data, populate tree

        name = line[0]
        # remove trailing comma
        children = [child.rstrip(',') for child in line[3:]]
        tree[name] = children


# print(weight)

def find_parent(name):
    for k, v in tree.items():
        if name in v:
            return k
    else:
        return name


# Answer 1: find root
def find_root(node):
    """returns root node"""
    parent = find_parent(node)
    while (parent != node):
        node, parent = parent, find_parent(parent)

    return node


node = list(tree.keys())[0]
root = find_root(node)

print(f'Answer 1: {root}')


# Part 2

def calc_tree_weight(node):
    """
        returns tree weight of the node
    """
    if node in tree_weight.keys():
        return tree_weight[node]

    if node not in tree:  # node is a leaf
        tree_weight[node] = weight[node]
        return weight[node]

    else:
        # node has children
        children = tree[node]
        weights = []
        for c in children:
            weights.append(calc_tree_weight(c))

        tree_weight[node] = sum(weights) + weight[node]
        return tree_weight[node]


# generate all tree weights
calc_tree_weight(root)


def find_unbalanced(node):
    """Assume the node passed is part of the unbalanced tree.
        Return the node with incorrect weighh, which may be itself.
    """
    #  print(f'Looking at {node}')
    children = tree.get(node, [])

    if len(children) == 0:
        return node

    assert len(children) >= 2

    weights = [tree_weight[c] for c in children]

    # either children are unbalanced, or this node itself is the problem
    counter = Counter(weights)
    # print(counter)

    uniq_weights = [k for k, v in counter.items() if v == 1]
    # print(f'uniqs: {uniq_weights}')

    if len(uniq_weights) == 1:  # one child is unbalanced
        idx = weights.index(uniq_weights[0])
        bad_node = children[idx]
        return find_unbalanced(bad_node)
    elif len(uniq_weights) == 0:  # all children balanced
        return node  # this node itself is the problem.
    else:
        # node has exactly two children, which have different weights
        assert len(children) == 2
        # try both subtrees
        # should not be possible that both return themselves.
        # Would not be able to disambiguate incorrect child
        attempt = find_unbalanced(children[0])
        attempt2 = find_unbalanced(children[1])
        assert attempt != children[0] or attempt2 != children[1]

        if attempt != children[0]:
            return attempt
        else:
            return attempt2


bad_node = find_unbalanced(root)
# print(f'Node with incorrect weight: {bad_node}')

bad_weight = tree_weight[bad_node]
siblings = tree[find_parent(bad_node)]
good_node = siblings[0] if bad_node != siblings[0] else siblings[1]
good_weight = tree_weight[good_node]

# bad_node_weight = bad_weight - sum(children_of_bad)
# correction = good_weight - sum(children_of_bad)
# so

correction = good_weight - bad_weight + weight[bad_node]
print(f'Answer 2: {correction}')
