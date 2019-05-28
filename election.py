def main():
    testCases = int(input())
    results = []
    for tc in range(testCases):
        stateandphazeInput = input()
        phasesText = input()
        phases = [getNum(x) for x in phasesText.strip().split(' ')]
        sucphasees = sum(1 for i in phases if i > 0)
        maxphases = max(phases)
        phasesseats = sum(phases)
        
        statesText = input()
        states = [getNum(x) for x in statesText.strip().split(' ')]
        sucstates = sum(1 for i in states if i > 0)
        maxstates = max(states)
        statesseats = sum(states)

        if phasesseats == statesseats and sucphasees >= maxstates and sucstates >= maxphases:
            results.append('YES')
        else:
            results.append('NO')

    for r in results:
        print(r)


def getNum(elem):
    return int(elem)

main()
