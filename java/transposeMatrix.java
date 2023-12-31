public class transposeMatrix {
    /*
     * 867. Transpose Matrix --- Easy
     * 
     * Given a 2D integer array matrix, return the transpose of matrix.
     * 
     * The transpose of a matrix is the matrix flipped over its main diagonal,
     * switching the matrix's row and column indices.
     * 
     * Example 1:
     * Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
     * Output: [[1,4,7],[2,5,8],[3,6,9]]
     * 
     * Example 2:
     * Input: matrix = [[1,2,3],[4,5,6]]
     * Output: [[1,4],[2,5],[3,6]]
     * 
     * 
     * Constraints:
     * m == matrix.length
     * n == matrix[i].length
     * 1 <= m, n <= 1000
     * 1 <= m * n <= 105
     * -10elev 9 <= matrix[i][j] <= 10elev9
     * 
     */

    public static void imprimirMatriz(int[][] matrix) {
        for (int[] fila : matrix) {
            for (int elemento : fila) {
                System.out.print(elemento + " ");
            }
            System.out.println();
        }
    }

    public static int[][] transpose(int[][] matrix) {
        int[][] res = new int[matrix[0].length][matrix.length];

        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                res[j][i] = matrix[i][j];
            }
        }

        return res;
    }

    public static void main(String[] args) {

        int[][] matrix = { { 1, 2, 3 }, { 4, 5, 6 }, { 7, 8, 9 } };
        System.out.println("Before transposing");
        imprimirMatriz(matrix);
        int[][] trans = transpose(matrix);
        System.out.println("After transposing");
        imprimirMatriz(trans);

    }

}