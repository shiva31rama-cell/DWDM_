public class ChiSquare {
    public static void main(String[] args) {

        int[][] observed = {{30, 20}, {10, 40}};

        int row1 = 50;
        int row2 = 50;
        int col1 = 40;
        int col2 = 60;
        int total = 100;

        double e11 = (double) row1 * col1 / total;
        double e12 = (double) row1 * col2 / total;
        double e21 = (double) row2 * col1 / total;
        double e22 = (double) row2 * col2 / total;

        double chi = 0;

        chi += (observed[0][0] - e11) * (observed[0][0] - e11) / e11;
        chi += (observed[0][1] - e12) * (observed[0][1] - e12) / e12;
        chi += (observed[1][0] - e21) * (observed[1][0] - e21) / e21;
        chi += (observed[1][1] - e22) * (observed[1][1] - e22) / e22;

        System.out.println("Chi-square value = " + chi);
    }
}