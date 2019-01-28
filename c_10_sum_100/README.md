见原贴： https://segmentfault.com/q/1010000017987193 ， 问题题意可能有争议。取这样的理解：
从1-100中选择10个数，满足10个数之和等于100，问这样的组合有多少个？打印出所有的组合。

c1.py 为我的代码
c2.py 为dodopy的代码
test.py为验证答案脚本，验证：1.每个解的和都是100； 2.每个解的唯一性，和每个解中元素的唯一性
使用方法：

```shell
./c1.py > result.txt
./test.py result.txt
Pass check sum test
Pass check uniq test
```
