/*
Copyright (c) 2013 Moody _"Kuuy"_ Wizmann <mail.kuuy@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
'Software'), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
*/

/*
 * Based on ``HDU-1427 速算24点``
 * Result:2013-01-19 11:31:03	Accepted	1427	625MS	304K	3218 B	G++	Wizmann
 */

#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <string>

using namespace std;

#define print(x) cout<<x<<endl
#define input(x) cin>>x
#define INF 1<<28

const int SIZE=256;

char chopr[]={'+','-','*','/'};

inline int calc(int a,int b,int opr)
{
	if(opr==0) return a+b;
	else if(opr==1) return a-b;
	else if(opr==2) return a*b;
	else if(opr==3)
	{
		if(b!=0 && a%b==0) return a/b;
		else return INF;
	}
	else
	{
		print(opr);
		return INF;
	}
}

bool formula_1(int num[4],int opr[3],string &result)
{
	//（a#b）#(c#d) 
	int a=calc(num[0],num[1],opr[0]);
	int b=calc(num[2],num[3],opr[2]);
	int c=calc(a,b,opr[1]);
	if(a==INF || b==INF || c==INF) return false;
	if(c==24)
	{
		char tmp[256];
		sprintf(tmp,"(%d %c %d) %c (%d %c %d)", \
					num[0],chopr[opr[0]],
					num[1],chopr[opr[1]],
					num[2],chopr[opr[2]],num[3]);
		result=string(tmp);
		
		return true;
	}
	else return false;
}

bool formula_2(int num[4],int opr[3],string &result)
{
	// ((a#b)#c)#d 
	int a=calc(num[0],num[1],opr[0]);
	int b=calc(a,num[2],opr[1]);
	int c=calc(b,num[3],opr[2]);
	if(a==INF || b==INF || c==INF) return false;
	if(c==24)
	{
		char tmp[256];
		sprintf(tmp,"( (%d %c %d) %c %d) %c %d", \
					num[0],chopr[opr[0]],
					num[1],chopr[opr[1]],
					num[2],chopr[opr[2]],num[3]);
		result=string(tmp);
		
		return true;
	}
	else return false;
}

bool formula_3(int num[4],int opr[3],string &result)
{
	// (a#(b#c)#d)
	int a=calc(num[1],num[2],opr[1]);
	int b=calc(num[0],a,opr[0]);
	int c=calc(b,num[3],opr[2]);
	if(c==24)
	{
		
		char tmp[256];
		sprintf(tmp,"(%d %c (%d %c %d)) %c %d", \
					num[0],chopr[opr[0]],
					num[1],chopr[opr[1]],
					num[2],chopr[opr[2]],num[3]);
		result=string(tmp);
		
		return true;
	}
	else return false;
}

string slove(int num[4])
{
	string result="";
	int opr[3];
	sort(num,num+4);
	for(int i=0;i<4;i++)
	{
		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			{
				opr[0]=i;opr[1]=j;opr[2]=k;
				do
				{
					if(formula_1(num,opr,result) \
					  || formula_2(num,opr,result) \
					  || formula_3(num,opr,result))
					{
						return result;
					}
				}while(next_permutation(num,num+4));
			}
		}
	}
	return result;
}

extern "C" 
const char* calc24(int num[4])
{
	string result=slove(num);
	char* res=new char[256];
	strncpy(res,result.c_str(),SIZE);
	return res;
}
