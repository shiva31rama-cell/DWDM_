public class SimulatedDataset {
    public static void main(String[] args) {

        int[][] data = new int[10][2];
        int count = 0;

        // Create simple records.
        for (int age = 18; age < 28; age++) {
            int score = 50 + (age - 18) * 3;

            data[count][0] = age;
            data[count][1] = score;
            count++;
        }

        System.out.println("Unique simulated dataset");

        for (int i = 0; i < count; i++) {
            System.out.println(
                "Age = " + data[i][0] +
                ", Score = " + data[i][1]
            );
        }

        System.out.println("Total unique records = " + count);
    }
}