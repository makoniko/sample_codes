# AWS EC2インスタンスを用意
- Ubuntu 22.04を使用
- ユーザ「ubuntu」で作業

# SSH接続
```
ssh aws_minikube
```

# kubectlインストール
参考
https://hombre-nuevo.com/workefficiency/docker/k8s0002/

```
curl -LO "https://dl.k8s.io/release/$(curl -LS https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x ./kubectl
sudo mv ./kubectl /usr/local/bin/kubectl
```

```
$ kubectl version --client
Client Version: v1.33.4
Kustomize Version: v5.6.0
```

# ubuntuアップデート & Dockerインストール
```
sudo apt-get update && sudo apt-get install docker.io -y
```

```
$ docker -v
Docker version 27.5.1, build 27.5.1-0ubuntu3~22.04.2
```

# minikubeインストール

```
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
```

```
$ minikube version
minikube version: v1.36.0
commit: f8f52f5de11fc6ad8244afac475e1d0f96841df1-dirty
```

# crictlインストール
https://github.com/kubernetes-sigs/cri-tools/releases
上記からcrictlの最新バージョンを確認し、下記スクリプトの変数を適宜変更する。

```
VERSION="v1.33.0"
wget https://github.com/kubernetes-sigs/cri-tools/releases/download/$VERSION/crictl-$VERSION-linux-amd64.tar.gz
sudo tar zxvf crictl-$VERSION-linux-amd64.tar.gz -C /usr/local/bin
rm -f crictl-$VERSION-linux-amd64.tar.gz
```

# cri-dockerdインストール

```
sudo add-apt-repository ppa:longsleep/golang-backports
sudo apt update
sudo apt install golang

git clone https://github.com/Mirantis/cri-dockerd.git 
cd cri-dockerd
mkdir bin
go build -o bin/cri-dockerd # ここ対応中
mkdir -p /usr/local/bin
sudo install -o root -g root -m 0755 bin/cri-dockerd /usr/local/bin/cri-dockerd
sudo cp -a packaging/systemd/* /etc/systemd/system
sudo sed -i -e 's,/usr/bin/cri-dockerd,/usr/local/bin/cri-dockerd,' /etc/systemd/system/cri-docker.service
sudo systemctl daemon-reload 
sudo systemctl enable cri-docker.service
sudo systemctl enable --now cri-docker.socket
```

# containernetworking-pluginsインストール
https://github.com/containernetworking/plugins/releases
上記からcontainernetworking-pluginsの最新バージョンを確認し、下記スクリプトの変数を適宜変更する。

```
CNI_PLUGIN_VERSION="v1.7.1"
CNI_PLUGIN_TAR="cni-plugins-linux-amd64-$CNI_PLUGIN_VERSION.tgz" # change arch if not on amd64
CNI_PLUGIN_INSTALL_DIR="/opt/cni/bin"

curl -LO "https://github.com/containernetworking/plugins/releases/download/$CNI_PLUGIN_VERSION/$CNI_PLUGIN_TAR"
sudo mkdir -p "$CNI_PLUGIN_INSTALL_DIR"
sudo tar -xf "$CNI_PLUGIN_TAR" -C "$CNI_PLUGIN_INSTALL_DIR"
rm "$CNI_PLUGIN_TAR"
```

# conntrackインストール

```
sudo apt install conntrack -y
```

# minikube起動

```
sudo minikube start --vm-driver=none
```

```
$ sudo minikube status
minikube
type: Control Plane
host: Running
kubelet: Running
apiserver: Running
kubeconfig: Configured
```
