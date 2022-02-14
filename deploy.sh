expect -c "
set timeout 1
spawn scp -P 22 ./* ns2pole@202.181.99.56:www/app
spawn scp -r ./templates ns2pole@202.181.99.56:www/app
spawn scp -r ./static ns2pole@202.181.99.56:www/app
expect \"password:\"
send \"fek9urz3fb\n\"
interact
"
