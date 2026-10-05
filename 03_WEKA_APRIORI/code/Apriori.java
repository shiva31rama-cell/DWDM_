public class Apriori {
    public static void main(String[] args) {

        String[][] transactions = {
            {"milk", "bread", "eggs"},
            {"milk", "bread"},
            {"milk", "eggs"},
            {"bread", "eggs"},
            {"milk", "bread", "eggs"}
        };

        String[] items = {"bread", "eggs", "milk"};
        int minimumSupport = 3;

        System.out.println("Frequent 1-itemsets");

        for (int i = 0; i < items.length; i++) {
            int count = 0;

            for (int t = 0; t < transactions.length; t++) {
                if (contains(transactions[t], items[i])) {
                    count++;
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
                    if (contains(transactions[t], items[i])
                            && contains(transactions[t], items[j])) {
                        count++;
                    }
                }

                if (count >= minimumSupport) {
                    System.out.println(items[i] + " + "
                            + items[j] + " count = " + count);
                }
            }
        }
    }

    static boolean contains(String[] transaction, String item) {
        for (int i = 0; i < transaction.length; i++) {
            if (transaction[i].equals(item)) {
                return true;
            }
        }
        return false;
    }
}