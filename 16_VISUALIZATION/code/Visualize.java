public class Visualize {
    public static void main(String[] args) {

        int[] scores = {45, 55, 60, 62, 70, 72, 75, 80, 85, 90};

        System.out.println("SIMPLE BAR CHART");

        for (int i = 0; i < scores.length; i++) {
            System.out.print(scores[i] + " : ");

            int bars = scores[i] / 5;

            for (int j = 0; j < bars; j++) {
                System.out.print("*");
            }

            System.out.println();
        }

        System.out.println();
        System.out.println("Use visualize.py for the required");
        System.out.println("Matplotlib histogram, box plot, bar chart and pie chart.");
    }
}