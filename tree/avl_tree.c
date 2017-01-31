/*
* Reference: http://www.geeksforgeeks.org/avl-tree-set-1-insertion/
*/

#include <stdio.h>
#include <stdlib.h>

typedef struct _node
{
    int data;
    int count;
    struct _node *leftchild;
    struct _node *rightchild;
}Node;

int get_balance(const Node *root)
{
    Node *leftchild = root->leftchild;
    Node *rightchild = root->rightchild;
    int leftheight = 0;
    int rightheight = 0;

    if (leftchild)
    {
        leftheight = leftchild->count;
    }

    if (rightchild)
    {
        rightheight = rightchild->count;
    }

    return leftheight - rightheight;
}

void left_rotation(Node **root)
{
    Node *n1 = (*root)->rightchild;
    Node *n2 = n1->leftchild;
    int count1 = (*root)->count;

    n1->leftchild = *root;
    n1->count = count1;
    (*root)->rightchild = n2;
    (*root)->count = 1;
    if (n2 != NULL)
    {
        (*root)->count = (*root)->leftchild->count + n2->count + 1;
    }

    *root = n1;
}

void right_rotation(Node **root)
{
    Node *n1 = (*root)->leftchild;
    Node *n2 = n1->rightchild;
    int count1 = (*root)->count;

    n1->rightchild = *root;
    (*root)->leftchild = n2;
    n1->count = count1;
    (*root)->count = 1;
    if (n2 != NULL)
    {
        (*root)->count = (*root)->rightchild->count + n2->count + 1;
    }

    *root = n1;
}

void left_right_rotation(Node **root)
{
    left_rotation(&((*root)->leftchild));
    right_rotation(root);
}

void right_left_rotation(Node **root)
{
    right_rotation(&((*root)->rightchild));
    left_rotation(root);
}

void rotate(Node **root, const int data)
{
    Node *left = (*root)->leftchild;
    Node *right = (*root)->rightchild;
    int factor = 0;
    factor = get_balance(*root);

    if (factor >= 2 && data < left->data)
    {
        /*
        *  This node is inserted in the left subtree of the left subtree.
        *  This tree needs a right rotation.
        */
        right_rotation(root);
    }
    else if(factor <= -2 && data >= right->data)
    {
        /*
        * This node is inserted in the right subtree of right subtree.
        * This tree needs a left rotation.
        */
        left_rotation(root);
    }
    else if (factor >= 2 && data >= left->data)
    {
        /*
        * This node is inserted in the right subtree of left subtree.
        * This tree needs a left right rotation.
        */
        left_right_rotation(root);
    }
    else if(factor <= -2 && data < right->data)
    {
        /*
        * This node is inserted in the left subtree of right subtree.
        * This tree needs a right left rotation.
        */
        right_left_rotation(root);
    }
}

void insert(Node **root, const int data)
{
    Node *node = NULL;
    Node *current = NULL;
    Node *parent = NULL;
    node = (Node*)malloc(sizeof(Node));
    if (NULL == node)
    {
        printf("%s: No memory to insert %d.\n", __func__, data);
        return;
    }

    node->data = data;
    node->count = 1;
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
            (parent->count)++;
            if (data < current->data)
            {
                /*go to left subtree*/
                current = current->leftchild;
                if (NULL == current)
                {
                    parent->leftchild = node;
                    break;
                }
            }
            else
            {
                /*go to right subtree*/
                current = current->rightchild;
                if (NULL == current)
                {
                    parent->rightchild = node;
                    break;
                }
            }
        }
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

void pre_order_traversal(const Node *root)
{
    if (root != NULL)
    {
        printf("%d ", root->data);
        pre_order_traversal(root->leftchild);
        pre_order_traversal(root->rightchild);
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

int main()
{
    int data[6] = {10, 20, 30, 40, 50, 25};
    int i = 0;
    Node *root = NULL;

    for (i=0; i<6; i++)
    {
        insert(&root, data[i]);
        rotate(&root, data[i]);
    }

    printf("Inorder traversal: ");
    in_order_traversal(root);
    printf("\n");

    printf("Preoder traversal: ");
    pre_order_traversal(root);
    printf("\n");

    printf("Postorder traversal: ");
    post_order_traversal(root);
    printf("\n");

    return 0;
}
