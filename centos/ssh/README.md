# centos7 ssh

## 方式一：运行 centos 后手动安装

centos7-manual

```cmd
yum install -y initscripts openssh-server openssl openssl-devel passwd openssh-clients
yum install -y vim passwd net-tools wget

ssh-keygen -A

passwd root

echo "123456" | passwd --stdin root

systemctl start sshd.service
systemctl enable sshd.service
systemctl status sshd.service
```

## 方式二：运行 centos 后自动安装

centos7-auto

## 测试

```
ssh -p 1022 root@127.0.0.1
ssh -p 2022 root@127.0.0.1
```

## 其他

```cmd
docker run -d -name centos7 --privileged=true centos:7 /usr/sbin/init

docker commit <容器ID> myimage/centos7-ssh
```

如果下载不了 systemctl，则使用 data 中的

```
wget https://raw.githubusercontent.com/gdraheim/docker-systemctl-replacement/master/files/docker/systemctl.py -O /bin/systemctl
修改为
cp /opt/data/systemctl /bin/systemctl
```

## QA

Failed to get D-Bus connection: Operation not permitted

https://zhuanlan.zhihu.com/p/648578218

```cmd
yum install -y wget
wget https://raw.githubusercontent.com/gdraheim/docker-systemctl-replacement/master/files/docker/systemctl.py -O /bin/systemctl
chmod a+x /bin/systemctl
```
