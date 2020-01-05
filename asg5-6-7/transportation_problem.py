class TransportationProblem:

    def __init__(self, producers, costumers):
        self._producers = producers
        self._costumers = costumers
        self._cost = [[0] * costumers for _ in range(producers)]
        self._capacity = [0] * producers
        self._demand = [0] * costumers
        self._solution = [[0] * costumers for _ in range(producers)]

    def add_cost(self, producer, costumer, cost):
        self._cost[producer][costumer] = cost

    def add_capacity(self, producer, capacity):
        self._capacity[producer] = capacity

    def add_demand(self, costumer, demand):
        self._demand[costumer] = demand

    def solve(self):
        while True:
            producer, costumer = self._get()
            if producer == costumer == -1:
                break
            if self._demand[costumer] <= self._capacity[producer]:
                self._solution[producer][costumer] = self._demand[costumer]
                self._capacity[producer] -= self._demand[costumer]
                self._demand[costumer] = 0
                for p in range(self._producers):
                    self._cost[p][costumer] = -1
            else:
                self._solution[producer][costumer] = self._capacity[producer]
                self._demand[costumer] -= self._capacity[producer]
                self._capacity[producer] = 0
                for c in range(self._costumers):
                    self._cost[producer][c] = -1

    def _get(self):
        producer = costumer = -1
        for p in range(self._producers):
            for c in range(self._costumers):
                if self._cost[p][c] == -1:
                    continue
                if producer == costumer == -1 or self._cost[p][c] < self._cost[producer][costumer]:
                    producer, costumer = p, c
                elif self._cost[p][c] == self._cost[producer][costumer] and self._demand[costumer] < self._demand[c]:
                    producer, costumer = p, c
        return producer, costumer

    def print_data(self):
        print('Data Table:')
        print('P\\C     ', end='')
        for c in range(self._costumers):
            print('C%-7d' % c, end='')
        print('Capacity')
        for p in range(self._producers):
            print('P%-7d' % p, end='')
            for c in range(self._costumers):
                print('%-8d' % self._cost[p][c], end='')
            print('%-8d' % self._capacity[p])
        print('Demand  ', end='')
        for c in range(self._costumers):
            print('%-8d' % self._demand[c], end='')
        print()

    def print_solution(self):
        print('Solution:')
        print('P\\C     ', end='')
        for c in range(self._costumers):
            print('C%-7d' % c, end='')
        print()
        for p in range(self._producers):
            print('P%-7d' % p, end='')
            for c in range(self._costumers):
                print('%-8d' % self._solution[p][c], end='')
            print()


def main():
    print('.: Transportation Problem :.')
    tp = TransportationProblem(3, 4)
    tp.add_cost(0, 0, 4)
    tp.add_cost(0, 1, 6)
    tp.add_cost(0, 2, 8)
    tp.add_cost(0, 3, 8)
    tp.add_cost(1, 0, 6)
    tp.add_cost(1, 1, 8)
    tp.add_cost(1, 2, 6)
    tp.add_cost(1, 3, 7)
    tp.add_cost(2, 0, 5)
    tp.add_cost(2, 1, 7)
    tp.add_cost(2, 2, 6)
    tp.add_cost(2, 3, 8)
    tp.add_capacity(0, 40)
    tp.add_capacity(1, 60)
    tp.add_capacity(2, 50)
    tp.add_demand(0, 20)
    tp.add_demand(1, 30)
    tp.add_demand(2, 50)
    tp.add_demand(3, 50)
    tp.print_data()
    tp.solve()
    tp.print_solution()


if __name__ == '__main__':
    main()
