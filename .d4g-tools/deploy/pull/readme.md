# Content of cron file on sytem:


```bash
* * * * * /opt/d4g/<MY_REPO>/.d4g-tools/deploy/pull/pull_cron --github-token=<REDACTED> --repository-name=dataforgoodfr/<MY_REPO> --branch=dev >> /tmp/log/pull_cron.log 2>&1
```
