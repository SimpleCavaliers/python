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
 
 
//������ȱ���
/*
��ȣ�����ʱ���Ƚ�������ѹ��ջ���ٽ�������ѹ��ջ����ջ���ﵽ��ȱ���Ч��
*/
void depthFirstSearch(Tree root){
    stack<Node *> nodeStack;  //ʹ��C++��STL��׼ģ���
    nodeStack.push(root);
    Node *node;
    while(!nodeStack.empty()){
        node = nodeStack.top();
        printf(format, node->data);  //���������
        nodeStack.pop();
        if(node->rchild){
            nodeStack.push(node->rchild);  //�Ƚ�������ѹջ
        }
        if(node->lchild){
            nodeStack.push(node->lchild);  //�ٽ�������ѹջ
        }
    }
}
 
//������ȱ���
/*
��ʹ�����飬��ÿ��ĩβ��һ����ǣ��������õ�ʱ�����ӽڵ�Ϊ��һ��ĩβ�� 
*/
void breadthFirstSearch(Tree root){
    queue<Node *> nodeQueue;  //ʹ��C++��STL��׼ģ���
    nodeQueue.push(root);
    Node *node;
    while(!nodeQueue.empty()){
        node = nodeQueue.front();
        nodeQueue.pop();
        printf(format, node->data);  //���� 
        if(node->lchild){
            nodeQueue.push(node->lchild);  //�Ƚ����������
        }
        if(node->rchild){
            nodeQueue.push(node->rchild);  //�ٽ����������
        }
    }
}

//�ݹ�����
void dfs(Tree root) {
    if (root == nullptr) {
        return;
    }
    std::cout << root->value << ",";
    dfs(root->left);
    dfs(root->right);
} 

//�ݹ����
void  bfs(queue<Node *> nodeQueue){
	if(nodeQueue.empty())return; 
    Node *node;
    node_size = nodeQueue.size();
    while(node_size--){  //����node_size���� 
        node = nodeQueue.front();
        nodeQueue.pop();
        printf(format, node->data);  //���� 
        if(node->lchild){
            nodeQueue.push(node->lchild);  //�Ƚ����������
        }
        if(node->rchild){
            nodeQueue.push(node->rchild);  //�ٽ����������
        }
    }
} 
