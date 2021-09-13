## Git报错解决：OpenSSL SSL_read:Connection was reset, errno 10054

Git操作出现网络错误，通过代理也无法解决。

**修改HTTP的SSL认证**

`git config --global http.sslVerify "false"`

