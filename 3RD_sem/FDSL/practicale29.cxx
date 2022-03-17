#include<iostream>
using namespace std;
class queue
{
int queue1[5]; //VARIABLE TO INSERT ELEMENT (data)
int rear,front; //variable rear and front
public:
queue() //constructor
{
rear=-1;
front=-1;
}
void insertjob(int x)
{
if(rear > 4) //check queue is full or not
{
cout <<"queue over flow";
front=rear=-1;
return;
}
queue1[++rear]=x;
cout <<"inserted" <<x;
 }
void deletejob()
{
if(front==rear)
{
cout <<"queue under flow";
return;
}
cout <<"deleted" <<queue1[++front];
}
void display()
{
if(rear==front)
{
cout <<" queue empty";
return;
}
for(int i=front+1;i<=rear;i++)
cout <<queue1[i]<<" ";
}
};
int main()
{
int ch; //choice variable
queue qu; // object of class (instance)
while(1)
{
cout <<"\n\n ********JOB QUEUE PROGRAM**********";
cout <<"\n 1.insert_job \n2.delete_job \n3.display \n4.exit\nEnter your choice :";
cin >> ch;
switch(ch)
{
case 1: cout <<"Enter order id:"; //insert element
cin >> ch;
qu.insertjob(ch);
break;
case 2: qu.deletejob(); break;
case 3: qu.display();break;
case 4: return(0);
}
}
return (0);
}