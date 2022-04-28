#include <bits/stdc++.h>
using namespace std;

struct Node
{
  int key;
  Node *left, *right;
  bool isThreaded;
};

Node *createThreaded(Node *root)
{

  if (root == NULL)
    return NULL;
  if (root->left == NULL &&
    root->right == NULL)
    return root;

  if (root->left != NULL)
  {

    Node* l = createThreaded(root->left);

    l->right = root;
    l->isThreaded = true;
  }

  if (root->right == NULL)
    return root;

  return createThreaded(root->right);
}

Node *leftMost(Node *root)
{
  while (root != NULL && root->left != NULL)
    root = root->left;
  return root;
}

void inOrder(Node *root)
{
  if (root == NULL) return;

  Node *cur = leftMost(root);

  while (cur != NULL)
  {
    cout << cur->key << " ";

    if (cur->isThreaded)
      cur = cur->right;

    else
      cur = leftMost(cur->right);
  }
}

Node *newNode(int key)
{
  Node *temp = new Node;
  temp->left = temp->right = NULL;
  temp->key = key;
  return temp;
}

Node *insert(Node *temp,int in_data)
      {
          if (temp==NULL)
          {
              temp=newNode(in_data);
          }
          else if(temp->key >in_data)
          {
              temp->left=insert(temp->left,in_data);
          }
          else
          {
              temp->right=insert(temp->right,in_data);
          }
          return temp;
      }

int main()
{
    int n=0;
    int num=0;
    Node *root;
    root=NULL;
        cout<<"Enter the number of elements in the Binary Tree : ";
        cin>>n;
        for(int i=0;i<n;i++)
        {
            cout<<"Number : ";
            cin>>num;
            root=insert(root,num);
        }

    
  createThreaded(root);

  cout << "Inorder traversal of created "
      "threaded tree is\n";
  inOrder(root);
  return 0;
}