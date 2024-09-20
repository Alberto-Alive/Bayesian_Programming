class RedBlackTree {
    private static final boolean RED = true;
    private static final boolean BLACK = false;

    class Node {
        int key;
        Node left, right, parent;
        boolean color;

        public Node(int key) {
            this.key = key;
            left = right = parent = null;
            color = RED;  // New nodes are always red initially
        }
    }

    private Node root;

    // Left Rotate
    private void leftRotate(Node x) {
        Node y = x.right; // Node y = 20
        x.right = y.left; // 20 = null
        if (y.left != null) y.left.parent = x;
        y.parent = x.parent;
        if (x.parent == null) root = y;
        else if (x == x.parent.left) x.parent.left = y;
        else x.parent.right = y;
        y.left = x;
        x.parent = y;
    }

    // Right Rotate
    private void rightRotate(Node y) {
        Node x = y.left;
        System.out.println("Node x: " + x);
        y.left = x.right;
        if (x.right != null) x.right.parent = y;
        x.parent = y.parent;
        if (y.parent == null) root = x;
        else if (y == y.parent.left) y.parent.left = x;
        else y.parent.right = x;
        x.right = y;
        y.parent = x;
    }

    // Fix Red-Black Tree violations
    private void fixInsert(Node k) {
        while (k.parent != null && k.parent.color == RED) {
            if (k.parent == k.parent.parent.left) {
                Node uncle = k.parent.parent.right;
                if (uncle != null && uncle.color == RED) {
                    // Case 1: Uncle is red
                    k.parent.color = BLACK;
                    uncle.color = BLACK;
                    k.parent.parent.color = RED;
                    k = k.parent.parent;
                } else {
                    // Case 2: Uncle is black (rotation)
                    if (k == k.parent.right) {
                        k = k.parent;
                        leftRotate(k);
                    }
                    k.parent.color = BLACK;
                    k.parent.parent.color = RED;
                    rightRotate(k.parent.parent);
                }
            } else {
                Node uncle = k.parent.parent.left;
                if (uncle != null && uncle.color == RED) {
                    // Mirror case 1
                    k.parent.color = BLACK;
                    uncle.color = BLACK;
                    k.parent.parent.color = RED;
                    k = k.parent.parent;
                } else {
                    // Mirror case 2
                    if (k == k.parent.left) {
                        k = k.parent;
                        rightRotate(k);
                    }
                    k.parent.color = BLACK;
                    k.parent.parent.color = RED;
                    leftRotate(k.parent.parent);
                }
            }
        }
        root.color = BLACK;
    }

    // Insert a new node
    public void insert(int key) {
        Node node = new Node(key);
        if (root == null) {
            root = node;
            root.color = BLACK;  // Root must always be black
            return;
        }

        Node temp = root;
        Node parent = null;
        while (temp != null) {
            parent = temp;
            if (key < temp.key) temp = temp.left;
            else temp = temp.right;
        }

        node.parent = parent;
        if (key < parent.key) parent.left = node;
        else parent.right = node;

        fixInsert(node);
    }

    // In-order traversal for checking the tree
    public void inOrder(Node node) {
        if (node != null) {
            inOrder(node.left);
            System.out.print(node.key + " (" + (node.color == RED ? "Red" : "Black") + ") ");
            inOrder(node.right);
        }
    }

    public Node getRoot() {
        return root;
    }

    public static void main(String[] args) {
        RedBlackTree rbt = new RedBlackTree();
        rbt.insert(10);
        rbt.insert(20);
        rbt.insert(30);
        rbt.inOrder(rbt.getRoot());
    }
}
