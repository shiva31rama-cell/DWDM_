import java.util.*;

public class Apriori {
    static List<Set<String>> transactions = Arrays.asList(
        new HashSet<>(Arrays.asList("milk", "bread", "eggs")),
        new HashSet<>(Arrays.asList("milk", "bread")),
        new HashSet<>(Arrays.asList("milk", "eggs")),
        new HashSet<>(Arrays.asList("bread", "eggs")),
        new HashSet<>(Arrays.asList("milk", "bread", "eggs"))
    );

    static double support(Set<String> itemset) {
        int count = 0;
        for (Set<String> t : transactions)
            if (t.containsAll(itemset)) count++;
        return (double) count / transactions.size();
    }

    public static void main(String[] args) {
        double minSupport = 0.6;
        Set<String> allItems = new TreeSet<>();
        for (Set<String> t : transactions) allItems.addAll(t);

        List<Set<String>> current = new ArrayList<>();
        for (String item : allItems)
            current.add(new TreeSet<>(Collections.singleton(item)));

        while (!current.isEmpty()) {
            List<Set<String>> frequent = new ArrayList<>();
            for (Set<String> itemset : current) {
                if (support(itemset) >= minSupport) {
                    frequent.add(itemset);
                    System.out.printf("%s support=%.2f%n", itemset, support(itemset));
                }
            }

            Set<Set<String>> next = new HashSet<>();
            for (int i = 0; i < frequent.size(); i++) {
                for (int j = i + 1; j < frequent.size(); j++) {
                    Set<String> union = new TreeSet<>(frequent.get(i));
                    union.addAll(frequent.get(j));
                    if (union.size() == frequent.get(i).size() + 1)
                        next.add(union);
                }
            }
            current = new ArrayList<>(next);
        }
    }
}