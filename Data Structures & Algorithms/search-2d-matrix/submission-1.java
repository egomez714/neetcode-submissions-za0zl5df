class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int ROWS = matrix.length;
        int COLS = matrix[0].length;

        int left = 0, right = ROWS * COLS - 1;

        while (left <= right){
            int middle = left + (right - left) / 2;
            int row = middle / COLS, col = middle % COLS;
            if (matrix[row][col] == target){
                return true;
            }else if (matrix[row][col] > target){
                right = middle - 1;
            }
            else{
                left = middle + 1;
            }
        }
        return false;
    }
}
