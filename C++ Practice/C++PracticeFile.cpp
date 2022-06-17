#include <iostream>
using namespace std;

int main()
{
    int x [] = {5,6,7,8,9,10,20,30,40};
    
    int arrSize = sizeof(x)/sizeof(x[0]);
    
    for(int i = 0; i < arrSize; i++){
        std::cout << x[i] << std::endl;
    }
}

