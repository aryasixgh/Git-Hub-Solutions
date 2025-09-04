#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


class Solution{
    public:
    int countStudents(std::vector<int>& students, std::vector<int>& sandwiches){
        for(int i=0; i<students.size()-1; i++){
            for(int j=0; j<students.size()-i-1; j++){
                if(students[j]==sandwiches[j]){
                    students[j]=2;
                    sandwiches[j]=2;
                    enqueue(students);
                    pop(sandwiches, )
                }
            }
        }
    }
    
    vector<int> enqueue(vector<int> students){
        //putting a student to the end of the queue
        for(int j=0; j<students.size()-1; j++){
            int temp=students[j];
            students[j]=students[j+1];
            students[j+1]=temp;
        }
        return students;
    }
    vector<int> pop(vector<int> sandwiches, int top){
        //removing a sandwich from the stack
        cout << "Top= " << +sandwiches[top];
        if(sandwiches[top]!=2){
            sandwiches[top]=2;
            --top; //change value of top
        }
        return sandwiches;
    }

};  
int main(){
    cout << "Students unable to eat Program:";
    Solution sol;
    vector<int> students={1,1,0,0};
    vector<int> sandwiches={1,0,1,0};
    reverse(sandwiches.begin(), sandwiches.end());
    int top = sandwiches.size()-1;
    vector<int> ansStudents=sol.enqueue(students);
    vector<int> ansSandwiches=sol.pop(sandwiches, top);
    cout << "Students: ";
    for(int num : ansStudents){
        cout << num << " ";
    }   
    cout << endl << "Sandwiches: ";
    for(int num : ansSandwiches){
        cout << num << " ";
    }
    return 0;
}