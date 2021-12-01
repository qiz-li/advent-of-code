#include <fstream>
#include <iostream>
#include <limits>
#include <stdlib.h>
#include <vector>
using namespace std;

int main()
{
    // Read input
    vector<int> nums;
    fstream problemInput(realpath("../input.txt", NULL));
    int num = 0;
    while (problemInput >> num)
    {
        nums.push_back(num);
    }
    problemInput.close();

    int count;
    int prev = INT_MAX;

    for (int i = 2, l = nums.size(); i < l; i++)
    {
        int sum = nums[i - 2] + nums[i - 1] + nums[i];
        if (sum > prev)
        {
            ++count;
        }
        prev = sum;
    }

    cout << count << '\n';
}