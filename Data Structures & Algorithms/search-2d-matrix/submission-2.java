class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int numberOfRows = matrix.length;
        int numberOfCols = matrix[0].length;

        int left = 0;
        int right = numberOfRows * numberOfCols - 1;

        while (left <= right){
            int middle = left + (right - left) / 2;
            int row = middle / numberOfCols;
            int col = middle % numberOfCols;
            if (matrix[row][col] == target){
                return true;
            }else if(matrix[row][col] > target){
                right = middle - 1;
            }else{
                left = middle + 1;
            }
        }
        return false;
    }
}
