public class DissimilarityMatrix {
    public static void main(String[] args) {

        // 1. Create four objects with two attributes
        int[][] points = {
            {1, 2},
            {2, 4},
            {5, 5},
            {8, 7}
        };

        // 2. Calculate and display the matrix
        System.out.println("--- DISSIMILARITY MATRIX ---");

        for (int i = 0; i < points.length; i++) {

            for (int j = 0; j < points.length; j++) {

                double dx = points[i][0] - points[j][0];
                double dy = points[i][1] - points[j][1];

                double distance = Math.sqrt(dx * dx + dy * dy);

                System.out.printf("%.2f ", distance);
            }

            System.out.println();
        }

        // 3. Observation
        System.out.println("\nObservation: Diagonal values are 0.");
    }
}