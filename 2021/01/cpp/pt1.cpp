#include <fstream>
#include <iostream>
#include <limits>
#include <stdlib.h>
using namespace std;

int main()
{
    fstream problemInput(realpath("../input.txt", NULL));

    int i;
    int count;
    int prev = INT_MAX;

    while (problemInput >> i)
    {
        int cur = i;
        if (cur > prev)
        {
            ++count;
        }
        prev = cur;
    }

    cout << count << '\n';
}