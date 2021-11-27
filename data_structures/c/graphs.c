#include <stdio.h>
#include <stdlib.h>
#include "graphs.h"

void test_graph(void) {
  
  Graph *g = create_graph(5);

  /* Add edges via node adjacency lists */

  // A -> B
  add_edge(&g->nodes[0], &g->nodes[1]);

  // B -> A, C, E
  add_edge(&g->nodes[1], &g->nodes[0]);
  add_edge(&g->nodes[1], &g->nodes[2]);
  add_edge(&g->nodes[1], &g->nodes[4]);

  // C -> B, D
  add_edge(&g->nodes[2], &g->nodes[1]);
  add_edge(&g->nodes[2], &g->nodes[3]);
  
  //D -> C, E
  add_edge(&g->nodes[3], &g->nodes[2]);
  add_edge(&g->nodes[3], &g->nodes[4]);

  // E -> B, D
  add_edge(&g->nodes[4], &g->nodes[1]);
  add_edge(&g->nodes[4], &g->nodes[3]);
  
  print_graph(g);
}

void add_edge(GraphNode *a, GraphNode *b){

  // In case of an empty adjacency list, just add the item

  if (a->adjacentNodes == NULL){

    a->adjacentNodes = malloc(sizeof(ListNode));
    a->adjacentNodes->gn = b;
    a->adjacentNodes->next = NULL;

  }
  else
  {
  // Traverse a's adjacency list, reach the end, add pointer to b
  
  ListNode *n = a->adjacentNodes;

  while (n->next != NULL){
    n = n->next;
  }

  n->next = malloc(sizeof(ListNode));
  n->next->gn = b;
  n->next->next = NULL;
  }
}

void print_graph(Graph *g){

  for (int i = 0; i < g->nodes_count; i++){
    print_graph_node(&g->nodes[i]);
  }
  
}

void print_graph_node(GraphNode *gn){

  printf("%c is connected to: ", gn->id);

  ListNode *n = gn->adjacentNodes;

  while (n!=NULL){

    printf("%c", n->gn->id);
    if (n->next!=NULL){
      printf(", ");
    }
    n = n->next;

  }

  printf("\n");
}


Graph *create_graph(int nodes_count){

  Graph *g = malloc(sizeof(Graph));

  g->nodes_count = nodes_count;

  g->nodes = calloc(g->nodes_count, sizeof(GraphNode));

  for (int i = 0; i<g->nodes_count; i++){

    g->nodes[i].id = 'A' + i;
    g->nodes[i].adjacentNodes = NULL;

  }
  return g;
}


