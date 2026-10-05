public class DissimilarityMatrix {
    public static void main(String[] args) {

        int[][] p = {
            {1, 2},
            {2, 4},
            {5, 5},
            {8, 7}
        };

        System.out.println("Dissimilarity matrix");

        for (int i = 0; i < p.length; i++) {
            for (int j = 0; j < p.length; j++) {

                // Squared distance is used to keep the program simple.
                double distance =
                    (p[i][0] - p[j][0]) * (p[i][0] - p[j][0])
                    + (p[i][1] - p[j][1]) * (p[i][1] - p[j][1]);

                System.out.printf("%.2f ", Math.sqrt(distance));
            }
            System.out.println();
        }
    }
}