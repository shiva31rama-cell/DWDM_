import java.util.HashSet;
import java.util.Random;
import java.util.Set;

public class SimulatedDataset {
    public static void main(String[] args) {
        int numberOfInstances = 10;
        int generated = 0;
        Random random = new Random(42);
        Set<String> uniqueInstances = new HashSet<>();

        while (generated < numberOfInstances) {
            int age = 18 + random.nextInt(43);
            int score = 40 + random.nextInt(61);
            String instance = age + "," + score;

            if (uniqueInstances.add(instance)) {
                generated++;
                System.out.println("Instance " + generated + ": " + instance);
            }
        }

        System.out.println("Total unique instances = " + uniqueInstances.size());
    }
}