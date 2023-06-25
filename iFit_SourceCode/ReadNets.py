# -*- coding: UTF-8 -*-
'''
@Project ：iFit
@File    ：ReadNets.py
@IDE     ：PyCharm 
@Author  ：Du Xin
@Date    ：2021-10-25 13:55
@Abstract: Operating network
'''
import networkx as nx
from networkx.readwrite import read_pajek
from matplotlib import pyplot as plt

plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['SimHei']
import os


class graphAttribute:
    def __init__(self, GraphPath):
        self.GraphPath = GraphPath
        # 读取网络，并创建
        self.graph = read_pajek(self.GraphPath)

    def Graph2DirWeight(self):
        '''
        加权有向图
        :return:
        '''
        DirWeightG = nx.DiGraph()
        nodes = self.graph.nodes()  # 节点集合
        edges = self.graph.edges()  # 边集合
        GraphAttribute = []  # [(node1,node2,{'weight':value}),...]
        for node in nodes:
            DirWeightG.add_node(node)
        for edge in edges:
            self.graph.get_edge_data(edge[0], edge[1])[0]['weight'] = int(self.graph.get_edge_data(edge[0], edge[1])[0]['weight'])
            GraphAttribute.append(tuple((edge[0], edge[1], self.graph.get_edge_data(edge[0], edge[1])[0])))
        DirWeightG.add_edges_from(GraphAttribute)
        return DirWeightG

    def GraphUndirUnWeight(self):
        '''
        无权无向图
        :return:
        '''
        UndirWeightG = nx.Graph()
        nodes = self.graph.nodes()  # 节点集合
        edges = self.graph.edges()  # 边集合
        GraphAttribute = []  # [(node1,node2,{'weight':value}),...]
        for node in nodes:
            UndirWeightG.add_node(node)
        for edge in edges:
            GraphAttribute.append(tuple((edge[0], edge[1], {'weight':1})))
        UndirWeightG.add_edges_from(GraphAttribute)
        return UndirWeightG

    def GraphUndirWeight(self):
        '''
        生成加权有向图
        :return:
        '''
        self.DirWeightG = self.Graph2DirWeight()
        graph = self.DirWeightG
        edges = self.update_weight(graph).edges()
        # edges = graph.edges()
        remove_edges = []
        for edge in edges:
            if edge[0] == edge[1]:
                remove_edges.append(edge)
        for edge in remove_edges:
            graph.remove_edge(edge[0], edge[0])
        un_graph = self.DirWeight2UndirWeight(graph)
        return un_graph

    def DirWeight2UndirWeight(self, graph):
        '''
        由加权有向图->加权无向图
        :return:
        '''
        un_graph = nx.Graph()
        nodes = self.DirWeightG.nodes
        for node in nodes:
            un_graph.add_node(node)
        edges = graph.edges
        for edge in edges:
            _weight = graph.get_edge_data(edge[0], edge[1])['weight']
            if un_graph.has_edge(edge[0], edge[1]):
                _old_weight = un_graph.get_edge_data(edge[0], edge[1])['weight']
                _old_weight = _old_weight + _weight
                un_graph.add_edge(edge[0], edge[1], weight=_old_weight)
            else:
                un_graph.add_edge(edge[0], edge[1], weight=_weight)
        return un_graph

    def update_weight(self, graph):
        """
        将边权规格化
        :param graph:
        :return:
        """
        edges = graph.edges()
        weight_set = set()
        for edge in edges:
            weight = graph.get_edge_data(edge[0], edge[1])['weight']
            weight_set.add(weight)
        max_weight = max(weight_set)

        for edge in edges:
            weight = graph.get_edge_data(edge[0], edge[1])['weight']
            graph.add_edge(edge[0], edge[1], weight=weight / max_weight)
        return graph
