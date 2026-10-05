public class KNN {
    public static void main(String[] args) {

        int[][] data = {
            {150, 45}, {155, 50}, {160, 52},
            {175, 70}, {180, 75}, {185, 80}
        };

        String[] classes = {"A", "A", "A", "B", "B", "B"};

        int testHeight = 158;
        int testWeight = 51;
        int k = 3;

        double[] distance = new double[data.length];

        for (int i = 0; i < data.length; i++) {
            double dh = data[i][0] - testHeight;
            double dw = data[i][1] - testWeight;
            distance[i] = dh * dh + dw * dw;
        }

        // Selection sort by distance.
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

        int countA = 0;
        int countB = 0;

        for (int i = 0; i < k; i++) {
            if (classes[i].equals("A")) countA++;
            else countB++;
        }

        System.out.println("Nearest classes:");
        for (int i = 0; i < k; i++) {
            System.out.println(classes[i]);
        }

        if (countA > countB)
            System.out.println("Predicted class = A");
        else
            System.out.println("Predicted class = B");
    }
}