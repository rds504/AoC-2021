from tools.general import load_strings

# Part 1
def routes_from(pos, visited=set()):

    if pos == 'end':
        return 1

    if pos.islower() and pos in visited:
        # May not visit a small cave again
        return 0

    return sum(routes_from(nbr, visited.union({pos})) for nbr in links[pos])

# Part 2
def routes_with_revisit_from(pos, visited=set(), revisited=None):

    if pos == 'end':
        return 1

    if pos.islower() and pos in visited:

        if pos == 'start' or revisited is not None:
            # May only revisit one small cave and it may not be start
            return 0

        revisited = pos

    return sum(routes_with_revisit_from(nbr, visited.union({pos}), revisited) for nbr in links[pos])

links = {}
for line in load_strings('day12.txt'):
    i, j = line.split('-')
    if i not in links:
        links[i] = []
    if j not in links:
        links[j] = []
    links[i].append(j)
    links[j].append(i)

print(f'Part 1 => {routes_from("start")}')
print(f'Part 2 => {routes_with_revisit_from("start")}')