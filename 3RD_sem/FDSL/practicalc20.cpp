#include<iostream>
using namespace std;
class node
{
public:
char status;
int stn;
node *next,*prev;
};
class cinemax
{
public:
node *head,*last;
void create(); //function declaration
void display();
void book();
void cancel();
cinemax() //constructor
{
head=NULL;
}
};
void cinemax::create()
{
node *n;
for(int i=0;i<=7;i++)
{
n=new node; //create new node (allocate memory)
n->status=NULL; //empty node
n->prev=NULL;
if(head==NULL) //
{
head=n;
n->next=head; //1st node
}
else
{
node *t1,*t2;
t1=head;
while(t1->next!=head) //2nd node
{
t2=t1; //prev * next pointer not connected
t1=t1->next;
}
t1->next=n; // linking between two node… t1- n t1 n
n->prev=t1;
n->next=head; //PASSING HEAD TO NEXT NODE due Circular DLL
t1->prev=t2;
}
}
}
void cinemax::display()
{
node *temp;
temp=head;
while(temp->next!=head)
{
cout<<"("<<temp->status<<")"<<" \t ";
temp=temp->next;
}
}
void cinemax::book()
{
node *temp;
int row1,i;
cout<<"Enter seat number you want to book:";
cin>>row1; 
temp=head;
for(i=1;i<row1;i++) //row1 = seat no
{
temp=temp->next;
}
if(temp->status=='B')
{
cout<<"\n Selected seat is not available!!!\n";
}
else
{
temp->status='B';
}
}
void cinemax::cancel()
{
node *temp;
int row1,i;
cout<<"Enter seat number you want to cancel:";
cin>>row1;
temp=head;
for(i=1;i<row1;i++)
{
temp=temp->next;
}
if(temp->status==NULL)
{
cout<<"\n The selected seat is free.\n\n";
}
else
{
temp->status=NULL;
}
}
int main()
{
int row,j=1,choice; //variable declaration
char ans;
cinemax c[10]; //10 row
for(int i=1;i<10;i++)
{
c[i].create(); //to create single row
}
for(int a=0;a<7;a++) //to display column 1 t0 7
{
cout<<" \t "<<j;
++j;
}
cout<<endl;
j=1;
for(int i=1;i<10;i++)
{
cout<<j<<" \t ";
c[i].display();
cout<<endl;
++j;
}
do
{
cout<<"Enter your choice:\n Enter\n 1.Book Seat\n 2.cancel Seat\n";
cin>>choice;
switch(choice)
{
case 1: //book function
cout<<"Enter number of row in which you want to book a seat ";
cin>>row;
c[row].book();
j=1;
for(int k=0;k<7;k++)
{
cout<<" \t "<<j;
++j;
}
cout<<endl;
j=1;
for(int i=1;i<10;i++)
{
cout<<j<<" \t ";
c[i].display();
cout<<endl;
++j;
}
break;
case 2:
cout<<"Enter number of row from which you want to cancel a seat ";
cin>>row;
c[row].cancel();
j=1;
for(int k=0;k<7;k++)
{
cout<<" \t "<<j;
j++;
}
cout<<endl;
j=1;
for(int i=1;i<10;i++)
{
cout<<j<<" \t ";
c[i].display();
cout<<endl;
++j;
}
}
cout<<"\n\nDo you want to continue?Enter y for yes /n for no.\n\n";
cin>>ans;
}while(ans=='y' );
return 0;
}