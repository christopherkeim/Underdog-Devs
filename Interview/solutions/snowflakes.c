#include <stdio.h>
#include <stdlib.h>

#define MAX_ARR_SIZE 100

typedef struct {
  int value;
  struct Node *next;
} Node;

int main(void) {
  Node test_node = {value : 5, next : NULL};

  Node *arr[MAX_ARR_SIZE] = {NULL};

  for (size_t i = 0; i < MAX_ARR_SIZE; i++) {
    arr[i] = malloc(sizeof(Node));
    arr[i]->value = i;
    arr[i]->next = NULL;
    // or: *(arr[i]) = (Node){value : i, next : NULL};
    printf("Node in ARR current: %d\n", arr[i]->value);
  }

  for (int i = 0; i < MAX_ARR_SIZE; i++) {
    printf("Node in ARR: %d\n", arr[i]->value);
    free(arr[i]);
  }

  printf("Size of Node: %ld\n", sizeof(test_node));
}