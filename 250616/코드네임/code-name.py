MAX_N = 5

codenames = []
scores = []
for _ in range(MAX_N):
    codename, score = input().split()
    codenames.append(codename)
    scores.append(int(score))

# Please write your code here.

class Agent:
    def __init__(self, codename, score) :
        self.codename = codename
        self.score = score

agents = []
for i in range(MAX_N) :
    agents.append(Agent(codenames[i], scores[i]))

min_idx = 0
for i in range(1, MAX_N) :
    if agents[i].score < agents[min_idx].score :
        min_idx = i

print(agents[min_idx].codename, agents[min_idx].score)