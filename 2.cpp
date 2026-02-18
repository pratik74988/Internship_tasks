#include <iostream>
#include <vector>
using namespace std;


class student {
public :
 int age;
 string name;
 int roll_no ;
 int marks ; 
 student(){
    cout<<age<<" "<<name<<"  "<<roll_no <<"  "<< marks <<endl;
 };
};

int main (){
    student n;
    student n2;
    return 0;
// vector <int> nums;
// for (int i = 0; i<3; i++){
//     int a;
//     cin>>a;
//     nums.push_back(a);}

// vector <int> nums = {2 , 1 , 4};
// int maxx = INT32_MIN;
// for (int i = 0; i < nums.size(); i++){
//     if (maxx < nums[i]){
//         maxx = nums[i];
//     }
// }



}
