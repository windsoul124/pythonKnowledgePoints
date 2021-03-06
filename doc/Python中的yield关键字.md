# Python中的yield关键字

### 迭代的相关概念

- **迭代（iteration）**
- **可迭代的（iterable）**
- **迭代器（iterator）**
- **迭代器协议（iterator protocol）**

#### 迭代（iteration）

迭代是一种操作，很多数据都是一种容器，逐个获取容器中元素的过程就叫做迭代。

#### 可迭代的（iterable）

可迭代的是对象的一种特性，若可以从一个对象中逐个获取元素，那么称作这个对象是可迭代的。

Python中的顺序类型（`list`, `tuple`, `string`）都是可迭代的，包括`dict`, `set`, `file`也可迭代。

若用户自己实现的类型中提供了`__iter__()`或`__getitem__()`方法，也是可迭代的。

#### 迭代器（iterator）

迭代器是一种对象，迭代器抽象的是一种【数据流】，是一种只允许迭代一次的对象。对迭代器不断调用`next()`方法，则可以获取下一个元素；当迭代器中无元素时，调用`next()`则会抛出`stopIteration`异常。

迭代器的`__iter__()`会返回迭代器自身，因此迭代器也是可迭代的。

#### 迭代器协议（iterator protocol）

如果一个容器类提供了`__iter__()`方法，并且该方法可以返回一个可以逐个返回容器中元素的迭代器，那么可以称该容器类实现了迭代器协议。

Python中的迭代器协议和Python中的`for`循环是紧密相连的。

