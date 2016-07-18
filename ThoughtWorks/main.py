#!/usr/bin/env python
#coding=utf-8

'''
    ThoughtWorks Problem One: Trains --> main.py
'''

from graph import Graph

'''
    Expect output:
    Output #1: 9
    Output #2: 5
    Output #3: 13
    Output #4: 22
    Output #5: NO SUCH ROUTE
    Output #6: 2
    Output #7: 3
    Output #8: 9
    Output #9: 9
    Output #10: 7
'''

if __name__ == "__main__":
    log_f = open("log.txt", "w")
    output = "Output #%d:%d"
    output_s = "Output #%d:%s"
    routes = [["A","B","C"],["A","D"],["A","D","C"],["A","E","B","C","D"],["A","E","D"]]
    for i in range(10):
        result = 0
        try:
            graph = Graph()
        except Exception, e:
            log_f.write("Init graph\n")
            log_f.write("Exception occurred:%s\n" % e)

        if i in range(5):
            try:
                result = graph.distance_route(routes[i])
            except Exception, e:
                log_f.write("graph.distance_route()\n")
                log_f.write("Exception occurred:%s\n" % e)
                pass

            if result != -1:
                print output % (i+1, result)
            else:
                print output_s % (i+1, "NO SUCH ROUTE")

        elif (i == 5):
            try:
                result = graph.start_end_max_hops("C", "C", 3)
            except Exception, e:
                log_f.write("graph.start_end_max_hops()\n")
                log_f.write("Exception occurred:%s\n" % e)
                pass

            print output % (i+1, result)

        elif (i == 6):
            try:
                result = graph.start_end_hops("A", "C", 4)
            except Exception, e:
                log_f.write("graph.start_end_hops()\n")
                log_f.write("Exception occurred:%s\n" % e)
                pass

            print output % (i+1, result)

        elif (i == 7):
            try:
                result = graph.start_end_shortest_route("A", "C")
            except Exception, e:
                log_f.write("graph.start_end_shortest_route()\n")
                log_f.write("Exception occurred:%s\n" % e)
                pass

            print output % (i+1, result)

        elif (i == 8):
            try:
                result = graph.start_end_shortest_route("B", "B")
            except Exception, e:
                log_f.write("graph.start_end_shortest_route()\n")
                log_f.write("Exception occurred:%s\n" % e)
                pass

            print output % (i+1, result)

        elif (i == 9):
            try:
                result = graph.start_end_max_cost("C", "C", 30)
            except Exception, e:
                log_f.write("graph.start_end_max_cost()\n")
                log_f.write("Exception occurred:%s\n" % e)
                pass

            print output % (i+1, result)
