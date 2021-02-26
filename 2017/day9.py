f = open('day9input.txt')
line = f.readline().strip()

garbage_count = 0
def remove_garbage(stream):
    global garbage_count
    garbage_count = 0
    
    output = []
    state = "normal"
    i=0
    
    while i < len(stream):
        if stream[i] == '<' and state != 'garbage':
            state = 'garbage'
        elif stream[i] == '>':
            state = 'normal'
        elif stream[i] == '!':
            i += 1 # skip next char
        elif state != 'garbage':
            output.append(stream[i])
        elif state == 'garbage':
            garbage_count += 1
        i += 1

    ret = "".join(output)

    # cleanup from trash removal

    # repeatedly replace commas
    changed = ret.replace(",,", ',')
    while changed != ret:
        ret, changed = changed, changed.replace(",,", ',')

    ret= ret.replace("{,}", "{}")
    
    return ret

def list_subgroups(group):
    """subgroups contained in this group. Depth 1"""
    
    substr = group[1:-1]
    # print(f'substr: {substr}')

    subgroups = []

    idx = 0
    depth = 0
    group = [] 
    while idx < len(substr):
        if substr[idx] == '{':
            depth += 1
            group.append(substr[idx])
        elif substr[idx] == '}':
            depth -= 1
            group.append(substr[idx])
        elif substr[idx] == ',' and depth == 0: # group ends
            subgroups.append("".join(group))
            # print('Found end of group')
            group = []
        else:
            group.append(substr[idx])
        idx += 1
        
    subgroups.append("".join(group)) # cleanup
    
    # print(subgroups)

    return subgroups

def get_groups(stream):
    """ returns list of all groups (including itself) """
    
    # Assumes what's given is a stream
    assert stream[0] == '{' and stream[-1] == '}'

    if stream == "{}":
        return [stream]

    output = []
    subgroups = list_subgroups(stream)
    
    for subgroup in subgroups:
        output.extend(get_groups(subgroup)) 

    output.append(stream) # add itself

    return output

def score(group):
    """Assumes garbage was removed"""

    ans = 0
    depth = 0
    for c in group:
        if c == '{':
            depth += 1
            ans += depth
        elif c == '}':
            depth -= 1

    return ans
   
assert remove_garbage("<>") == ''
assert remove_garbage("<random characters>") == ''
assert remove_garbage("<<<>") == ''
assert remove_garbage("<{!>}>") == ''
assert remove_garbage("<!!>") == ''
assert remove_garbage("<!!!>>") == ''
assert remove_garbage('<{o"i!a,<{i<a>') == ''

assert len(get_groups("{{{}}}")) == 3
assert len(get_groups("{{},{}}")) == 3
assert len(get_groups("{{{},{},{{}}}}")) == 6
assert len(get_groups(remove_garbage("{<{},{},{{}}>}"))) == 1
assert len(get_groups(remove_garbage("{<a>,<a>,<a>,<a>}"))) == 1
assert len(get_groups(remove_garbage("{{<a>},{<a>},{<a>},{<a>}}"))) == 5
assert len(get_groups(remove_garbage("{{<!>},{<!>},{<!>},{<a>}}"))) == 2

assert score("{}") == 1
assert score("{{{}}}") == 6
assert score("{{},{}}") == 5
assert score("{{{},{},{{}}}}") == 16
assert score(remove_garbage("{<a>,<a>,<a>,<a>}")) == 1
assert score(remove_garbage("{{<ab>},{<ab>},{<ab>},{<ab>}}")) == 9
assert score(remove_garbage("{{<!!>},{<!!>},{<!!>},{<!!>}}")) == 9
assert score(remove_garbage("{{<a!>},{<a!>},{<a!>},{<ab>}}")) == 3

#### part 2 tests

remove_garbage("<>")
assert garbage_count == 0
remove_garbage("<random characters>")
assert garbage_count == 17
remove_garbage("<<<<>")
assert garbage_count == 3
remove_garbage("<{!>}>")
assert garbage_count == 2
remove_garbage("<!!>")
assert garbage_count == 0
remove_garbage("<!!!>>")
assert garbage_count == 0
remove_garbage('<{o"i!a,<{i<a>')
assert garbage_count == 10

print(f'Answer 1: {score(remove_garbage(line))}')
print(f'Answer 2: {garbage_count}')
