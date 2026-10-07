public class Visualize {
    public static void main(String[] args) {

        // 1. Line graph representation
        int[] x = {0, 2, 4, 6, 8};
        int[] y = {0, 4, 16, 36, 64};

        System.out.println("--- LINE GRAPH DATA ---");
        for (int i = 0; i < x.length; i++) {
            System.out.println("(" + x[i] + ", " + y[i] + ")");
        }

        // 2. Scatter plot representation
        System.out.println("\n--- SCATTER PLOT DATA ---");
        int[] sx = {2, 4, 6, 8, 10, 12};
        int[] sy = {50, 70, 20, 80, 90, 40};

        for (int i = 0; i < sx.length; i++) {
            System.out.println("(" + sx[i] + ", " + sy[i] + ")");
        }

        // 3. Histogram representation
        int[] marks = {90, 95, 20, 35, 70, 75, 60, 65, 30, 55};

        System.out.println("\n--- HISTOGRAM COUNTS ---");
        int low = 0;
        int mid = 0;
        int high = 0;

        for (int i = 0; i < marks.length; i++) {
            if (marks[i] < 50) {
                low++;
            } else if (marks[i] < 80) {
                mid++;
            } else {
                high++;
            }
        }

        System.out.println("0-49  = " + low);
        System.out.println("50-79 = " + mid);
        System.out.println("80-100 = " + high);

        // 4. Bar chart
        String[] category = {"H", "E", "M", "A"};
        int[] value = {30, 50, 70, 90};

        System.out.println("\n--- BAR CHART ---");
        for (int i = 0; i < category.length; i++) {
            System.out.print(category[i] + " : ");

            for (int j = 0; j < value[i] / 10; j++) {
                System.out.print("*");
            }

            System.out.println();
        }

        // 5. Box plot data
        int[] boxData = {11, 4, 6, 8, 6, 9, 3};

        System.out.println("\n--- BOX PLOT DATA ---");
        for (int i = 0; i < boxData.length; i++) {
            System.out.print(boxData[i] + " ");
        }

        // 6. Pie chart data
        System.out.println("\n\n--- PIE CHART DATA ---");
        System.out.println("Excellent = 35%");
        System.out.println("Good      = 30%");
        System.out.println("Average   = 20%");
        System.out.println("Poor      = 15%");

        System.out.println("\nObservation: Python Matplotlib is used to");
        System.out.println("display the actual graphs and charts.");
    }
}