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

        int yesCount = 0;
        int noCount = 0;

        for (int i = 0; i < data.length; i++) {
            if (data[i][2].equals("Yes")) {
                yesCount++;
            } else {
                noCount++;
            }
        }

        int yesWeather = 0, yesTemp = 0;
        int noWeather = 0, noTemp = 0;

        for (int i = 0; i < data.length; i++) {
            if (data[i][2].equals("Yes")) {
                if (data[i][0].equals(testWeather)) yesWeather++;
                if (data[i][1].equals(testTemperature)) yesTemp++;
            } else {
                if (data[i][0].equals(testWeather)) noWeather++;
                if (data[i][1].equals(testTemperature)) noTemp++;
            }
        }

        double yesProbability = ((double) yesCount / data.length)
                * (yesWeather + 1.0) / (yesCount + 3)
                * (yesTemp + 1.0) / (yesCount + 2);

        double noProbability = ((double) noCount / data.length)
                * (noWeather + 1.0) / (noCount + 3)
                * (noTemp + 1.0) / (noCount + 2);

        System.out.println("Yes probability = " + yesProbability);
        System.out.println("No probability = " + noProbability);

        if (yesProbability > noProbability)
            System.out.println("Predicted class = Yes");
        else
            System.out.println("Predicted class = No");
    }
}