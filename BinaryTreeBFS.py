import logging
from collections import deque

logging.basicConfig(level=logging.DEBUG)


class Tree:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None


def buildMidTree(lis: list, start: int, end: int) -> Tree:
    """
    中序构造二叉树，先构造左边的子树，然后依次返回上级节点构造右边子树
    :param lis: 数据
    :param start: 从 lis 的第 start 节点开始
    :param end: 从 lis 的第 end 节点结束
    :return: 根节点
    """
    # root = None
    if end >= start:
        root = Tree()
        mid = (start + end + 1) // 2
        root.data = lis[mid]
        root.left = buildMidTree(lis, start, mid - 1)
        root.right = buildMidTree(lis, mid + 1, end)
    else:
        root = None
    return root


def bfsTree(root: Tree):
    """
    BFS 方式打印每层存储的值 ----> 循环方式
    :param root:
    :return:
    """
    if root == None:
        logging.debug("None")
    queue = deque()
    queue.append(root)
    while len(queue) > 0:
        # 弹出首节点
        cur = queue.popleft()
        logging.debug(cur.data)
        #
        if cur.left != None:
            queue.append(cur.left)
        if cur.right != None:
            queue.append(cur.right)


def pre(root: Tree, lis=[]):
    """
    前序遍历：先访问根节点，然后递归访问左子树，再递归访问右子树
    即实现    根->左->右   的访问顺序
    递归方法
    因为使用递归，所以每一个子树都实现了这样的顺序。
    :param root:
    :return:
    """
    if root == None:
        return
    lis.append(root.data)
    pre(root.left, lis)
    pre(root.right, lis)
    return lis


def mid(root: Tree, lis=[]):
    """
    左->根->右 的访问顺序 遍历 二叉树
    如果二叉树是中序构造的，则恰好能返回原始的数组顺序
    递归方式
    :param root:
    :return:
    """
    if root == None:
        return
    mid(root.left, lis)
    lis.append(root.data)
    mid(root.right, lis)
    return lis


def aft(root: Tree, lis=[]):
    """
    对于后序遍历，就是先访问左子树，再访问右子树，再访问根节点
    左->右->根
    递归方式
    :param root:
    :return:
    """
    if root == None:
        return
    aft(root.left, lis)
    aft(root.right, lis)
    lis.append(root.data)
    return lis


if __name__ == "__main__":
    lis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    root = buildMidTree(lis, 0, len(lis) - 1)

    logging.debug("BFS search")
    bfsTree(root)

    logging.debug("pre search")
    lis = pre(root)
    logging.debug(lis)

    logging.debug("Mid search")
    lis = mid(root)
    logging.debug(lis)

    logging.debug("aft search")
    lis = aft(root)
    logging.debug(lis)
