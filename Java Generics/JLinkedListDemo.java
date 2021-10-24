import java.util.*;
import static java.lang.System.out;

public class JLinkedListDemo
{
    public static void main(String[] args)
    {
        JLinkedList<Integer> list = new JLinkedList<Integer>();
        JLinkedList<Integer> list2 = new JLinkedList<Integer>();
        list.insertEnd(9);
        list.printList();
        list.insertFront(5);
        list.printList();
        list.insertEnd(10);
        list.printList();
        list.insertKey(7,5);
        list.printList();
        list.insertKey(12,0);
        list.printList();
        list.insertKey(13,10);
        list.printList();
        list.insertFront(2);
        list.printList();

        list.insertFront(1);
        list.insertFront(2);
        list.insertFront(3);
        list.insertFront(4);
        list.printList();
        list2.insertFront(5);
        list2.insertFront(6);
        list2.printList();

        list.merge(list2);
        out.println("Merged List:");
        list.printList();

        list.insertEnd(1);
        list.insertEnd(2);
        list.insertEnd(3);
        list.insertEnd(4);
        list.insertEnd(5);
        list.insertEnd(6);
        list.insertEnd(7);
        list.insertEnd(8);
        list.printList();

        list.deleteAny(4);
        list.printList();

        list.deleteFront();
        list.printList();

        list.reverse();
        

    }
}