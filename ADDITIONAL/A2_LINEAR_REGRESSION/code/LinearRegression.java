public class LinearRegression {
    public static void main(String[] args) {

        double[] x = {1, 2, 3, 4, 5};
        double[] y = {2, 4, 5, 4, 5};

        double sumX = 0;
        double sumY = 0;

        for (int i = 0; i < x.length; i++) {
            sumX += x[i];
            sumY += y[i];
        }

        double meanX = sumX / x.length;
        double meanY = sumY / y.length;

        double numerator = 0;
        double denominator = 0;

        for (int i = 0; i < x.length; i++) {
            numerator += (x[i] - meanX) * (y[i] - meanY);
            denominator += (x[i] - meanX) * (x[i] - meanX);
        }

        double slope = numerator / denominator;
        double intercept = meanY - slope * meanX;

        double newX = 6;
        double prediction = intercept + slope * newX;

        System.out.println("Slope = " + slope);
        System.out.println("Intercept = " + intercept);
        System.out.println("Prediction for x=6 = " + prediction);
    }
}