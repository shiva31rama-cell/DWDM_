public class AssociationRules {
    public static void main(String[] args) {

        String[][] transactions = {
            {"milk", "bread", "eggs"},
            {"milk", "bread"},
            {"milk", "eggs"},
            {"bread", "eggs"},
            {"milk", "bread", "eggs"}
        };

        int milkCount = 0;
        int bothCount = 0;

        for (int i = 0; i < transactions.length; i++) {
            boolean milk = false;
            boolean bread = false;

            for (int j = 0; j < transactions[i].length; j++) {
                if (transactions[i][j].equals("milk")) milk = true;
                if (transactions[i][j].equals("bread")) bread = true;
            }

            if (milk) milkCount++;
            if (milk && bread) bothCount++;
        }

        double support = (double) bothCount / transactions.length;
        double confidence = (double) bothCount / milkCount;

        System.out.println("Rule: milk -> bread");
        System.out.println("Support = " + support);
        System.out.println("Confidence = " + confidence);

        if (confidence >= 0.70)
            System.out.println("Strong rule");
        else
            System.out.println("Weak rule");
    }
}