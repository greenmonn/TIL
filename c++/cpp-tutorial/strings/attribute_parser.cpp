#include <string>
#include <iostream>
#include <vector>

using namespace std;

typedef pair<string, string> Attribute;
typedef pair<string, vector<Attribute*>> Tag;

string parse_tag_name(string line) {
    stringstream 
    return line;
}

vector<Attribute*> parse_attributes(string line) {
    Attribute attribute = make_pair("test", "test");

    vector<Attribute*> sample;

    sample.push_back(&attribute);

    return sample;
}

void execute() {
    int lineLength, queryCount;

    cin >> lineLength >> queryCount;

    Tag tags[lineLength/2];
    int linePos = 0;

    for (int i = 0; i < lineLength; i++) {
        // parse HRML string and store
        string line;
        getline(cin, line);

        // IF opening tag
            // parse tagname
            string tagName = parse_tag_name(line);

            // parse each attribute
            vector<Attribute*> attributes = parse_attributes(line);

            tags[linePos++] = make_pair(tagName, attributes);
        // ELSE IF closing tag

    }

    for (int i = 0; i < queryCount; i++) {
        // print query result
    }
}