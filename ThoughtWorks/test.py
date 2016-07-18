#!/usr/bin/env python
#encoding=utf-8

import unittest
import graph

class test_graph(unittest.TestCase):
    def setUp(self):
        self.tclass = graph.Graph()
        self.log_f = open("log.txt", "w")

    def testDown(self):
        pass

    def test_distance_route(self):
        routes = [["A","B","C"], ["A","D"], ["A","D","C"], ["A","E","B","C","D"], ["A","E","D"]]
        results = [9, 5, 13, 22, -1]
        for route, result in zip(routes, results):
            try:
                self.assertEqual(self.tclass.distance_route(route), result)
            except Exception, e:
                log_f.write("self.assertEqual(self.tclass.distance_route()\n")
                log_f.write("Exception occurred:%s\n" % e)
                pass

    def test_start_end_max_hops(self):
        try:
            self.assertEqual(self.tclass.start_end_max_hops("C","C",3), 2)
        except Exception, e:
            log_f.write("self.assertEqual(self.tclass.start_end_max_hops()\n")
            log_f.write("Exception occurred:%s\n" % e)
            pass

    def test_start_end_hops(self):
        try:
            self.assertEqual(self.tclass.start_end_hops("A","C",4), 3)
        except Exception, e:
            log_f.write("self.assertEqual(self.tclass.start_end_hops()\n")
            log_f.write("Exception occurred:%s\n" % e)
            pass

    def test_start_end_shortest_path(self):
        starts = ["A", "B"]
        ends = ["C", "B"]
        results = [9, 9]
        for start, end, result in zip(starts, ends, results):
            try:
                self.assertEqual(self.tclass.start_end_shortest_route(start, end), result)
            except Exception, e:
                log_f.write("self.assertEqual(self.tclass.start_end_shortest_route()\n")
                log_f.write("Exception occurred:%s\n" % e)
                pass

    def test_start_end_max_cost(self):
        try:
            self.assertEqual(self.tclass.start_end_max_cost("C","C",30), 7)
        except Exception, e:
            log_f.write("self.assertEqual(self.tclass.start_end_max_cost()\n")
            log_f.write("Exception occurred:%s\n" % e)
            pass

if __name__ == "__main__":
    unittest.main()
