def is_chomsky1(rules) -> bool:
    for l, r in rules:
        if l.islower(): return False  # at least one V_N
        for i in r:
            if len(l) <= len(i): continue  # length of left <= length of right
            else: return False
    return True


def is_chomsky2(rules) -> bool:
    for l, r in rules:
        if not l.isupper(): return False  # A->anything
    return True


def is_chomsky3(rules) -> bool:
    for l, r in rules:  # l: left part   r: right parts.
        if len(l) > 1 or len(r) == 1 and l.islower(): return False
        for i in r:
            if len(i) == 1 and not i.isupper(): continue  # A->a
            elif len(i) == 2 and not i[0].isupper() and i[1].isupper(): continue  # A->aB
            elif len(i) == 2 and i[0].isupper() and not i[1].isupper(): continue  # A->Ab
            else: return False
    return True


def judge(rules, flag=0):
    if is_chomsky3(rules): flag = 3
    elif is_chomsky2(rules): flag = 2
    elif is_chomsky1(rules): flag = 1
    return flag


def document():
    print('\n======== Chomsky Hierarchy Classifier ========')
    print('➤ Author: AaronComo')
    print('➤ NOTE: Don\'t press space in the input stream!')
    print('➤ Input format: ')
    print('  grammar: G[N]\n  VN: N,D\n  rule1: N::=ND|D\n  rule2: D::=0|1|2|3')
    print('==============================================\n')


if __name__ == '__main__':
    document()
    S = input('grammar: ')
    S = S.split('[')[1].split(']')[0]
    print()

    Vn = input('VN: ')
    Vn = set(Vn.split(','))
    print()

    print('Use \'end\' to stop.')
    _rules = list()
    i = 0
    while (True):
        print('rule{}: '.format(i + 1), end='')
        a = input()
        if a == 'end': break
        _rules.append(a)
        i = i + 1

    # split symbols
    Vt = set()
    rules = list()
    for ru in _rules:
        l, r = ru.split('::=')  # l: left part.
        r = r.split('|')  # r: right parts.
        rules.append((l, r))
        for i in r:
            if not i.isupper():  # check whether right part has Vt
                for j in i:
                    if (j.islower() or j.isdigit()) and j not in Vt: Vt.add(j)

    print('\n--------- Result ----------')
    print('G[{}]:\t({}, {}, P, {})'.format(S, Vn, Vt, S))
    print('P:', end='')
    for r in rules:
        print('\t{} ::= {}'.format(r[0], '|'.join(r[1])))
    print('\nGiven grammar is a Chomsky-{} grammar.'.format(judge(rules)))
    print('---------------------------')
    
