public class ChiSquare {
    public static void main(String[] args) {

        // 1. Create observed data
        int[][] observed = {
            {50, 10},
            {20, 40}
        };

        // 2. Calculate row totals, column totals and grand total
        int row1 = observed[0][0] + observed[0][1];
        int row2 = observed[1][0] + observed[1][1];

        int col1 = observed[0][0] + observed[1][0];
        int col2 = observed[0][1] + observed[1][1];

        int total = row1 + row2;

        // 3. Calculate expected frequencies
        double e11 = (double) row1 * col1 / total;
        double e12 = (double) row1 * col2 / total;
        double e21 = (double) row2 * col1 / total;
        double e22 = (double) row2 * col2 / total;

        // 4. Calculate Chi-Square value
        double chi = 0;

        chi = chi + (observed[0][0] - e11)
                * (observed[0][0] - e11) / e11;

        chi = chi + (observed[0][1] - e12)
                * (observed[0][1] - e12) / e12;

        chi = chi + (observed[1][0] - e21)
                * (observed[1][0] - e21) / e21;

        chi = chi + (observed[1][1] - e22)
                * (observed[1][1] - e22) / e22;

        // 5. Display the tables
        System.out.println("--- OBSERVED DATA ---");
        System.out.println("Young  Apple = 50, Orange = 10");
        System.out.println("Old    Apple = 20, Orange = 40");

        System.out.println("\n--- EXPECTED DATA ---");
        System.out.println("Young  Apple = " + e11 + ", Orange = " + e12);
        System.out.println("Old    Apple = " + e21 + ", Orange = " + e22);

        System.out.printf("\nChi-Square Value = %.4f%n", chi);

        // 6. Observation
        System.out.println("Observation: The calculated Chi-Square value");
        System.out.println("shows a strong difference between observed");
        System.out.println("and expected frequencies.");
    }
}