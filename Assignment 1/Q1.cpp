#include <iostream>
using namespace std;

int main(int argc, char *argv[])
{
    int len=0;
    while(argv[++len] != NULL);

    int i,arrayTEMP[len],num=0,alpha=0,special=0;
    char **array1TEMP[len];

    for(i=0;i<len-1;i++)
        array1TEMP[i]=&argv[i+1];
    for(i=0;i<len-1;i++)
        arrayTEMP[i]=atoi(argv[i+1]);

    for(i=0;i<len-1;i++)
    {
        if(**array1TEMP[i]>=48 && **array1TEMP[i]<=57)
            num++;
        else if (**array1TEMP[i]>=65 && **array1TEMP[i]<=90 || **array1TEMP[i]>=97 && **array1TEMP[i]<=122)
            alpha++;
        else
            special++;
    }

    if(alpha>0)
    {
        cout<<"Please enter numbers only\n";
        int exit_code;
            exit( exit_code );
    }
    else
    {
        for(i=0;i<len-1;i++)
        {
            int temp = arrayTEMP[0];
            for(i=0; i<len-1; i++)
            {
                if(temp>arrayTEMP[i])
                    temp=arrayTEMP[i];
            }
            cout<<"Smallest Number is : "<<temp;
        }
        cout<<"\n";
    }
    return 0;
}

