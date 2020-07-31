
## 管理 已经做过的题
` find ./ -type f |grep mian| awk -F'/' '{print $NF}'|sort > ./done_.md`