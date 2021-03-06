#!/usr/bin/python
# -*- coding: UTF-8 -*-
#from pythonds.basic.stack import Stack
# from pythonds.self.trees.binaryTree import BinaryTree

# def printTree(self.tree):
#     print "%s,"%self.tree.getRootVal()
#     lchild = self.tree.getLeftChild()
#     rchild = self.tree.getRightChild()
#     if lchild is not None:
#         printTree(lchild)
#     if rchild is not None:
#         printTree(rchild)

class miniHeap():
    tree = []
    def __init__(self,maxSize = 10):
        self.maxSize = maxSize
        # self.root = BinaryTree(rootValue)
        self.crtSize = 0

    def leftChild(self,curPos):
        return (((curPos+1)*2-1) if ((curPos+1)*2-1)<self.crtSize else -1)

    def rightChild(self,curPos):
        return (((curPos+1)*2) if ((curPos+1)*2)<self.crtSize else -1)

    def parent(self,curPos):
        return (((curPos+1)/2-1) if curPos>0 else -1)

    def dataUp(self,curPos):
        parent = self.parent(curPos)
        if parent<>-1:
            left = self.leftChild(parent)
            right = self.rightChild(parent)
            if self.tree[parent]>self.tree[curPos]:
                self.tree[parent],self.tree[curPos] = self.tree[curPos],self.tree[parent]
                if (curPos == left):
                    if self.tree[parent]>self.tree[right]:
                        self.tree[right],self.tree[parent] = self.tree[parent],self.tree[right]
                else:
                    if self.tree[parent]>self.tree[left]:
                        self.tree[left],self.tree[parent] = self.tree[parent],self.tree[left]
                # self.dataDown(parent)
                self.dataUp(parent)

    def dataDown(self,curPos):
        # print curPos
        targetPos = curPos
        left = self.leftChild(curPos)
        right = self.rightChild(curPos)
        # print curPos,left,right,self.crtSize
        if left<>-1 and right<>-1:
            if self.tree[curPos]>self.tree[left] and self.tree[curPos]>self.tree[right]:
                if self.tree[right]>self.tree[left]:
                    targetPos = left
                else:
                    targetPos = right
            elif self.tree[curPos]>self.tree[left]:
                targetPos = left
            elif self.tree[curPos]>self.tree[right]:
                targetPos = right
            else:
                targetPos=-1
        elif left<>-1:
            if self.tree[curPos]>self.tree[left]:
                targetPos = left
            else:
                targetPos=-1
        else:
            targetPos=-1
        if targetPos<>-1:
            self.tree[targetPos],self.tree[curPos] = self.tree[curPos],self.tree[targetPos]
            self.dataDown(targetPos)
        else:
            pass
        return

    def dataInsert(self,value):
        if self.crtSize==self.maxSize:
            if self.tree[0]<value:
                self.tree[0]=value
                self.dataDown(0)
        else:
            print self.crtSize,value
            self.tree.append(value)
            self.crtSize+=1
            self.dataUp(self.crtSize-1)
        print self.tree

    def sort(self):
        rstList = []
        # target = self.tree
        # targetSize = self.crtSize
        while self.crtSize>1:
            rstList.append(self.tree[0])
            self.tree[0]=self.tree[self.crtSize-1]
            self.crtSize=self.crtSize-1
            self.dataDown(0)
        if self.crtSize == 1:
            rstList.append(self.tree[0])
            self.crtSize=self.crtSize-1
        return rstList

def main(testList,maxSize = 10):
    # print testList[0]
    test = miniHeap(maxSize)
    for testV in testList:
        test.dataInsert(testV)
    print test.sort()
    # print test.tree
    # printTree(test.root)

if __name__ == '__main__':
    testList =[9,8,7,15,5,6,4,3,2,1,10,11,12]
    maxSize = 10
    main(testList,maxSize)