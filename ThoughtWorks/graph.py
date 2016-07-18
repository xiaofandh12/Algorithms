#!/usr/bin/env python
#coding=utf-8

'''
    ThoughtWorks Problem One: Trains --> graph.py
'''

class Graph:
    '''
        Read data from data.txt.
        Calculate the distance of the given route.
        Calculate the route between two vertexs of given the stops.
        Calculate the shortest route between two vertexs.
    '''

    def __init__(self, data_file = "data.txt", log_file = "log.txt"):
        self.graph = {} # 使用临接矩阵表示图
        self.data_f = open(data_file, "r")
        self.trip_count = 0
        self.best_cost = 100000

        self.init_graph(self.data_f)

    def init_graph(self, f):
        '''
            Init self.graph.
        '''

        for i in f:
            edges = i.split(",")
            for edge in edges:
                if self.graph.has_key(edge[0]):
                    temp = self.graph[edge[0]]
                else:
                    temp = {}
                temp[edge[1]] = edge[2]
                self.graph[edge[0]] = temp

    def distance_route(self, route):
        '''
            Calculate the distance of the given route.
        '''

        distance = 0
        if (len(route) < 2):
            distance = -1 # route中少于两个点
            return distance

        for i in range(len(route) - 1):
            vertex_cur = route[i]
            vertex_next = route[i + 1]
            if self.graph[vertex_cur].has_key(vertex_next):
                distance += int(self.graph[vertex_cur][vertex_next])
            else:
                distance = -1 # route中包含了无效的边
                return distance
        return distance

    def start_end_max_hops(self, start, end, max_hops):
        '''
            Calculate the routes between start and end within max_hops.
        '''

        def dfs(route, end, max_hops):
            if (len(route) > max_hops):
                return

            if ((len(route) > 1) and (route[len(route) - 1] == end)):
                tmp_route = route[:]
                self.trip_count = self.trip_count + 1

            last_vertex = route[len(route) - 1]
            for vertex in self.graph[last_vertex].keys():
                route.append(vertex)
                dfs(route, end, max_hops)

        init_route = []
        init_route.append(start)
        for vertex in self.graph[start].keys():
            tmp_route = init_route[:]
            tmp_route.append(vertex)
            dfs(tmp_route, end, max_hops + 1)

        result = self.trip_count
        self.trip_count = 0
        return result

    def start_end_hops(self, start, end, hops):
        '''
            Calculate the routes between start and end with exactly hops.
        '''

        result = 0
        last_vertexs = []
        last_vertexs.append(start)

        for hop in range(hops):
            vertexs = [] # vertexs为第hop跳可以跳到哪些节点的列表
            for last_vertex in last_vertexs:
                tmp_vertexs = self.graph[last_vertex].keys()
                for vertex in tmp_vertexs:
                    vertexs.append(vertex)
            last_vertexs = vertexs

        result = last_vertexs.count(end)

        return result

    def start_end_shortest_route(self, start, end):
        '''
            Calculate the shortest route between start and end.
        '''

        def dfs(route, end, cost):
            if ((route[len(route) - 1] == end) and (cost < self.best_cost) and (cost > 0)):
                self.best_cost = cost
                return

            last_vertex = route[len(route) - 1]
            for vertex in self.graph[last_vertex].keys():
                newCost = int(self.graph[last_vertex][vertex])
                if (route.count(vertex) and route.index(vertex) > 0):
                    continue
                route.append(vertex)
                dfs(route, end, cost + newCost)

        init_route = []
        init_route.append(start)
        cost = 0
        dfs(init_route, end, cost)

        result = self.best_cost
        self.best_cost = 100000
        return result

    def start_end_max_cost(self, start, end, max_cost):
        '''
            Calculate the routes between start and end within max_cost.
        '''

        def dfs(route, end, cost):
            if (cost >= max_cost):
                return

            if ((route[len(route) - 1] == end) and (cost > 0)):
                self.trip_count = self.trip_count + 1

            last_vertex = route[len(route) - 1]
            for vertex in self.graph[last_vertex].keys():
                newCost = int(self.graph[last_vertex][vertex])
                route.append(vertex)
                dfs(route, end, cost + newCost)

        init_route = []
        init_route.append(start)
        cost = 0
        dfs(init_route, end, cost)

        result = self.trip_count
        self.trip_count = 0
        return result
