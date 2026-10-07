public class Apriori {
    public static void main(String[] args) {

        // 1. Create transaction data
        String[][] transactions = {
            {"Milk", "Bread", "Eggs"},
            {"Milk", "Bread"},
            {"Milk", "Eggs"},
            {"Bread", "Eggs"},
            {"Milk", "Bread", "Eggs"}
        };

        String[] items = {"Milk", "Bread", "Eggs"};
        int minimumSupport = 3;

        // 2. Find frequent 1-itemsets
        System.out.println("--- FREQUENT 1-ITEMSETS ---");

        for (int i = 0; i < items.length; i++) {
            int count = 0;

            for (int t = 0; t < transactions.length; t++) {
                for (int x = 0; x < transactions[t].length; x++) {
                    if (transactions[t][x].equals(items[i])) {
                        count++;
                        break;
                    }
                }
            }

            if (count >= minimumSupport) {
                System.out.println(items[i]
                        + " Support Count = " + count);
            }
        }

        // 3. Find frequent 2-itemsets
        System.out.println("\n--- FREQUENT 2-ITEMSETS ---");

        for (int i = 0; i < items.length; i++) {
            for (int j = i + 1; j < items.length; j++) {

                int count = 0;

                for (int t = 0; t < transactions.length; t++) {
                    boolean first = false;
                    boolean second = false;

                    for (int x = 0; x < transactions[t].length; x++) {
                        if (transactions[t][x].equals(items[i])) first = true;
                        if (transactions[t][x].equals(items[j])) second = true;
                    }

                    if (first && second) count++;
                }

                if (count >= minimumSupport) {
                    System.out.println(items[i] + " + " + items[j]
                            + " Support Count = " + count);
                }
            }
        }
    }
}