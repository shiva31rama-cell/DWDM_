public class KMeans {
    public static void main(String[] args) {

        int[][] p = {{1,1},{2,1},{1,2},{8,8},{9,8},{8,9}};
        double aX=1, aY=1, bX=8, bY=8;

        for (int round=0; round<5; round++) {
            double ax=0, ay=0, bx=0, by=0;
            int ac=0, bc=0;

            for (int i=0; i<p.length; i++) {
                double da=(p[i][0]-aX)*(p[i][0]-aX)+(p[i][1]-aY)*(p[i][1]-aY);
                double db=(p[i][0]-bX)*(p[i][0]-bX)+(p[i][1]-bY)*(p[i][1]-bY);

                if (da <= db) {
                    ax += p[i][0]; ay += p[i][1]; ac++;
                } else {
                    bx += p[i][0]; by += p[i][1]; bc++;
                }
            }

            aX=ax/ac; aY=ay/ac;
            bX=bx/bc; bY=by/bc;
        }

        System.out.println("Cluster 1 center = (" + aX + ", " + aY + ")");
        System.out.println("Cluster 2 center = (" + bX + ", " + bY + ")");
    }
}