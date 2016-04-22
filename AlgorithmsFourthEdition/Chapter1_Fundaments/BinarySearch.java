/* 需要先按照http://algs4.cs.printceton.edu/mac的指导安装好algs4，
 * 然后可以使用DrJava图形化程序来编辑、编译、运行书中的程序，
 * 也可以在任何地方使用vim编辑书中程序，使用javac-algs4编译java文件，使用java-algs4运行程序。
 * 有必要的时候需要导入algs.jar和stdlib.jar。
 *
 * 编译运行此程序需要准备largeW.txt和largeT.txt两个文件，其内容如下所示。
 * largeT.txt不是必须的，我们可以在终端输入数据即可。
 * largeW.txt(W:White):
 *  100
 *  200
 *  300
 *  400
 *  500
 *  600
 *  700
 *  800
 * largeT.txt(T:Test):
 *  100
 *  400
 *  700
 *  1000
 *
 * 编译:sudo javac-algs4 BinarySearch.java
 * 运行:sudo java-algs4 BinarySearch largeW.txt < largeT.txt
 * 输出:1000
 * 功能:BinarySearch会把largeW.txt中的数据读入存在whitelist中，然后从largeT.txt中一个一个的读入数据
 * 如果从largeT.txt中读入的数据在whitelist中存在，就不做反应，
 * 如果从largeT.txt中读入的数据在whitelist中不存在，就打印输出该数据
 */
import java.util.Arrays;
import edu.princeton.cs.algs4.*;
    
public class BinarySearch
{
    public static int rank(int key, int[] a)
    {
        int lo = 0;
        int hi = a.length - 1;
        while (lo <= hi)
        {
            int mid = lo + (hi - lo)/2;
            if (key < a[mid]) hi = mid - 1;
            else if (key > a[mid]) lo = mid + 1;
            else return mid;
        }
        return -1;
    }
    
    public static void main(String[] args)
    {
        int[] whitelist = In.readInts(args[0]);
        Arrays.sort(whitelist);
        while(!StdIn.isEmpty())
        {
            int key = StdIn.readInt();
            if (rank(key, whitelist) == -1)
                StdOut.println(key);
        }
    }
}
