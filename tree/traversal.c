#include <stdio.h>
#include <stdlib.h>

typedef struct _node
{
    int data;
    struct _node *leftchild;
    struct _node *rightchild;
}Node;


void insert_node(Node **root, const int data)
{
    Node *current = NULL;
    Node *parent = NULL;
    Node *node = NULL;

    node = (Node*)malloc(sizeof(Node));
    if (NULL == node)
    {
        printf("%s: No memory for new node.\n", __func__);
        return;
    }

    node->data = data;
    node->leftchild = NULL;
    node->rightchild = NULL;

    if (NULL == *root)
    {
        *root = node;
    }
    else
    {
        current = *root;
        while (1)
        {
            parent = current;
            if (data < current->data)
            {
                /*go to left child*/
                current = current->leftchild;
                if (NULL == current)
                {
                    parent->leftchild = node;
                    break;
                }
            }
            else
            {
                /*go to right child*/
                current = current->rightchild;
                if (NULL == current)
                {
                    parent->rightchild = node;
                    break;
                }
            }
        }
    }

    return;
}

void pre_order_traversal(const Node *root)
{
    if (root != NULL)
    {
        printf("%d ", root->data);
        pre_order_traversal(root->leftchild);
        pre_order_traversal(root->rightchild);
    }
}

void in_order_traversal(const Node *root)
{
    if (root != NULL)
    {
        in_order_traversal(root->leftchild);
        printf("%d ", root->data);
        in_order_traversal(root->rightchild);
    }
}

void post_order_traversal(const Node *root)
{
    if (root != NULL)
    {
        post_order_traversal(root->leftchild);
        post_order_traversal(root->rightchild);
        printf("%d ", root->data);
    }
}

Node *search(Node *root, const int key)
{
    Node *current = NULL;

    if (NULL == root)
    {
        printf("%s: this tree is empty.\n", __func__);
        return current;
    }

    current = root;
    printf("Visiting elements: ");
    while (current != NULL)
    {
        printf("%d ", current->data);
        if (key == current->data)
        {
            break;
        }
        else if (key < current->data)
        {
            /*go to left child*/
            current = current->leftchild;
        }
        else
        {
            /*go to right child*/
            current = current->rightchild;
        }
    }

    return current;
}

int main()
{
    int i = 0;
    int data[7] = {27, 14, 35, 10, 19, 31, 42};
    Node *root = NULL;
    Node *pos = NULL;

    for (i=0; i<7; i++)
    {
        insert_node(&root, data[i]);
    }

    printf("Inorder traversal: ");
    in_order_traversal(root);
    printf("\n");

    printf("Preorder traversal: ");
    pre_order_traversal(root);
    printf("\n");

    printf("Postorder traversal: ");
    post_order_traversal(root);
    printf("\n");

    pos = search(root, 31);
    if (pos)
    {
        printf(" Element found.\n");
    }
    else
    {
        printf(" Element not found (%d).\n", 31);
    }

    pos = search(root, 15);
    if (pos)
    {
        printf(" Element found.\n");
    }
    else
    {
        printf(" Element not found (%d).\n", 15);
    }

    return 0;
}
