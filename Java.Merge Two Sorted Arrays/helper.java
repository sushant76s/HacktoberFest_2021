public class helper {
    static void outputArray(int[] array) {
        if (array == null)
            return;

        StringBuilder strB = new StringBuilder();

        for (int i : array) {
            if (strB.length() > 0)
                strB.append(',');
            
            strB.append(i);
        }

        System.out.println("[" + strB.toString() + "]");
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
    
        int[] A = {1, 2, 3, 4};
        int[] B = {2, 4, 5, 6};
    
        helper.outputArray(solution.mergeSortedArray(A, B));
    }
}
