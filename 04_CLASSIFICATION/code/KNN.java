public class KNN {
    public static void main(String[] args) {

        // 1. Training data
        int[][] data = {
            {150, 45}, {155, 50}, {160, 52},
            {175, 70}, {180, 75}, {185, 80}
        };

        String[] classes = {"A", "A", "A", "B", "B", "B"};

        // 2. Test record and value of K
        int testHeight = 158;
        int testWeight = 51;
        int k = 3;

        // 3. Calculate squared Euclidean distance
        double[] distance = new double[data.length];

        for (int i = 0; i < data.length; i++) {
            double dh = data[i][0] - testHeight;
            double dw = data[i][1] - testWeight;

            distance[i] = dh * dh + dw * dw;
        }

        // 4. Sort by distance using selection sort
        for (int i = 0; i < distance.length; i++) {
            for (int j = i + 1; j < distance.length; j++) {

                if (distance[j] < distance[i]) {
                    double temp = distance[i];
                    distance[i] = distance[j];
                    distance[j] = temp;

                    String tempClass = classes[i];
                    classes[i] = classes[j];
                    classes[j] = tempClass;
                }
            }
        }

        // 5. Count the first K classes
        int countA = 0;
        int countB = 0;

        for (int i = 0; i < k; i++) {
            if (classes[i].equals("A")) {
                countA++;
            } else {
                countB++;
            }
        }

        // 6. Display result
        System.out.println("--- NEAREST CLASSES ---");

        for (int i = 0; i < k; i++) {
            System.out.println(classes[i]);
        }

        if (countA > countB) {
            System.out.println("Predicted class = A");
        } else {
            System.out.println("Predicted class = B");
        }
    }
}