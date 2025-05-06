# 確認すること
- バックアップ＆リストア
- ログ管理
- DBアクセス

# VM作成
## Ubuntu作成
[デプロイテンプレート](CreateVm-canonical.ubuntu-24_04-lts-server-20250216192555.json)

## Dockerインストール
```
sudo apt update
sudo apt install ca-certificates curl gnupg

sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

echo \
    "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
    $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
    sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt update

sudo groupadd docker
sudo usermod -aG docker azureuser

sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

docker --version
docker compose version
```

# DBアクセス

