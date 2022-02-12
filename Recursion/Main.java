import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        ArrayList<Integer> A = new ArrayList<>() {
            {
            add(3);
            add(5);
            add(9);
            }
        };
        ArrayList<Integer> B = new ArrayList<>() {
            {
            add(4);
            add(6);
            add(8);
            }
        };
        System.out.println(mergeSortedArrays(A, B));
    }
    
    static void pattern(int n) {
        if (n==0) return;
        helper(n);
        System.out.print("\n");
        pattern(--n);
    }

    static void helper(int n) {
        if (n==0) return;
        System.out.print("*");
        helper(--n);
    }

    static void pattern(int r, int c) {
        if (r==0) return;
        if (r == c) {
            pattern(--r, 0);
            System.out.println();
            return;
        }
        pattern(r, ++c);
        System.out.print("*");
    }

    static void pattern(int r, int c, int N) {
        if (N==0) return;
        if (c == N) {
            System.out.println();
            pattern(++r, 0, --N);
            return;
        }
        System.out.print("*");
        pattern(r, ++c, N);
    }

    static int[] bubbleSort(int A[], int i, int N) {
        if (N==0) return A;
        if (i == N) {
            return bubbleSort(A, 0, --N);
        }
        if (A[i] > A[i+1]) {
            int temp = A[i];
            A[i] = A[i+1];
            A[i+1] = temp;
        }
        return bubbleSort(A, ++i, N);
    }

    static int[] selectionSort(int A[], int i, int j) {
        if (i == A.length-1) return A;
        if (j == A.length) return selectionSort(A, ++i, i+1);
        if (A[i] > A[j]) {
            int temp = A[i];
            A[i] = A[j];
            A[j] = temp;
        }
        return selectionSort(A, i, ++j);
    }

    static ArrayList<Integer> mergeSort(ArrayList<Integer> arr) {
        if (arr.size() == 1) return arr;
        int mid = arr.size()/2;
        ArrayList<Integer> left = mergeSort(arr, 0, mid)
    }

    static ArrayList<Integer> mergeSortedArrays(ArrayList<Integer> A, ArrayList<Integer> B) {
        int i = 0;
        int j = 0;
        ArrayList<Integer> res = new ArrayList<>();
        while (i < A.size() && j < B.size()) {
            if (A.get(i) > B.get(j)) {
                res.add(B.get(j));
                j++;
            } else {
                res.add(A.get(i));
                i++;
            }
        }
        while (i < A.size()) {
            res.add(A.get(i));
            i++;
        }
        while (j < B.size()) {
            res.add(B.get(j));
            j++;
        }
        return res;
    }
}