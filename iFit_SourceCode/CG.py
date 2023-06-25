# -*- coding: UTF-8 -*-
'''
@Project ：iFit
@File    ：CG.py
@IDE     ：PyCharm 
@Author  ：Du Xin
@Date    ：2021-10-25 15:09
@Abstract: CG Metric
'''
import pandas as pd
import numpy as np
divide_num = np.finfo(float)
from ReadNets import graphAttribute
import networkx as nx
import math
import os
from matplotlib import pyplot as plt
pd.set_option('display.precision', 200)

class CG:
    def __init__(self, _NetPath,_PrideDF,METRIC):
        self.metric = METRIC
        self.NetPath = _NetPath
        net = graphAttribute(self.NetPath)
        self.G = net.GraphUndirUnWeight()
        ClassName = _PrideDF['ClassName']
        ImportanceRank = _PrideDF[self.metric]
        self.class_ClassRank = dict(zip(ClassName, ImportanceRank))

    def Get_Neigbors(self, Graph, v_i, order=1):
        '''
        :param node:
        :param order:
        :return:
        '''
        neibords_set = {}
        neibords = dict(nx.bfs_successors(Graph, source=v_i, depth_limit=order))
        nodes = [v_i]
        for order_num in range(1, order + 1):
            neibords_set.setdefault(order_num, [])
            for node in nodes:
                neibords_set[order_num].extend(neibords.get(node, []))
            nodes = neibords_set[order_num]
        neighbords_list = []
        for j in neibords_set.values():
            for innode in j:
                neighbords_list.append(innode)
        return neighbords_list

    def RecordAllPath(self):
        '''
        :return:
        '''
        AllPath = {}
        v_i_neigbhords = {}
        nodes = list(self.G.nodes())
        for v_i in nodes:
            v_i_neigbhords[v_i] = self.Get_Neigbors(Graph=self.G, v_i=v_i, order=3)
        for node in self.G.nodes():
            AllPath.setdefault(node, [])
            for source in v_i_neigbhords[node]:
                AllPath[node].extend(list(nx.all_simple_paths(self.G, source=node, target=source, cutoff=3)))
        return AllPath

    def path_length(self, path, weight):
        w = 0
        for ind, nd in enumerate(path[1:]):
            prev = path[ind]
            w += self.G[prev][nd][weight]
        return w

    def _Calculate_CG(self):
        N = len(self.G.nodes())
        nodes = list(self.G.nodes())
        v_i_neigbhords = {}
        for v_i in nodes:
            v_i_neigbhords[v_i] = self.Get_Neigbors(Graph=self.G, v_i=v_i, order=3)

        AllPath = self.RecordAllPath()

        GPC_v_i_dict = {}
        for i in range(N):
            neibords_set = v_i_neigbhords[nodes[i]]
            v_i_ClassRank = self.class_ClassRank[nodes[i]]
            GPC_v_i = 0
            for innode in neibords_set:
                F_ij = 0
                d_ij = nx.shortest_path_length(self.G, source=nodes[i], target=innode)
                if d_ij > 3:
                    continue
                a_kj = {}
                al_kj = {}
                a_ij = {}
                for v in range(1, 4):
                    al_kj[v] = 0
                    a_ij[v] = 0
                a_kj.setdefault(innode, [])
                a_kj[innode] = AllPath[innode]
                for k, v in a_kj.items():
                    for num in v:
                        if 0 <= len(num) - 1 <= 3:
                            al_kj[len(num) - 1] += 1
                for path in nx.all_simple_paths(self.G, source=nodes[i], target=innode, cutoff=3):
                    if len(path) - 1 <= 3:
                        a_ij.setdefault(len(path) - 1, 0)
                        a_ij[len(path) - 1] += 1
                for l in range(d_ij, 4):
                    al_ij = a_ij[l]
                    v_j_ClassRank = self.class_ClassRank[innode]
                    F_ij += (al_ij / (al_kj[l] + 0.01)) * ((v_i_ClassRank * v_j_ClassRank) / (l ** 2))
                GPC_v_i += F_ij
            GPC_v_i_dict[nodes[i]] = GPC_v_i
        result = pd.DataFrame({'ClassName': list(GPC_v_i_dict.keys()), 'CG': list(GPC_v_i_dict.values())})
        return result
