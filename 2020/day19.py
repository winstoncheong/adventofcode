from os import replace
from pprint import pprint

# f = open('day19in.txt')
f = open('testin.txt')
lines = [line.strip() for line in f.readlines()]

part = 0

# num => [patterns]
# num => [ [token, token], [..], ..]
rules = {}
test_strings = []

i = lines.index('')

for line in lines[0:i]:
    k, v = line.split(':')
    patterns = [p.strip() for p in v.split('|')]
    pattern_toks = [p.split(' ') for p in patterns]
    rules[k] = pattern_toks

test_strings = lines[i+1:]

def simplify_rules(rules):
    """Simplify the rules. Only the things that don't branch."""

    singletons = {k:v[0] for k,v in rules.items() if len(v)==1}
    print(singletons)

    # terminals = [k for k,v in rules.items() if '"' in v]
    # singletons = [k for k,v in rules.items() if len(v.split('|')) == 1 and k not in terminals]

    # print(singletons)
    # print(terminals)

    # If a singleton shows up in a rule, it can be replaced by its correspondents

    for token in singletons.keys():
        for rule, patterns in rules.items():
            for pattern in patterns:
                if token in pattern:
                    # Try the replacement
                    # rule => [pattern: [token, token], pattern, ...]

                    # print(f'In rule {rule}=>{patterns}')
                    # print(f'Simplification: {token} => {singletons[token]}')
                    # print(f'Old pattern: {pattern}')
                    pattern_str = " ".join(pattern)
                    singleton_str = " ".join(singletons[token])
                    replacement = pattern_str.replace(token, singleton_str)
                    # print(f'Pattern: {pattern_str}, Singleton: {singleton_str}, Replacement: {replacement}')
                    new_pattern = replacement.split(' ')
                    # print(f'New pattern: {new_pattern}')

                    # print(f'First rule: {rule}=>{rules[rule]}')
                    patterns.remove(pattern)
                    patterns.append(new_pattern)
                    # print(f'Modified rule: {rule}=>{rules[rule]}')

    # Can simplify the rules themselves...

    # Can replace terminals in strings... but that might make matching logic harder

#pprint(rules)

# simplify_rules(rules)

# pprint(rules)

def naive_expand_rule(rules, start):
    """ Just simplify everything in one go.
    Given a start, return a list of patterns that match.

    rules: "start" : patterns
    where patterns = [ pattern.. ]
    and each pattern = [tokens]
    """

    expanded = []
    patterns = rules[start] 

    for pattern in patterns:
        # pattern: [token, token, ...]
        new_pattern = []

        for token in pattern:
            if '"' in token:
                new_pattern.append(token)
            else:
                # recursively call naive_simplify
                replacement = naive_expand_rule(rules, token)
                if len(replacement) == 1: # the pattern matching 'token' doesn't branch
                    replacement = replacement[0]
                new_pattern.append(replacement)

        expanded.append(new_pattern) 

    return expanded


match0 = naive_expand_rule(rules,'0')
print(match0)



# Argh
def condense(rules, start):
    patterns = rules[start] # list of patterns that code to the start

    for pattern in patterns:
        pattern_str = " ".join(pattern)
        for token in pattern:
            if '"' not in token: # token can be replaced
                pass


# TODO this won't work...
def check_match(msg, matcher):
    """Matcher is the incredibly nested structure"""

    # Base case. Matcher only has one branch
    if len(matcher)==1:
        if type(matcher[0]) is str:
            return msg == matcher[0]
        else: #matcher does not branch, but there are subcomponents in the match expression
            return check_match(msg, matcher[0])

    # Matcher has multiple branches. Need to line up msg with matcher parts
    for branch in matcher:
        if check_match(msg, branch):
            return True
    return False

    # try all splittings possible?
    for i in range(1,len(msg)):
        print(f'Split into {msg[0:i]} and {msg[i:]}')
        if check_match(msg[0:i], matcher[0]) and check_match(msg[i:], matcher[1:]):
            return True
        
    else:
        return False


#check_match('ababbb', match0)
check_match('a', [['a'],['b']])