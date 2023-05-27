import sys
import re
from itertools import combinations

import libmambapy

allowed_flags = [
    'SOLVER_JOBMASK',
    'SOLVER_SOLVABLE_PROVIDES',
    'SOLVER_INSTALL',
    'SOLVER_LOCK',
    'SOLVER_SOLVABLE_ONE_OF',
    'SOLVER_UPDATE',
    'SOLVER_ERASE',
    'SOLVER_FAVOR',
]
flag_mapping = {getattr(libmambapy, _): _ for _ in allowed_flags if _.startswith('SOLVER_')}

runs = []

run = {
    'matchspec': {},
}

for line in sys.stdin:
    if line.startswith('>>> '):
        match = re.search(">>> matchspec2id: '(.*)' (-?\d+)", line[:-1])
        if match:
            matchspec, value = match.groups()
            run['matchspec'][int(value)] = matchspec
        elif line.startswith('>>> M_JOBS:'):
            run['M_JOBS'] = [int(_) for _ in line[11:].split()]
            runs.append(run)
            run = {
                'matchspec': {},
            }
        elif line.startswith('>>> M_FLAGS:'):
            run['M_FLAGS'] = [int(_) for _ in line[12:].split()]


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


print(runs)


for run in runs:
    print('>>>> SOLVE ATTEMPT <<<<')
    for flag, matchspec_id in chunks(run['M_JOBS'], 2):
        solutions = [comb for i in range(1, 5) for comb in combinations(flag_mapping.keys(), i) if sum(comb) == flag]
        _solutions = []
        for solution in solutions:
            _solutions.append([flag_mapping[_] for _ in solution])
        print(_solutions, matchspec_id, run['matchspec'][matchspec_id])
    print('\n\n')
