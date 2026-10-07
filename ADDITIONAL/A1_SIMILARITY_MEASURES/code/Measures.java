public class Measures {
    public static void main(String[] args) {

        // 1. Create two data objects
        double[] A = {1, 2, 3, 4};
        double[] B = {2, 3, 4, 5};

        // 2. Calculate Euclidean and Manhattan distances
        double squareSum = 0;
        double manhattan = 0;

        for (int i = 0; i < A.length; i++) {
            double difference = A[i] - B[i];

            squareSum = squareSum + difference * difference;

            if (difference < 0) {
                difference = -difference;
            }

            manhattan = manhattan + difference;
        }

        double euclidean = Math.sqrt(squareSum);

        // 3. Calculate Cosine Similarity
        double dot = 0;
        double squareA = 0;
        double squareB = 0;

        for (int i = 0; i < A.length; i++) {
            dot = dot + A[i] * B[i];
            squareA = squareA + A[i] * A[i];
            squareB = squareB + B[i] * B[i];
        }

        double cosine = dot / (Math.sqrt(squareA) * Math.sqrt(squareB));

        // 4. Calculate Pearson Correlation
        double meanA = 0;
        double meanB = 0;

        for (int i = 0; i < A.length; i++) {
            meanA = meanA + A[i];
            meanB = meanB + B[i];
        }

        meanA = meanA / A.length;
        meanB = meanB / B.length;

        double numerator = 0;
        double partA = 0;
        double partB = 0;

        for (int i = 0; i < A.length; i++) {
            numerator += (A[i] - meanA) * (B[i] - meanB);
            partA += (A[i] - meanA) * (A[i] - meanA);
            partB += (B[i] - meanB) * (B[i] - meanB);
        }

        double pearson = numerator / Math.sqrt(partA * partB);

        // 5. Calculate Jaccard Similarity
        int intersection = 0;
        int union = 0;

        for (int i = 0; i < A.length; i++) {
            boolean found = false;

            for (int j = 0; j < B.length; j++) {
                if (A[i] == B[j]) {
                    found = true;
                }
            }

            if (found) intersection++;
            union++;
        }

        for (int i = 0; i < B.length; i++) {
            boolean found = false;

            for (int j = 0; j < A.length; j++) {
                if (B[i] == A[j]) {
                    found = true;
                }
            }

            if (!found) union++;
        }

        double jaccard = (double) intersection / union;

        // 6. Display results
        System.out.println("Euclidean Distance = " + euclidean);
        System.out.println("Manhattan Distance = " + manhattan);
        System.out.println("Cosine Similarity = " + cosine);
        System.out.println("Pearson Correlation = " + pearson);
        System.out.println("Jaccard Similarity = " + jaccard);
    }
}