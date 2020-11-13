//两种非递归遍历树的代码风格统一方法

//1.标识遍历法，就是要处理的并入堆栈之后，紧接着放入一个空指针作为标记。
//此方法适合前中后遍历，通用
//中
public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        Deque<TreeNode> stack = new LinkedList<>();
        if(root!=null) stack.push(root);
        while(!stack.isEmpty()){
            TreeNode node = stack.pop();
            if(node!=null){
                if(node.right!=null) stack.push(node.right);//右，注意此处是先把右结点压栈，先进后出
                stack.push(node);//中
                stack.push(null);//标记
                if(node.left!=null) stack.push(node.left);//左
            }else{// 只有遇到空节点的时候，才将下一个节点放进结果集
                node=stack.pop();
                res.add(node.val);
            }      
        }
        return res;
    }
//前
public List<Integer> preorderTraversal(TreeNode root) {
        //统一风格迭代
        List<Integer> res = new ArrayList<>();
        Deque<TreeNode> stack = new LinkedList<>();
        if(root!=null) stack.push(root);
        while(!stack.isEmpty()){
            TreeNode node = stack.pop();
            if(node!=null){
                if(node.right!=null) stack.push(node.right);
                if(node.left!=null) stack.push(node.left);
                stack.push(node);
                stack.push(null);
            }else{
                node=stack.pop();
                res.add(node.val);
            }
        }
        return res;
}
//后
public List<Integer> postorderTraversal(TreeNode root) {
        //统一风格迭代
        List<Integer> res = new ArrayList<>();
        Deque<TreeNode> stack = new LinkedList<>();
        if(root!=null) stack.push(root);
        while(!stack.isEmpty()){
            TreeNode node = stack.pop();
            if(node!=null){
                stack.push(node);
                stack.push(null);
                if(node.right!=null) stack.push(node.right);
                if(node.left!=null) stack.push(node.left);
            }else{
                node=stack.pop();
                res.add(node.val);
            }
        }
        return res;
}
//2.根据第几个遇见结点的继承
//此方法只适合前中遍历，后遍历用此框架需要额外添加一个pre前驱来判断是不是第三次访问此例程

//中
	List<Integer> res = new ArrayList<>();
        Deque<TreeNode> stack = new LinkedList<>();
        while(root!=null||!stack.isEmpty()){
            while(root!=null){
                stack.push(root);//第一次遇见
                root=root.left;
            }
            root = stack.pop();//第二次遇见
            res.add(root.val);
            root=root.right;
        }
        return res;
//前
	List<Integer> res = new ArrayList<>();
        Deque<TreeNode> stack = new LinkedList<>();
        while(root!=null||!stack.isEmpty()){
            while(root!=null){
                stack.push(root);//第一次遇见
		res.add(root.val);//入res
                root=root.left;
            }
            root = stack.pop();//第二次遇见
            root=root.right;
        }
        return res;
//后，加一个pre判断是不是第三次
	List<Integer> res = new ArrayList<>();
        Deque<TreeNode> stack = new LinkedList<>();
        TreeNode pre = null;
        while(root!=null||!stack.isEmpty()){
            while(root!=null){
                stack.push(root);//第一次遇见
                root=root.left;
            }
            root = stack.pop();
		/*1，如果right为null代表无right，既此结点为叶子结点，则此次是第三次访问，
		2.或者在有右孩子的时候，right==pre，代表访问过了右孩子，所以这是第三次访问*/
            if(root.right==null||root.right==pre){
                res.add(root.val);
                pre = root;
                root = null;
            }else{//第二次
                stack.push(root);//因为是第二次访问，没到访问的时候，所以放回栈内
                root = root.right;
            }
        }
        return res;
