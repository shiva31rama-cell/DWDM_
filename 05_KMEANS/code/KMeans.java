public class KMeans {
    public static void main(String[] args) {

        int[][] points = {
            {1, 1}, {2, 1}, {1, 2},
            {8, 8}, {9, 8}, {8, 9}
        };

        double c1x = 1, c1y = 1;
        double c2x = 8, c2y = 8;

        for (int repeat = 0; repeat < 5; repeat++) {

            int c1Count = 0, c2Count = 0;
            double c1xSum = 0, c1ySum = 0;
            double c2xSum = 0, c2ySum = 0;

            for (int i = 0; i < points.length; i++) {

                double d1 = (points[i][0] - c1x) * (points[i][0] - c1x)
                          + (points[i][1] - c1y) * (points[i][1] - c1y);

                double d2 = (points[i][0] - c2x) * (points[i][0] - c2x)
                          + (points[i][1] - c2y) * (points[i][1] - c2y);

                if (d1 <= d2) {
                    c1xSum += points[i][0];
                    c1ySum += points[i][1];
                    c1Count++;
                } else {
                    c2xSum += points[i][0];
                    c2ySum += points[i][1];
                    c2Count++;
                }
            }

            c1x = c1xSum / c1Count;
            c1y = c1ySum / c1Count;
            c2x = c2xSum / c2Count;
            c2y = c2ySum / c2Count;
        }

        System.out.println("Cluster 1 center = (" + c1x + ", " + c1y + ")");
        System.out.println("Cluster 2 center = (" + c2x + ", " + c2y + ")");
    }
}