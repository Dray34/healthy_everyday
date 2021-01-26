### Github Action 自动报健康

1. fork 本项目到自己的仓库

2. 在 Settings-Secrets-Actions secrets 下添加两个变量 `ACTION_USERNAME` 和 `ACTION_PASSWORD` 分别为数字北林/校园网的账号和密码
3. 每日默认执行时间为每日9点，可以修改~/healthy_everyday.yml中的`cron`参数来修改时间（注意crontab为UTC/GMT）

本项目基于 [quaeast/healthy_everyday](https://github.com/quaeast/healthy_everyday)

