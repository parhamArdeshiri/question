#include <iostream>
#include <string>
#include <sstream>
#include <bitset>
#include <fstream>
#include <vector>

using namespace std;

vector <string> split(string text, char Char = ' '){
    vector <string> splitedText;
    string word;
    //cout << "test 1 passed." << endl;
    //hello h e l l o
    for (char character : text){
        //cout << "test 2[" << character << "] passed." << endl;
        //cout << character << endl;

        if (character != Char) {
            word += character;
        } else if (!word.empty()) {
            splitedText.push_back(word);
            word.clear();
        }
    }

    if (!word.empty()) splitedText.push_back(word);

    //cout << "test 3 passed." << endl;

    return splitedText;
}

int main()
{
    fstream outputFile("./cache/output.txt", ios::out);
    fstream filePath("./cache/path.txt", ios::in);
    fstream statFile("./cache/stat.txt", ios::out);
    vector <string> splitedData;
    string output;
    string path;
    string data;

    while (getline(filePath, path))
    {
        fstream bin(path, ios::in);

        if(!bin)
        {
            statFile << "-1";
            return -1;
        }

        while (getline(bin, data))
        {
            splitedData = split(data);
            for(string dataPart : splitedData)
            {
                stringstream sstream(dataPart);
                while(sstream.good())
                {
                    bitset<8> bits;
                    sstream >> bits;
                    char c = char(bits.to_ulong());
                    output += c;
                }

                outputFile << output << endl;
                output.clear();

            }
        }
        
    }
    statFile << "0";

    return 0;
}