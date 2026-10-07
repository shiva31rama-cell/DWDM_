public class WekaExploration {
    public static void main(String[] args) {

        // 1. Create a small sample dataset
        String[][] data = {
            {"Sunny", "30", "Yes"},
            {"Rainy", "20", "No"},
            {"Cloudy", "25", "Yes"},
            {"Sunny", "32", "Yes"},
            {"Rainy", "18", "No"}
        };

        System.out.println("--- DATASET ---");

        // 2. Display all records
        for (int i = 0; i < data.length; i++) {
            System.out.println(
                data[i][0] + " " + data[i][1] + " " + data[i][2]
            );
        }

        // 3. Display number of records and attributes
        System.out.println("\nTotal records = " + data.length);
        System.out.println("Total attributes = 3");

        System.out.println("\n--- ATTRIBUTES ---");
        System.out.println("Weather -> Nominal");
        System.out.println("Temperature -> Numeric");
        System.out.println("Play -> Class attribute");

        // 4. Count class values
        int yes = 0;
        int no = 0;

        for (int i = 0; i < data.length; i++) {
            if (data[i][2].equals("Yes")) {
                yes++;
            } else {
                no++;
            }
        }

        System.out.println("\n--- CLASS COUNT ---");
        System.out.println("Yes = " + yes);
        System.out.println("No  = " + no);

        // 5. Observation
        System.out.println("\nObservation: The dataset has "
                + data.length + " records.");
    }
}