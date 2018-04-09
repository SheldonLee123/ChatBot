//
// Program Name: chatbot2
// Description: this is an improved version
// of the previous chatterbot program "chatbot1"
// this one will try a little bit more to understand what the user is trying to say
//
// Author: Li Xiangyu
//


#pragma warning(disable: 4786)  //标识符过长，超过了最大限定255个字,屏蔽4786warning  

#include <iostream>
#include <string>
#include <vector>
#include <ctime>

using namespace std;

const int MAX_RESP = 3;

typedef vector<string> vstring;

vstring find_match(string input);
void copy(char *array[], vstring &v);

typedef struct {
	char *input;
	char *responses[MAX_RESP];
}record;

record KnowledgeBase[] = {
	{
		"WHAT IS YOUR NAME",
		{
		"MY NAME IS CHATBOT2.",
	 	"YOU CAN CALL ME CHATBOT2.",
	 	"WHY DO YOU WANT TO KNOW MY NAME"
	 	}		
	},

	{
		"HI",
		{
		"HI THERE!",
		"HOW ARE YOU?",
		"HI!"
		}
	},

	{
		"HOW ARE YOU",
		{
		"I'M DOING FINE!",
		"I'M DOING WELL AND YOU?",
		"WHY DO YOU WANT TO KNOW HOW AM I DOING?"
		}
	},

	{
		"WHO ARE YOU",
		{
		"I'M AN A.I PROGRAM.",
		"I THINK THAT YOU KNOW WHO I'M",
		"WHY ARE YOU ASKING?"
		}
	},

	{
		"ARE YOU INTELLIGENT",
		{
		"YES, OF COURSE.",
		"WHAT DO YOU THINK?",
		"ACTUALLY, I'M VERY INTELLIGENT!"
		}
	},

	{
		"ARE YOU REAL",
		{
		"DOES THAT QUESTION REALLY MATERS TO YOU?",
		"WHAT DO YOU MEAN BY WHAT?",
		" I'M AS REAL AS I CAN BE."
		}
	}	
};

size_t nKnowledgeBaseSize = sizeof(KnowledgeBase)/sizeof(KnowledgeBase[0]);

int main() {
	srand((unsigned) time(NULL));

	string sInput = "";
	string sResponse = "";

	while(1) {
		cout << ">";
		getline(cin, sInput);
		vstring responses = find_match(sInput);
		if(sInput == "BYE") {
			cout << "IT WAS NICE TALKING TO YOU USER, SEE YOU NEXTTIME!" << endl;
			break;
		}
		else if(responses.size() == 0) {
			cout << "I'M NOT SURE IF I UNDERSTAND WHAT YOU ARE TALKING ABOUT." << endl;
		}
		else {
			int nSelection = rand() % MAX_RESP;
			sResponse = responses[nSelection];
			cout << sResponse << endl;
		}
	}
	return 0;
}

// make a search for the user's input
// inside the datebase of the program
vstring find_match(string input) {
	vstring result;
	for(int i = 0; i< nKnowledgeBaseSize; ++i) {
		if(string(KnowledgeBase[i].input) == input) {
			copy(KnowledgeBase[i].responses, result);
			return result;
		}
	}
	return result;
}

void copy(char *array[], vstring &v) {
	for(int i=0; i < MAX_RESP; ++i) {
		v.push_back(array[i]);
	}
}