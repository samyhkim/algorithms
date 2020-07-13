'''
if point A cannot reach point B,
    gap will measure the gas needed to travel from point A to point B
start == len(gas) means we ran off the gas array
https://leetcode.com/problems/gas-station/discuss/167542/10-lines-Python-that-beats-100-NO-PROOF-IN-HERE
'''


def can_complete_circuit(gas, cost):
    tank = gap = start = 0
    for i in range(len(gas)):
        tank += gas[i]
        if tank >= cost[i]:
            tank -= cost[i]
        else:
            gap += cost[i] - tank
            start = i + 1
            tank = 0
    if start == len(gas) or tank < gap:
        return - 1
    return start
