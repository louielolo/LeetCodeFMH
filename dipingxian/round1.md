2021/07/09 卢彦廷 lu.yanting@qq.com
1、项目介绍
2、对方介绍了应用软件部门的组成:算法后处理+嵌入式软件架构+可视化客户端+devops
3、沟通了意向


1.	给定一个非空的整数数组，每一个元素都出现两次，只有一个元素出现一次，找出出现一次的那个元素为何？时间复杂度限制为O(n)，并且能不能不使用额外的内存来完成?
范例1.
Input: [2,2,1]
Output: 1
范例2.
	Input: [4,1,2,1,2]
Output: 4
class Solution:
	def findOnce(self,arr:list)->int:
  	dict_test = {}
  	'''找到只出现一次的元素'''
    #元素去重
  	setArr = set(arr)
    #将元素与次数存入字典
    for i in setArr:
    	dict_test[i] = arr.count(i)
    return [k for k,v in dict_test.items() if v == 1]

2.	实现void *memcpy(void *dest, const void *src, size_t n)或char *strcpy(char *dest, const char *src)
python str.deepcopy()
思路：
class deepcopy:
	@classmethod
  def basicTypeCpy(cls,src):
  #基本类型的拷贝
  if isinstance(src,'int') or isinstance(src,'str') or isinstance(src,'double):
  	instance = cls.copy(src)
  return instance
  @classmethod
  def listCpy(cls,src)
  if isinstace(src,'list'):
  	instance = cls.copy(src)
  return instance
  @classmethod
  def dictCpy(cls,src)
  if isinstance(src,'dict')
  	instance = cls.copy(src)
  return instance
  @classmethod
  def tupleCpy(cls,src)
  ...
  @clasmethod
  def setCpy(cls,src)
  
3.	二叉树的节点定义如下，请实现一个中序/前序/后序遍历这个二叉树 （任一即可）
struct TreeNode
{
  int val;
  TreeNode* left;
  TreeNode* right;
};

def dlr(node:Treenode):
	if node is None:
  	return node
  print(node.val)
  dlr(node.left)
  dlr(node.right)
  return