//
//Programm Name: Chatterbot1
//Description: this is a very basic example of a chatbot program
//
//Author: Li Xiangyu
//

#include <iostream>
#include <string>
#include <stdlib.h>
#include <ctime>
using namespace std;
int main()
{
	string Response[] = {
		"I HEARD YOU!",
		"SO, YOU ARE TAKING TO ME.",
		"CONTINUE, I'M LISTENING.",
		"VERY INTERESTING CONVERSATION.",
		"TELL ME MORE..."
	};

	srand((unsigned) time(NULL));   //use current time to initial a random number

	string sInput = "";
	string sResponse = "";

	while(1){
		cout << ">";
		getline(cin, sInput);
		int nSelection = rand() % 5;
		sResponse = Response[nSelection];
		cout << sResponse << endl;
	}

	return 0;
}
