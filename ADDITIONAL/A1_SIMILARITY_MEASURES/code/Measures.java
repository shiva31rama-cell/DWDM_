public class Measures {
    public static void main(String[] args) {

        double[] a = {1, 2, 3, 4};
        double[] b = {2, 3, 4, 5};

        double dot = 0;
        double squareA = 0;
        double squareB = 0;
        double euclideanSquare = 0;
        double manhattan = 0;

        for (int i = 0; i < a.length; i++) {
            dot += a[i] * b[i];
            squareA += a[i] * a[i];
            squareB += b[i] * b[i];

            double difference = a[i] - b[i];

            euclideanSquare += difference * difference;

            if (difference < 0) {
                difference = -difference;
            }

            manhattan += difference;
        }

        double cosine = dot / (Math.sqrt(squareA) * Math.sqrt(squareB));

        double meanA = 0;
        double meanB = 0;

        for (int i = 0; i < a.length; i++) {
            meanA += a[i];
            meanB += b[i];
        }

        meanA = meanA / a.length;
        meanB = meanB / b.length;

        double numerator = 0;
        double denominatorA = 0;
        double denominatorB = 0;

        for (int i = 0; i < a.length; i++) {
            numerator += (a[i] - meanA) * (b[i] - meanB);
            denominatorA += (a[i] - meanA) * (a[i] - meanA);
            denominatorB += (b[i] - meanB) * (b[i] - meanB);
        }

        double pearson = numerator /
                Math.sqrt(denominatorA * denominatorB);

        int intersection = 0;
        int union = 0;

        for (int i = 0; i < a.length; i++) {
            boolean found = false;

            for (int j = 0; j < b.length; j++) {
                if (a[i] == b[j]) found = true;
            }

            if (found) intersection++;
            union++;
        }

        for (int i = 0; i < b.length; i++) {
            boolean alreadyPresent = false;

            for (int j = 0; j < a.length; j++) {
                if (b[i] == a[j]) alreadyPresent = true;
            }

            if (!alreadyPresent) union++;
        }

        double jaccard = (double) intersection / union;

        System.out.println("Euclidean = " + Math.sqrt(euclideanSquare));
        System.out.println("Manhattan = " + manhattan);
        System.out.println("Cosine = " + cosine);
        System.out.println("Pearson = " + pearson);
        System.out.println("Jaccard = " + jaccard);
    }
}