/* A book consists of chapters, chapters consist of sections and sections consist of
subsections. Construct a tree and print the nodes. Find the time and space requirements
of your method.
*/


#include<iostream>
#include<stdlib.h>
using namespace std;

struct node
{
	char title[60];
	int count;
	node *child[50];
}*root;

class tree
	{
		public:
		void insert();
		void display();

		tree()
		{
			root == NULL;
		}
	};

	void tree::insert()
		{
			int secount;
			root = new node();
			cout<<"Enter the name of book : ";
			cin>>root->title;
			cout<<"Enter the total number of chapters in book : ";
			cin>>root->count;
			
			for(int i=0;i<root->count;i++)
				{
					root->child[i] = new node();
					cout<<"Enter the name of chapters : ";
					cin>>root->child[i]->title;

					cout<<"Enter the number of sections : ";
					cin>>root->child[i]->count;
					for(int j=0;j<root->child[i]->count;j++)
						{
							root->child[i]->child[j] = new node();
							cout<<"Enter the name of section : ";
							cin>>root->child[i]->child[j]->title;

							cout<<"Enter the number of sub sections : ";
							cin>>root->child[i]->child[j]->count;
							for(int k=0; k<root->child[i]->child[j]->count; k++)
								{
									root->child[i]->child[j]->child[k] = new node();
									cout<<"Enter the name of sub section : ";
									cin>>root->child[i]->child[j]->child[k]->title;
								}
						}
				}
		}

	void tree::display()
		{
			if(root != NULL)
				{
					cout<<"********** Hierarchy of Book **********"<<endl;
					cout<<"Book Name is "<<root->title<<endl;
					for(int i=0; i<root->count; i++)
						{
							cout<<"— "<<root->child[i]->title<<endl;
							for(int j=0; j<root->child[i]->count; j++)
							{
								cout<<"——– "<<root->child[i]->child[j]->title<<endl;
								for(int k=0; k<root->child[i]->child[j]->count; k++)
								{
									cout<<"—————– "<<root->child[i]->child[j]->child[k]->title<<endl;
								}
							}
						}
				}
		}

int main()
	{
		tree t;
		int ch;
		do
		{
			cout<<"~~~~~ MENU ~~~~~"<<endl;
			cout<<"1. Insert."<<endl;
			cout<<"2. Display."<<endl;
			cout<<"Enter the choice:";
			cin>>ch;

			switch(ch)
			{
				case 1: t.insert();
				break;
				case 2: t.display();
				break;
			}
		}while(ch<3);
	}
