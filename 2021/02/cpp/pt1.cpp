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

    while (getline(file, commandRaw))
    {
        string command = commandRaw.substr(0, commandRaw.find(' '));
        int num = stoi(commandRaw.substr(commandRaw.find(' ')));

        if (command == "forward")
        {
            hor += num;
        }
        else if (command == "up")
        {
            depth -= num;
        }
        else if (command == "down")
        {
            depth += num;
        }
    }

    cout << hor * depth << '\n';
}