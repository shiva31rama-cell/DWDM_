public class Apriori {
    public static void main(String[] args) {

        String[][] transactions = {
            {"milk", "bread", "eggs"},
            {"milk", "bread"},
            {"milk", "eggs"},
            {"bread", "eggs"},
            {"milk", "bread", "eggs"}
        };

        String[] items = {"milk", "bread", "eggs"};
        int minimumSupport = 3;

        System.out.println("Frequent 1-itemsets");

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
                System.out.println(items[i] + " count = " + count);
            }
        }

        System.out.println("\nFrequent 2-itemsets");

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
                    System.out.println(items[i] + " + "
                            + items[j] + " count = " + count);
                }
            }
        }
    }
}