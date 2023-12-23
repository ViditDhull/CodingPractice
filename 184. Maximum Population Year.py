class Solution(object):
    def maximumPopulation(self, logs):
        pop = {}
        for i in range(len(logs)):
            for j in range(logs[i][0], logs[i][1]):
                if j not in pop:
                    pop[j] = 1
                else:
                    pop[j] += 1
        max_pop = max(pop.values())
        max_years = []
        for i in pop.keys():
            if pop[i] == max_pop:
                max_years.append(i)
        return min(max_years)