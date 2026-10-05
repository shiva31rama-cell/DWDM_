public class ZeroR {
    public static void main(String[] args) {

        String[] classes = {
            "Setosa", "Versicolor", "Setosa", "Virginica", "Setosa"
        };

        int setosa = 0;
        int versicolor = 0;
        int virginica = 0;

        for (int i = 0; i < classes.length; i++) {
            if (classes[i].equals("Setosa")) {
                setosa++;
            } else if (classes[i].equals("Versicolor")) {
                versicolor++;
            } else {
                virginica++;
            }
        }

        String majority;

        if (setosa >= versicolor && setosa >= virginica) {
            majority = "Setosa";
        } else if (versicolor >= virginica) {
            majority = "Versicolor";
        } else {
            majority = "Virginica";
        }

        System.out.println("Setosa count = " + setosa);
        System.out.println("Versicolor count = " + versicolor);
        System.out.println("Virginica count = " + virginica);
        System.out.println("ZeroR prediction = " + majority);
    }
}