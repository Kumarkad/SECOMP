#include<iostream>
using namespace std;
class pizza
{
int order[10];
int max;
int f,r;
public :
pizza() //constructor
{
f=-1,r=-1;
cout<<"\nEnter Maximum order : ";
cin>>max;
}
int full()
{
if((f==(r+1)%max))
return 1;
else
return 0;
}
int qempty()
{
if(f==-1)
return 1;
else
return 0;
}
void add(int a){ //10
if(full()) //true
{
cout<<"\nOrder is Full!";
}
else //false
{
if(f==-1)// there is no element in queue
{
f=r=0; //set front and rear = 0
}
else //false
{
r=(r+1)%max; //formula for circular queue/ wrap around
}
order[r]=a; //f=0 && r=max-1 f==r+1%max

}
}
void remove()
{
int i;
i=order[f];
if(f==r)// if there is only 1 element in list
{
f=r=-1; //set front and rear to -1
}
else //false
{
f=(f+1)%max; //formula for circular queue
}
cout<<"\n Order deleted : "<<i;
}
void display()
{
int temp;
temp=f;
if(qempty())
{
cout<<"\nNo orders currently\n";
}
else
{
cout<<"\nThe oders are : \n\n";
while(temp!=r){
cout<<" "<<order[temp];
temp=(temp+1)%max; //formula for circular queue
}
cout<<""<<order[temp];
}}
};
int main()
{ 
int ch;
pizza p;// object
do
{
cout<<"\n1. Order \n2. Remove order \n3.Display orders \n4. Exit\n";
cin>>ch;
switch(ch)
{
case 1:
int o;
cout<<"\nEnter Order number : ";
cin>>o;
p.add(o); //call insert function
break;
case 2:p.remove();
break;
case 3:p.display();
break;
}
}
while(ch!=4);
return 0;
}