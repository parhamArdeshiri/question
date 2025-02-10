#include <iostream>
#include <fstream>
#include <string>
#include <bitset>
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

    ////cout << "test 3 passed." << endl;

    return splitedText;
}
int main()
{

    fstream inputFile("./cache/output.txt", ios::in);
    fstream pathFile("./cache/path.txt", ios::in);
    fstream statFile("./cache/stat.txt", ios::out);
    vector <string> binOutput = {};
    string output;
    fstream file;
    string path;

    while(getline(pathFile, path))
    {
        file.open(path, ios::out);
    }

    while (getline(inputFile, output))
    {
            if (path != "") 
            {

                if(!file)
                {
                    statFile << "-1";
                    return -1;
                }

                string binaryStr;

                //cout << "output: " << output << endl;

                for (char c : output)
                {
                    bitset<8> b(c);
                    binaryStr += b.to_string();

                    binOutput.push_back(binaryStr);
                    //cout << "binaryStr: " << binaryStr << endl;
                }

                file << binaryStr << endl;
                binaryStr.clear();
            }
    }

    statFile << "0";

    return 0;
}