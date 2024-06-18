# Install gum
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://repo.charm.sh/apt/gpg.key | sudo gpg --dearmor -o /etc/apt/keyrings/charm.gpg
echo "deb [signed-by=/etc/apt/keyrings/charm.gpg] https://repo.charm.sh/apt/ * *" | sudo tee /etc/apt/sources.list.d/charm.list
sudo apt update && sudo apt install gum


# Content of cron file on sytem:


```bash
* * * * * /opt/d4g/<MY_REPO>/.d4g-tools/deploy/pull/pull_cron --github-token=<REDACTED> --repository-name=dataforgoodfr/<MY_REPO> --branch=dev >> /tmp/log/pull_cron.log 2>&1
```
