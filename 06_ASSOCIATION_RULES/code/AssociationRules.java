public class AssociationRules {
    public static void main(String[] args) {

        // 1. Create transaction data
        String[][] transactions = {
            {"Milk", "Bread", "Eggs"},
            {"Milk", "Bread"},
            {"Milk", "Eggs"},
            {"Bread", "Eggs"},
            {"Milk", "Bread", "Eggs"}
        };

        // Rule: Milk -> Bread
        int milkCount = 0;
        int breadCount = 0;
        int bothCount = 0;

        // 2. Count occurrences
        for (int i = 0; i < transactions.length; i++) {

            boolean milk = false;
            boolean bread = false;

            for (int j = 0; j < transactions[i].length; j++) {
                if (transactions[i][j].equals("Milk")) milk = true;
                if (transactions[i][j].equals("Bread")) bread = true;
            }

            if (milk) milkCount++;
            if (bread) breadCount++;
            if (milk && bread) bothCount++;
        }

        // 3. Calculate support and confidence
        double support = (double) bothCount / transactions.length;
        double confidence = (double) bothCount / milkCount;

        // 4. Display result
        System.out.println("--- ASSOCIATION RULE ---");
        System.out.println("Rule: Milk -> Bread");
        System.out.println("Support = " + support);
        System.out.println("Confidence = " + confidence);

        if (confidence >= 0.70) {
            System.out.println("Observation: Strong rule");
        } else {
            System.out.println("Observation: Weak rule");
        }
    }
}