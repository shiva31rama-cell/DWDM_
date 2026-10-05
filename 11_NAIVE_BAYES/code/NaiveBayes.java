public class NaiveBayes {
    public static void main(String[] args) {

        String[][] data = {
            {"Sunny", "Hot", "No"},
            {"Sunny", "Cool", "Yes"},
            {"Rainy", "Cool", "Yes"},
            {"Rainy", "Hot", "Yes"},
            {"Cloudy", "Hot", "Yes"},
            {"Cloudy", "Cool", "Yes"}
        };

        String testWeather = "Rainy";
        String testTemperature = "Hot";

        int yes = 0;
        int no = 0;

        for (int i = 0; i < data.length; i++) {
            if (data[i][2].equals("Yes")) yes++;
            else no++;
        }

        int yesWeather = 0, yesTemperature = 0;
        int noWeather = 0, noTemperature = 0;

        for (int i = 0; i < data.length; i++) {
            if (data[i][2].equals("Yes")) {
                if (data[i][0].equals(testWeather)) yesWeather++;
                if (data[i][1].equals(testTemperature)) yesTemperature++;
            } else {
                if (data[i][0].equals(testWeather)) noWeather++;
                if (data[i][1].equals(testTemperature)) noTemperature++;
            }
        }

        double pYes = (double) yes / data.length;
        pYes = pYes * (yesWeather + 1.0) / (yes + 3);
        pYes = pYes * (yesTemperature + 1.0) / (yes + 2);

        double pNo = (double) no / data.length;
        pNo = pNo * (noWeather + 1.0) / (no + 3);
        pNo = pNo * (noTemperature + 1.0) / (no + 2);

        System.out.println("P(Yes) = " + pYes);
        System.out.println("P(No) = " + pNo);

        if (pYes > pNo)
            System.out.println("Predicted class = Yes");
        else
            System.out.println("Predicted class = No");
    }
}