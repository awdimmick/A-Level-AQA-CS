//
// Created by Adam Dimmick on 27/11/2021.
//

#ifndef C_GRAPHS_H
#define C_GRAPHS_H

typedef struct graph_node{
    char id;
    struct _node *adjacentNodes;
} GraphNode;

typedef struct _node{
    GraphNode *gn;
    struct _node *next;
} ListNode;

typedef struct graph {
    GraphNode *nodes;
    int nodes_count;
} Graph;


Graph *create_graph(int nodes_count);
void print_graph_node(GraphNode *gn);
void print_graph(Graph *g);
void add_edge(GraphNode *a, GraphNode *b);
void test_graph(void);

#endif //C_GRAPHS_H
