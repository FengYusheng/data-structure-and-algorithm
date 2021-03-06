## 下压栈
在应用程序中使用栈迭代器的一个典型原因是在用集合保存元素的同时**颠倒它们的相对顺序**。

## 定容栈
实现一份API的第一步就是**选择数据的表示方式**。

### 定容栈应当支持的操作

    FixCapacityStack(int cap)           #　创建一个容量为cap的空栈

    void push(String item)      　　　　 # 添加一个字符串

    String pop()                        # 删除最近添加的字符串

    boolean isEmptry()                  # 栈是否为空

    int size()                          # 栈中字符串的数量


`pop`和`push`操作所需的时间独立于栈的长度。

## 变容栈(ResizingStack)
书中说这个实现几乎（只是几乎）达到了任意集合类型数据类型的实现的最佳性能：

1. 每项操作的用时与集合大小无关(与栈的大小有关)；
2. 空间需求总是不超过集合大小乘以一个常数。

`ResizingStack`的缺点在于某些`push`和`pop`操作的耗时和栈大小成正比。


## 链表

### 链表的好处
1. 它可以处理任意类型的数据
2. 所需的空间总是和集合的大小成正比
3. 操作所需的时间总是和集合的大小无关

### 链表的插入和删除
>通过first链接访问链表的首节点，通过last链接访问链表的尾节点。

1. 在表头插入节点，所需的时间和链表长度无关。
2. 在表头删除节点，所需的时间和链表长度无关。
3. 在表尾插入节点，所需的时间和链表长度无关。
4. 删除指定节点。
5. 在指定节点前插入一个新节点。

>对于在表尾插入节点，可以借助一个指向链表最后一个节点的链接，完成这个操作。但这也增添了维护链表的难度，当链表中只有一个链表时该怎么办，当链表是一个空表时该怎么办。如何在表尾删除节点呢？last链接帮不上忙，一个解决办法就是遍历怎个链表并找出指向last的节点，但这种操作所需的时间和链表的长度成正比。**实现任意插入和删除操作的标准解决方案是使用双向链表。**


### 基本的数据结构

|数据结构 | 优点 | 缺点|
|--------|------|-----|
|数组    | 通过索引可以直接访问任意元素 | 在初始化时就需要知道元素的数量
|链表 | 使用的空间大小和元素数量成正比 | 需要通过引用访问任意元素

#### 使用数据抽象解决实际问题的步骤
1. 定义API
2. 根据特定的应用场景开发用例代码
3. **描述一种数据结构（一组值的表示），并在API所对应的抽象数据类型的实现中根据它定义类的实例变量**
4. 描述算法（实现一组操作的方式），并根据它实现类中的实例方法
5. 分析算法的性能特点

#### 本书给出的数据结构
|数据结构|章节|抽象数据类型|数据表示|
|-------|---|----------|-------|
|父链接树|1.5|UnionFind|整型数组|
|二分查找树|3.2, 3.3|BST|含有两个链接的结点|
|字符串|5.1|String|数组，偏移量和长度|
|二叉堆|2.4|PQ|对象数组|
|散列表（拉链法）|3.4|SeparateChainingHashST|链表数组|
|散列表（线性探测法）|3.4|LinearProbingHashST|链表数组|
|图的邻接链表|4.1, 4.2|Graph|Bag对象的数组|
|单词查找树|5.2|TrieST|含有链接数组的结点|
|三向单词查找树|5.3|TST|含有三个链接的结点|
