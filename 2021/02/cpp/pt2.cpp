#include <fstream>
#include <iostream>
#include <string>
using namespace std;

int main()
{
    fstream file("../input.txt");
    string commandRaw;

    int hor = 0;
    int depth = 0;
    int aim = 0;

    while (getline(file, commandRaw))
    {
        string command = commandRaw.substr(0, commandRaw.find(' '));
        int num = stoi(commandRaw.substr(commandRaw.find(' ')));

        if (command == "up")
        {
            aim -= num;
        }
        else if (command == "down")
        {
            aim += num;
        }
        else if (command == "forward")
        {
            hor += num;
            depth += aim * num;
        }
    }

    cout << hor * depth << '\n';
}