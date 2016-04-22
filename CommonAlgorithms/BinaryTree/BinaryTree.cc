/* LeetCode 337是一道关于二叉树的题，所以在这里先研究一下二叉树的知识
 * 
 * 参考：
 *     http://blog.csdn.net/fansongy/article/details/6798278
 *     http://noalgo.info/832.html
 * 
 * Morris实现前序遍历、中序遍历、后序遍历没有写
 * 层次遍历没有写
 * 前序遍历、中序遍历，求后序遍历没有写
 * 由前序遍历生成二叉树没有写
 * 求二叉树的节点个数没有写
 * 二叉树查找没有写
 * 二叉树生成平衡二叉树没有写
 *
 * mac下编译命令：sudo gcc BinaryTree.cc -lstdc++
 */

#include <cstdio>
#include <stack>
using namespace std;

struct Node {
    int val;
    Node *left, *right;
    //《C++ Primer》（第五版）p237:构造函数初始值列表
    Node(int v = 0, Node *l = NULL, Node *r = NULL): val(v), left(l), right(r) {}
};

// 递归实现前序遍历
void preorderRecursion(Node *root) {
    if (root == NULL) return;
    printf("%d ", root->val);
    preorderRecursion(root->left);
    preorderRecursion(root->right);
}

// 递归实现中序遍历
void inorderRecursion(Node *root) {
    if (root == NULL) return;
    inorderRecursion(root->left);
    printf("%d ", root->val);
    inorderRecursion(root->right);
}

// 递归实现后序遍历
void postorderRecursion(Node *root) {
    if (root == NULL) return;
    postorderRecursion(root->left);
    postorderRecursion(root->right);
    printf("%d ", root->val);
}

// 栈模拟，非递归算法实现前序遍历
void preorderStack(Node *root) {
    if (root == NULL) return;

    stack<Node *> stk;
    stk.push(root);
    while (!stk.empty()) {
        Node *p = stk.top(); stk.pop();
        printf("%d ", p->val);
        if (p->right) stk.push(p->right);
        if (p->left) stk.push(p->left);
    }
}

// 栈模拟，非递归算法实现中序遍历
void inorderStack(Node *root) {
    stack<Node *> stk;
    Node *p = root;
    while (p != NULL || !stk.empty()) {
        if (p != NULL) {
            stk.push(p); p = p->left;
        } else {
            p = stk.top(); stk.pop();
            printf("%d ", p->val);
            p = p->right;
        }
    }
}

// 栈模拟，非递归算法实现后序遍历
void postorderStack(Node *root) {
    if (root == NULL) return;
    stack<Node *> stk,stkBak;
    stk.push(root);
    while (!stk.empty()) {
        Node *p = stk.top(); stk.pop();
        stkBak.push(p);
        if (p->left) stk.push(p->left);
        if (p->right) stk.push(p->right);
    }
    while (!stkBak.empty()) {
        Node *p = stkBak.top(); stkBak.pop();
        printf("%d ", p->val);
    }
}

// 递归算法求二叉树的高度
int height(Node *root) {
    if (root == NULL) return 0;
    int h, left, right;
    left = height(root->left);
    right = height(root->right);
    h = ((left > right)?left:right) + 1;
    return h;
}

int main() {
    Node a1(1), a3(3), a5(5), a7(7);
    Node a2(2, &a1, &a3), a6(6, &a5, &a7);
    Node a4(4, &a2, &a6);

    printf("递归实现前序遍历:"); preorderRecursion(&a4); printf("\n");
    printf("递归实现中序遍历:"); inorderRecursion(&a4); printf("\n");
    printf("递归实现后序遍历:"); postorderRecursion(&a4); printf("\n");

    printf("栈模拟实现前序遍历:"); preorderStack(&a4); printf("\n");
    printf("栈模拟实现中序遍历:"); inorderStack(&a4); printf("\n");
    printf("栈模拟实现后序遍历:"); postorderStack(&a4); printf("\n");

    printf("递归算法求二叉树的高度:");printf("%d\n", height(&a4));
}
