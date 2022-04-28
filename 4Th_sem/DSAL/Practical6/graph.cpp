
 #include<iostream>
#include<stdlib.h>
#include<string.h>
using namespace std;
struct node
{
    string vertex;
    int time=0;
    node *next;
};   

class adjmatlist
{
    int m[10][10],n,i,j;
    char ch;
    string v[20];
    node *head[20];
    node *temp=NULL;

     public:
     adjmatlist()
     {
            for(i=0;i<20;i++)
            {
                head[i]=NULL;
            }
     }
               
     void getgraph();
     void adjlist();
 
     void displaym();
     void displaya();
};

void adjmatlist::getgraph()
{
   cout<<"\n Enter no. of cities(max. 20) : ";
   cin>>n;
   
   for(i=0;i<n;i++)
   {
     cout<<" Enter name of city : ";
     cin>>v[i];
   }
           
   for(i=0;i<n;i++)
   { 
      for(j=0;j<n;j++)
      {
         cout<<"\n If path is present between city "<<v[i]<<" and "<<v[j]<<" then press enter Y or y otherwise N or n : "; 
         cin>>ch;
         if(ch=='y' || ch=='Y')
         { 
           cout<<"\n Enter time required to reach city "<<v[j]<<" from "<<v[i]<<" in minutes : ";
           cin>>m[i][j];
         }
         else if(ch=='n' || ch=='N')
         {
             m[i][j]=0;
         }
         else
         {
             cout<<"\n Invalid entry !!! ";
         }
      }
   }      
      
      adjlist();
}

void adjmatlist::adjlist()
{  
    cout<<"\n *****************************************";
    cout<<endl<<"Cities : ";
       for(i=0;i<n;i++)
       {  
          node *p=new(struct node);
          p->next=NULL;
          p->vertex=v[i];   
          head[i]=p;      
          cout<<"\n"<<head[i]->vertex;
       }
     
       for(i=0;i<n;i++)
       {
          for(j=0;j<n;j++)
          {
                   if(m[i][j]!=0)
                   {      
                         node *p=new(struct node);
                         p->vertex=v[j];
                         p->time=m[i][j];
                         p->next=NULL;
                         if(head[i]->next==NULL)
                         {
                             head[i]->next=p;
                         }
                         else
                         {
                             temp=head[i];
                             while(temp->next!=NULL)
                             {
                                 temp=temp->next;
                             }
                             temp->next=p;
                         }
                   }
          }
       }     
}

void adjmatlist::displaym()
{
     cout<<"********** Adjacency Matrix of Cities **********";
     cout<<"\n";
     for(j=0;j<n;j++)
     {
         cout<<"\t"<<v[j];
     }
     
     cout<<endl<<"---------------------------------------"<<endl;
     
     for(i=0;i<n;i++)
     {
        cout<<"\n "<<v[i];
        for(j=0;j<n;j++)
        {
            cout<<"\t"<<m[i][j];
        }
            cout<<"\n";
            cout<<"---------------------------------------"<<endl;
     }
}  
 
void adjmatlist::displaya()
{     
       cout<<"\n ************ Adjacency list of cities **********";
     
       for(i=0;i<n;i++)
       { 
        if(head[i]==NULL)
        {
           cout<<"\n Adjacency list not present !!!";  
            break;   
        }
        else
         { 
             cout<<"\n"<<head[i]->vertex;
             temp=head[i]->next;
             while(temp!=NULL)
             {
                            cout<<"-> "<<temp->vertex;
                            temp=temp->next;
             }                
         }
       }
     
         cout<<"\n Path and time required to reach cities is : ";
       
       for(i=0;i<n;i++)
       {
                         if(head[i]==NULL)
                         {
                             cout<<"\n Adjacency list not present !!!";
                             break;
                         }
                         else
                         {
                             temp=head[i]->next;
                             while(temp!=NULL)
                             {
                                cout<<"\n"<<head[i]->vertex;
                                cout<<"-> "<<temp->vertex<<"\n   [time required: "<<temp->time<<" min ]";
                                temp=temp->next;
                             } 
                         }
       }
}

int main()
{
   int m;   
   adjmatlist a;

   while(1)
   {
       cout<<"\n\n *************** Graph ***************  ";
       cout<<"\n 1.Enter graph";
       cout<<"\n 2.Display adjacency matrix for cities";
       cout<<"\n 3.Display adjacency list for cities";
       cout<<"\n 4.Exit"<<endl;
       cout<<"Enter your choice : ";
       cin>>m;
  
        switch(m)
       {
                                    case 1: a.getgraph();
                                    break;
                                    case 2: a.displaym();
                                    break;
                                    case 3: a.displaya();
                                    break;
                                    case 4: exit(0);
                                    default:  cout<<"\n Invalid choice !!!";
       }
   }
    return 0;
}   