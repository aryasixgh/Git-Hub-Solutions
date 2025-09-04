#include <iostream>
#include <vector>
#include <cmath>

class Solution {
public:
    int distinctIntegers(int n) {
        int x = 0;
        std::vector<int> board;
        board.push_back(n);
        int temp = 0;

        // Run the rotation loop until we find a repeated pattern or reach a limit
        while (true) {
            for (int k = temp; k < board.size(); k++) {
                x = board[k];
                std::vector<int> tempBoard;  // Temporary vector to store the next rotation

                // Find i to put in board
                for (int i = 1; i <= n; i++) {
                    if (x % i == 1) {
                        tempBoard.push_back(i);
                    }
                }

                // Check if the pattern repeats
                if (tempBoard == board) {
                    return board.size();
                }

                // Update the board with the new rotation
                board.insert(board.end(), tempBoard.begin(), tempBoard.end());
                temp++;
                break;
            }
        }

        // This point may never be reached, depending on the pattern
        return -1;
    }
};

int main() {
    Solution solution;
    int ans = solution.distinctIntegers(3);
    std::cout << "Output: " << ans << std::endl;
    return 0;
}
