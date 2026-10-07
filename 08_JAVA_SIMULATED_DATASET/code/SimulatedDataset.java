public class SimulatedDataset {
    public static void main(String[] args) {

        // 1. Create an empty dataset
        int[][] data = new int[10][2];
        int count = 0;

        // 2. Generate unique records
        for (int age = 18; age < 28; age++) {
            int score = 50 + (age - 18) * 3;

            data[count][0] = age;
            data[count][1] = score;
            count++;
        }

        // 3. Display the dataset
        System.out.println("--- SIMULATED DATASET ---");

        for (int i = 0; i < count; i++) {
            System.out.println(
                "Age = " + data[i][0]
                + ", Score = " + data[i][1]
            );
        }

        // 4. Display total
        System.out.println("Total unique records = " + count);
    }
}