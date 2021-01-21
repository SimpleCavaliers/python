#include <stdio.h>
#include <stdlib.h>
#include <malloc.h>
#include <Stack>
#include <Queue>
using namespace std;
 
typedef struct Node {
    Element data;
    struct Node *lchild;
    struct Node *rchild;
} *Tree;
 
 
//深度优先遍历
/*
深度：遍历时，先将右子树压入栈，再将左子树压入栈，弹栈；达到深度遍历效果
*/
void depthFirstSearch(Tree root){
    stack<Node *> nodeStack;  //使用C++的STL标准模板库
    nodeStack.push(root);
    Node *node;
    while(!nodeStack.empty()){
        node = nodeStack.top();
        printf(format, node->data);  //遍历根结点
        nodeStack.pop();
        if(node->rchild){
            nodeStack.push(node->rchild);  //先将右子树压栈
        }
        if(node->lchild){
            nodeStack.push(node->lchild);  //再将左子树压栈
        }
    }
}
 
//广度优先遍历
/*
若使用数组，在每行末尾加一个标记，遍历到该点时，其子节点为下一行末尾。 
*/
void breadthFirstSearch(Tree root){
    queue<Node *> nodeQueue;  //使用C++的STL标准模板库
    nodeQueue.push(root);
    Node *node;
    while(!nodeQueue.empty()){
        node = nodeQueue.front();
        nodeQueue.pop();
        printf(format, node->data);  //访问 
        if(node->lchild){
            nodeQueue.push(node->lchild);  //先将左子树入队
        }
        if(node->rchild){
            nodeQueue.push(node->rchild);  //再将右子树入队
        }
    }
}

//递归版深度
void dfs(Tree root) {
    if (root == nullptr) {
        return;
    }
    std::cout << root->value << ",";
    dfs(root->left);
    dfs(root->right);
} 

//递归版广度
void  bfs(queue<Node *> nodeQueue){
	if(nodeQueue.empty())return; 
    Node *node;
    node_size = nodeQueue.size();
    while(node_size--){  //访问node_size个。 
        node = nodeQueue.front();
        nodeQueue.pop();
        printf(format, node->data);  //访问 
        if(node->lchild){
            nodeQueue.push(node->lchild);  //先将左子树入队
        }
        if(node->rchild){
            nodeQueue.push(node->rchild);  //再将右子树入队
        }
    }
} 
