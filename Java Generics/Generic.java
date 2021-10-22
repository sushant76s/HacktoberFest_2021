import java.util.*;
import static java.lang.System.out;

public class Generic
{
    // Defining a generic method to print any datatype
   static <T> void genericPrint(T t){
        out.println(t);
    }

    public static void main(String[] args)
    {
        //Generic obj = new Generic();
        genericPrint(3);
        genericPrint(3.14);
        genericPrint("Hello World!");     
    }
}

