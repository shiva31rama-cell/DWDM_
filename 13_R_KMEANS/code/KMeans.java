public class KMeans {
    public static void main(String[] args) {

        int[][] points = {
            {1, 1}, {2, 1}, {1, 2},
            {8, 8}, {9, 8}, {8, 9}
        };

        double c1x = 1, c1y = 1;
        double c2x = 8, c2y = 8;

        for (int repeat = 0; repeat < 5; repeat++) {
            double x1 = 0, y1 = 0, x2 = 0, y2 = 0;
            int count1 = 0, count2 = 0;

            for (int i = 0; i < points.length; i++) {
                double d1 = (points[i][0] - c1x) * (points[i][0] - c1x)
                          + (points[i][1] - c1y) * (points[i][1] - c1y);

                double d2 = (points[i][0] - c2x) * (points[i][0] - c2x)
                          + (points[i][1] - c2y) * (points[i][1] - c2y);

                if (d1 <= d2) {
                    x1 += points[i][0];
                    y1 += points[i][1];
                    count1++;
                } else {
                    x2 += points[i][0];
                    y2 += points[i][1];
                    count2++;
                }
            }

            c1x = x1 / count1;
            c1y = y1 / count1;
            c2x = x2 / count2;
            c2y = y2 / count2;
        }

        System.out.println("Center 1 = " + c1x + ", " + c1y);
        System.out.println("Center 2 = " + c2x + ", " + c2y);
    }
}