import java.util.*;
import static java.lang.System.out;

public class TreeNode<T extends Comparable<T>>
{
    T element;
    TreeNode<T> left;
    TreeNode<T> right;

    public TreeNode(T o) {
        this.element = o;
        this.left = null;
        this.right = null;
    }
    public TreeNode(){
        this.element = null;
        this.left = null;
        this.right = null;
    }

    public void insert(T o){
        if(element.compareTo(o) < 0){
            if(right == null){
                right = new TreeNode<T>(o);
            }else{
                right.insert(o);
            }
        }else if(element.compareTo(o) > 0){
            if(left == null){
                left = new TreeNode<T>(o);
            }else{
                left.insert(o);
            }
        }
    }

    TreeNode delete(TreeNode root,T key){
        if(root == null)return root;

        if(root.element.compareTo(key) > 0)
        root.left = delete(root.left,key);
        else if(root.element.compareTo(key) < 0)
        root.right = delete(root.right,key);
        else{
            if(root.left == null)
            return root.right;
            else if(root.right ==null)
            return root.left;

            root.element = inSucc(root.right);

            root.right= delete(root.right,this.element);
        }
        return root;
    }

    public T inSucc(TreeNode root){
        T minv = this.element;
        while(root.left != null){
            minv = this.left.element;
            root = root.left;
        }
        return minv;
    }

    public TreeNode search(T key) {
        if(this == null){
            return null;
        }else{
            if(this.element.compareTo(key)==0)
            return this;

            if(this.element.compareTo(key)>0){
                if(this.left==null)return null;
                return this.left.search(key); }
                else{
                if(this.right==null)return null;
                return this.right.search(key);  }
        }
    }
    public void search_Result(T key){
        if(search(key)==null)
        out.println("NOT FOUND");
        else
        out.println(key+" Found");
    }

    public void inorder(TreeNode<T> R){
        if(R != null){
            inorder(R.left);
            R.visit();
            inorder(R.right);
        }
    }

    public void preorder(TreeNode<T> R){
        if(R != null){
            R.visit();
            preorder(R.left);
            preorder(R.right);
        }
    }

    public void postorder(TreeNode<T> R){
        if(R != null){
            postorder(R.left);
            postorder(R.right);
            R.visit();
        }
    }
    public void visit(){
        out.print(this.element+" ");
    }
    public static void main(String[] args){
        TreeNode<Integer> root = new TreeNode(6);
        root.insert(5);
        root.insert(7);
        root.insert(4);

        root.inorder(root);
        out.println();
        root.preorder(root);
        out.println();
        root.postorder(root);
        out.println();
        root.delete(root,5);
        root.inorder(root);
        out.println();

        root.search(7);
        root.search(12);
        root.search(-112);
    }
}