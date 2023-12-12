
dir=raw/transactions
file=${dir}/`date '+%Y-%m-%d'`.json
echo ${file}

curl 'https://www.fleaflicker.com/api/FetchLeagueTransactions?sport=NHL&league_id=15754' > ${file}

ls -l $dir


