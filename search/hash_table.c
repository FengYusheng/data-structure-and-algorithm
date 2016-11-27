#include <stdio.h>
#include <stdlib.h>

#define SIZE 20

typedef struct _dataItem {
  int key;
  int value;
} dateItem;

dateItem *srcArray[SIZE];
dateItem *dummyItem;

int _hashCode(int key) { return key % SIZE; }

dateItem *search(int key) {
  int index = 0;
  index = _hashCode(key);

  while (srcArray[index] != NULL) {
    if (key == srcArray[index]->key) {
      return srcArray[index];
    }
    index++;
    index = _hashCode(index);
  }
  return NULL;
}

void insertItem(int key, int value) {
  int index = -1;
  dateItem *item = (dateItem *)malloc(sizeof(dateItem));
  if (NULL == item) {
    return;
  }

  item->key = key;
  item->value = value;

  index = _hashCode(key);
  while (srcArray[index] != NULL && srcArray[index]->key != -1) {
    index++;
    index = _hashCode(index);
  }
  srcArray[index] = item;
}

void deleteItem(int key) {
  int index = 0;
  index = _hashCode(key);
  while (srcArray[index] != NULL) {
    if (key == srcArray[index]->key) {
      srcArray[index] = dummyItem;
    }
    index++;
    index = _hashCode(index);
  }
}

void dispaly() {
  int i = 0;
  for (i = 0; i < SIZE; i++) {
    if (srcArray[i] != NULL) {
      printf("(%d, %d) ", srcArray[i]->key, srcArray[i]->value);
    } else {
      printf("(NULL, NULL) ");
    }
  }
  printf("\n");
}

int main() {
  dateItem *item = NULL;
  dummyItem = (dateItem *)malloc(sizeof(dummyItem));
  if (NULL == dummyItem) {
    return 0;
  }
  dummyItem->key = -1;
  dummyItem->value = -1;

  insertItem(1, 20);
  insertItem(2, 70);
  insertItem(42, 80);
  insertItem(4, 25);
  insertItem(12, 44);
  insertItem(14, 32);
  insertItem(17, 11);
  insertItem(13, 78);
  insertItem(37, 97);

  dispaly();
  item = search(37);
  if (item != NULL) {
    printf("Found item: (%d, %d)\n", item->key, item->value);
  } else {
    printf("No Found.\n");
  }

  deleteItem(37);
  dispaly();
  item = search(37);
  if (item != NULL) {
    printf("Found (37): (%d, %d)\n", item->key, item->value);
  } else {
    printf("(37) Not Found\n");
  }

  return 0;
}
