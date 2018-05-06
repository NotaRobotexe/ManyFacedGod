#include <iostream>
#include <Windows.h>
#include <thread>
#include <chrono>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>  
#include <time.h>

using namespace std;

void new_pattern(short delay,string path);
void load_pattern(string path,vector<POINT>& points);
void make_pattern(short delay, vector<POINT> points);
void delay(int time_ms, int random_in_percent);

int main() {
	char pattern;
	cin >> pattern;	

	if (pattern == 'n'){
		new_pattern(4,"test.txt");
	}

	else{
		vector<POINT> points;
		string path = "test.txt";
		load_pattern(path,points);
		make_pattern(4, points);
	}

}

void new_pattern(short delay_ms,string path) {
	POINT p;
	ofstream file;
	vector<POINT> data;
	int move=0;

	while (!(GetKeyState(VK_CONTROL) & 0x8000))
	{
		if((GetKeyState(VK_LBUTTON) & 0x100) != 0){
			p.x = -1;
			p.y = -1;
		}	
		else{
			GetCursorPos(&p);
		}

		this_thread::sleep_for(chrono::milliseconds(delay_ms));
		data.push_back(p);
		move++;
	}	

	file.open(path);
	for (size_t i = 0; i < data.size(); i++){
		file << data[i].x << " " << data[i].y << "\n";
	}

	file.close();

	system("Pause");
}

void load_pattern(string path,vector<POINT>& points) {
	ifstream file;
	file.open(path);
	string buffer{istreambuf_iterator<char>(file), istreambuf_iterator<char>()};
	file.close();

	stringstream isbuff(buffer);
	string part;
	vector<string> data;
	while (getline(isbuff,part,'\n')){
		data.push_back(part);
	}

	vector<string> str_poins;
	string part2;
	for each (string obj in data)
	{
		stringstream isbuff2(obj);

		while (getline(isbuff2,part2,' ')){
			str_poins.push_back(part2);
		}

	}

	for (size_t i = 0; i < str_poins.size(); i+=2)
	{
		POINT p = { stoi(str_poins[i]),stoi(str_poins[i+1]) };
		points.push_back(p);
	}
}

void make_pattern(short delay_ms,vector<POINT> points) {
	for (int i = 0; i < points.size(); i++)
	{
		if (points[i].x > -1){	
			SetCursorPos(points[i].x,points[i].y);
		}
		else if (points[i].x == -1 && points[i - 1].x > -1) {
			mouse_event(MOUSEEVENTF_LEFTDOWN, points[i].x, points[i].y, 0, 0);
		}
		else if (points[i].x == -1 && points[i + 1].x > -1) 
		{
			mouse_event(MOUSEEVENTF_LEFTUP, points[i].x, points[i].y, 0, 0);
		}

		this_thread::sleep_for(chrono::milliseconds(delay_ms));

	}
	system("pause");
}

void write_data() {


}

void delay(float time_ms,float random_in_percent) {
	float min_possible = time_ms - (time_ms / 100 * random_in_percent);
	float max_possible = time_ms + (time_ms / 100 * random_in_percent);

	srand (time(NULL));
	int time = rand() % int(max_possible) - int(min_possible);

	this_thread::sleep_for(chrono::milliseconds(time));
}