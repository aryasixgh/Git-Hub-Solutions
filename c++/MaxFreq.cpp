#include <iostream>
#include <vector>
#include <cmath>

class Solution {
public:
    int maxFrequencyElements(std::vector<int>& nums) {
        std::vector<int> count;
        int nsize = nums.size();
        count.assign(0, nsize);
        for(int i=0; i<nsize; i++){
            for(int j=0; j<nsize; j++){
                if(nums[i]==nums[j]){
                    count[i]+=1;
                    if(count[i]!=0){
                        nums[j]=0;
                    }
                }
            }
        } 
        //sorting
        for(int i=0; i<count.size(); i++){
            for(int j=i; j<count.size(); j++){
               if(count[i]<count[j]){
                    int temp=count[j];
                    count[j]=count[i];
                    count[i]=temp;
               }
            }
        }
        //checking
        for(int i=0; i<count.size(); i++){
            if(count[i]!=count[i+1]){
                return count[i];
            }else{
                int j=0;
                int fcount=0;
                while(count[i]==count[j]){
                    fcount+=count[i];
                    j++;
                }
                return fcount;
            }
        }
        return 0;
    }
    int main(){
        std::vector<int> numss{1,2,2,3,1,4};
        std::cout << "Output:" << maxFrequencyElements(numss);
        

    }
};