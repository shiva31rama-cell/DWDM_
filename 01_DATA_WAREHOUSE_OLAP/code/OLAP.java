public class OLAP {
    public static void main(String[] args) {

        // 1. Create a simple sales data cube
        String[][] sales = {
            {"Laptop", "Bhimavaram", "January", "50000"},
            {"Laptop", "Bhimavaram", "February", "60000"},
            {"Phone", "Bhimavaram", "January", "30000"},
            {"Phone", "Vijayawada", "January", "40000"}
        };

        System.out.println("--- ORIGINAL DATA ---");
        for (int i = 0; i < sales.length; i++) {
            printRow(sales[i]);
        }

        // 2. SLICE
        System.out.println("\n--- SLICE: Product = Laptop ---");
        for (int i = 0; i < sales.length; i++) {
            if (sales[i][0].equals("Laptop")) {
                printRow(sales[i]);
            }
        }

        // 3. DICE
        System.out.println("\n--- DICE: Phone and Bhimavaram ---");
        for (int i = 0; i < sales.length; i++) {
            if (sales[i][0].equals("Phone")
                    && sales[i][1].equals("Bhimavaram")) {
                printRow(sales[i]);
            }
        }

        // 4. ROLL-UP
        int laptopTotal = 0;
        int phoneTotal = 0;

        for (int i = 0; i < sales.length; i++) {
            int amount = Integer.parseInt(sales[i][3]);

            if (sales[i][0].equals("Laptop")) {
                laptopTotal = laptopTotal + amount;
            } else {
                phoneTotal = phoneTotal + amount;
            }
        }

        System.out.println("\n--- ROLL-UP: Total by Product ---");
        System.out.println("Laptop = " + laptopTotal);
        System.out.println("Phone  = " + phoneTotal);

        // 5. DRILL-DOWN
        System.out.println("\n--- DRILL-DOWN: Detailed Sales ---");
        for (int i = 0; i < sales.length; i++) {
            printRow(sales[i]);
        }

        // 6. PIVOT
        System.out.println("\n--- PIVOT ---");
        System.out.println("Product       January    February");
        System.out.println("Laptop        50000      60000");
        System.out.println("Phone         70000      0");
    }

    static void printRow(String[] row) {
        System.out.println(
            row[0] + " " + row[1] + " " + row[2] + " " + row[3]
        );
    }
}