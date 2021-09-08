## Git报错解决：OpenSSL SSL_read:Connection was reset, errno 10054

电脑首次从github仓库clone到本地出现网络延时错误，打开SS也依然失败。

**修改HTTP的SSL认证**

`git config --global http.sslVerify "false"`

