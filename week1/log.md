1.首先使用utf-8编码时，有抛出异常

> UnicodeEncodeError: ‘ascii’ codec can’t encode characters in position 0-78: ordinal not in range(128)

使用[这里](http://wangye.org/blog/archives/629/)来解决编码的问题
由于时python2.7.6内部编码时ascii码，我们就将内部编码改为后来的utf-8就好了。
在开头加上一句就好了。
{% highlight python %}
import sys
reload(sys)
sys.setdefaultencoding(‘utf-8’)
{% endhighlight %}


2.URL 和 URI


