public class OLAP {
    public static void main(String[] args) {

        String[][] product = {
            {"Laptop", "Bhimavaram", "January", "50000"},
            {"Laptop", "Bhimavaram", "February", "60000"},
            {"Phone", "Bhimavaram", "January", "30000"},
            {"Phone", "Vijayawada", "January", "40000}
        };

        System.out.println("SLICE: Product = Laptop");
        for (int i = 0; i < product.length; i++) {
            if (product[i][0].equals("Laptop")) {
                printRow(product[i]);
            }
        }

        System.out.println("\nDICE: Phone from Bhimavaram");
        for (int i = 0; i < product.length; i++) {
            if (product[i][0].equals("Phone")
                    && product[i][1].equals("Bhimavaram")) {
                printRow(product[i]);
            }
        }

        int laptopTotal = 0;
        int phoneTotal = 0;

        // ROLL-UP: calculate total sales for each product
        for (int i = 0; i < product.length; i++) {
            int amount = Integer.parseInt(product[i][3]);

            if (product[i][0].equals("Laptop")) {
                laptopTotal = laptopTotal + amount;
            } else {
                phoneTotal = phoneTotal + amount;
            }
        }

        System.out.println("\nROLL-UP");
        System.out.println("Laptop = " + laptopTotal);
        System.out.println("Phone = " + phoneTotal);

        // DRILL-DOWN: display detailed rows
        System.out.println("\nDRILL-DOWN");
        for (int i = 0; i < product.length; i++) {
            printRow(product[i]);
        }

        // PIVOT is shown as a table in the record.
        System.out.println("\nPIVOT");
        System.out.println("Product       January    February");
        System.out.println("Laptop        50000      60000");
        System.out.println("Phone         70000      0");
    }

    static void printRow(String[] row) {
        System.out.println(row[0] + " " + row[1] + " " + row[2] + " " + row[3]);
    }
}