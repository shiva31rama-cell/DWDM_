public class LinearRegression {
    public static void main(String[] args) {

        // 1. Training data
        double[] x = {1, 2, 3, 4, 5};
        double[] y = {2, 4, 5, 4, 5};

        // 2. Calculate means
        double sumX = 0;
        double sumY = 0;

        for (int i = 0; i < x.length; i++) {
            sumX = sumX + x[i];
            sumY = sumY + y[i];
        }

        double meanX = sumX / x.length;
        double meanY = sumY / y.length;

        // 3. Calculate slope
        double numerator = 0;
        double denominator = 0;

        for (int i = 0; i < x.length; i++) {
            numerator = numerator + (x[i] - meanX) * (y[i] - meanY);
            denominator = denominator + (x[i] - meanX) * (x[i] - meanX);
        }

        double slope = numerator / denominator;

        // 4. Calculate intercept
        double intercept = meanY - slope * meanX;

        // 5. Predict a new value
        double newX = 6;
        double prediction = intercept + slope * newX;

        // 6. Display result
        System.out.println("Slope = " + slope);
        System.out.println("Intercept = " + intercept);
        System.out.println("Prediction for x = 6 : " + prediction);
    }
}