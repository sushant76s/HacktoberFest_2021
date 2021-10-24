import java.util.*;
import static java.lang.System.out;

public class JLinkedList<T>
{
    Node head;

    class Node{
        T data;
        Node next;

        Node(){
            data = null;
            next = null;    
        }
        Node(T d){
            data= d;
            next = null;
        }
    }
   JLinkedList(){
       head = new Node();
   }

   public void insertFront(T data){
       Node newNode = new Node(data);
       newNode.next = this.head.next;
       this.head.next = newNode;
    }

    public void insertEnd(T data){
        Node newNode = new Node(data);
        newNode.next = null;
        Node temp = this.head;
        while(temp.next != null){
            temp= temp.next;
        }
        temp.next = newNode;
    }

    public void insertKey(T data, T key){
        Node newNode = new Node(data);
        newNode.next = null;
        Node temp = this.head;
        boolean status = false;
        while(temp!=null){
        if(temp.data == key){
            status = true;
            break;
        }
        temp = temp.next;
        }
        if(status){
            newNode.next=temp.next;
            temp.next=newNode;
        }
    }
    public void printList(){
        Node currNode = this.head.next;
        out.println("Linked List: ");
        while(currNode != null){
            out.print(currNode.data+" ");
            currNode = currNode.next;
        }
        out.println();
    }
    public void merge(JLinkedList<T> l2){
        Node l1Node = this.head;
        Node l2Node = l2.head;
        while(l1Node.next != null){
            l1Node = l1Node.next;
        }
        l1Node.next = l2Node.next;
        //free(l2.head);
    }

    public void deleteFront(){
        T x = null;
        Node temp = this.head,prev= null;
        if(temp != null){
            x= temp.data;
            this.head = temp.next;
            out.println("Element Deleted");
        }
        //return x;
    }

    public T deleteEnd(){
        T x = null;
        Node temp = this.head,prev = null;
        if(temp != null){
            while(temp.next != null){
                prev = temp;
                temp = temp.next;
            }
            x= prev.next.data;
            prev.next = null;
        }
        return x;
    }

    public void deleteAny(T key){
        Node temp = this.head,prev = null;
        while(temp != null){
            if(temp.data == key){
                prev.next = temp.next;
                out.println(key+"position element deleted");
                break;
            }
            else{
                prev = temp;
                temp = temp.next;
            }
        }
    }

    public void reverse(){

        Node current = this.head.next;//out.println("Current ="+current.data);
        Node next = current.next;//out.println("Next "+next.data);
        Node prev = null;
        while(current!=null){
            next=current.next;//if(next != null)out.print(next.data+"n ");else out.print("FOOL ");
            current.next = prev;//if(current.next != null)out.print(current.next.data+"cn ");else out.print("FOOL "); 
            prev = current;//out.print(prev.data+"p ");
            current = next;//if(current != null)out.print(current.data+"cc ");else out.print("FOOL ");
           // out.println();
        }
        this.head.next=prev;

    }
}