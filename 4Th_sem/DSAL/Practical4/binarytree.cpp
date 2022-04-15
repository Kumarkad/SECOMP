/*
 Beginning with an empty binary search tree, Construct binary search tree by inserting 
the values in the order given. After constructing a binary tree -
i. Insert new node
ii. Find number of nodes in longest path from root
iii. Minimum data value found in the tree
iv. Change a tree so that the roles of the left and right pointers 
are swapped at every node
v. Search a value
*/

#include<iostream>
#include<stdlib.h>
#include<math.h>
using namespace std;

struct node
{
    int data;
    node *left=NULL;
    node *right=NULL;
};
    
class binarytree
{
    	int n,num;
    	public:
    	
    	node *root;
    	
    	binarytree()
    	{
    	    root=NULL;
    	}
    	
    	node *getnewnode(int in_data)
    	{
    	    node *ptr=new node();
    	    ptr->data=in_data;
    	    ptr->left=NULL;
    	    ptr->right=NULL;
    	    return ptr;
    	}
    	
    	node *insert(node *temp,int in_data)
    	{
    	    if (temp==NULL)
    	    {
    	        temp=getnewnode(in_data);
    	    }
    	    else if(temp->data >in_data)
    	    {
    	        temp->left=insert(temp->left,in_data);
    	    }
    	    else
    	    {
    	        temp->right=insert(temp->right,in_data);
    	    }
    	    return temp;
    	}
    	
    	void inorder(node *temp)
    	{
    	    if (temp !=NULL)
    	    {
    	        inorder(temp->left);
    	        cout<<temp->data<<" ";
    	        inorder(temp->right);
    	    }
    	}
    	 
        void postorder(node *temp)
        {
            if(temp != NULL)
            {
                postorder(temp->left);
                postorder(temp->right);
                cout<<temp->data<<" ";
            }
        }
 
        void preorder(node *temp)
        {
            if(temp != NULL)
            {
                cout<<temp->data<<" ";
                preorder(temp->left);
                preorder(temp->right);
            }
        }
    	
    	void create();
		void addelement();
		void display();
		void minimumdata(node *temp);
		void search(node *temp,int in_data);
		int longestpath(node *temp);
		void mirror(node *temp);
    };
    
    void binarytree::create()
    {
        cout<<"Enter the number of elements in the Binary Tree : ";
        cin>>n;
        for(int i=0;i<n;i++)
        {
            cout<<"Number : ";
            cin>>num;
            root=insert(root,num);
        }
    }
    
    void binarytree::addelement()
    {
        cout<<" Enter the Number do you want insert : ";
            cin>>num;
            root=insert(root,num);
        }
        
     void binarytree::display()
     {
         cout<<"+++++ Inorder Traversal  +++++ "<<endl;
         inorder(root);
         cout<<endl<<"+++++ Postorder Traversal +++++ "<<endl;
         postorder(root);
         cout<<endl<<"+++++ Preorder Traversal +++++ "<<endl;
         preorder(root);
         cout<<endl;
     }
     
     void binarytree::search(node *temp,int in_data)
     {
         cout<<"search"<<endl;
         if (temp != NULL)
         {
             if (temp->data==in_data)
             {
                 cout<<"Element found in Binary Tree "<<endl;
                 return ;
             }
             else if (temp->data > in_data)
             {
                 this->search(temp->left,in_data);
             }
             else if (temp->data < in_data)
             {
                 this->search(temp->right , in_data);
             }
         }
         else
         {
             cout<<"Element not found !!! "<<endl;
             return ;
         }
     }
         
     void binarytree::minimumdata(node *temp)
     {
         while(temp->left != NULL)
         {
             temp=temp->left;
         }
         cout<<"Minimum data : "<<temp->data<<endl;
     }
         
      int binarytree::longestpath(node *temp)
      {
          if(temp==NULL)
              return 0;
              return(max((longestpath(temp->left)),(longestpath(temp->right)))+1);
      }
      
      void binarytree::mirror(node *temp)
      {
           if(temp == NULL)
           {
               return; 
           }
           else
           {
               node *ptr;
               mirror(temp->left);
               mirror(temp->right);
               ptr = temp->left;
               temp->left = temp->right;
               temp->right = ptr; 
           }
      }

int main()
	{
		binarytree bt;
		int ch;
		bt.create();
		do
		{
			cout<<"~~~~~ MENU ~~~~~"<<endl;
			cout<<"1. Insert "<<endl;
			cout<<"2. Display "<<endl;
			cout<<"3. Longest path from root "<<endl;
			cout<<"4. Minimum data in tree "<<endl;
			cout<<"5. Search element in tree "<<endl;
			cout<<"6. Mirror the binary tree "<<endl;
			cout<<"7. Exit"<<endl;
			cout<<"Enter the choice:";
			cin>>ch;

			switch(ch)
			{
				case 1: 
				{
				    bt.addelement();
			    	break;
				}
				case 2:
				{
				     bt.display();
		    		break;
				}
				case 3:
				{
				    cout<<"Longest path from root : "<<bt.longestpath(bt.root)<<endl;
			    	break;
				}
				case 4:
				{
				    bt.minimumdata(bt.root);
				    break;
				}
				case 5:
				{
				    int key=0;
				    cout<<"Enter the number do you want search : ";
				    cin>>key;
				    bt.search(bt.root,key);
			    	break;
				}
				case 6:
				{
				    bt.mirror(bt.root);
				    cout<<"After changing a tree so that the roles of the left and right pointers are swapped at every node"<<endl;
				    bt.display();
				    break;
				}
			}
		}while(ch<7);
	}