### Github Action 自动报健康

1. fork 本项目到自己的仓库

2. 在 Settings-Secrets-Actions secrets 下添加两个变量 `ACTION_USERNAME` 和 `ACTION_PASSWORD` 分别为数字北林/校园网的 账号 和 密码
3. 每日默认执行时间为早晨9点，可以修改 [healthy_everyday.yml](https://github.com/Supremesir/healthy_everyday/blob/action/.github/workflows/healthy_everyday.yml) 中的 `cron` 参数来修改时间（注意 crontab 为 UTC/GMT）

本项目基于 [quaeast/healthy_everyday](https://github.com/quaeast/healthy_everyday)

