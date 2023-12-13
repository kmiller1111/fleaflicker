
dir=raw/transactions

#curl 'https://www.fleaflicker.com/api/FetchLeagueTransactions?sport=NHL&league_id=15754' > ${file}

for i in {0..49}; do
   offset=$(( i * 30 ))
   file=${dir}/`date '+%Y-%m-%d'`.$i.json
   echo "${file}   $offset"
   curl "https://www.fleaflicker.com/api/FetchLeagueTransactions?sport=NHL&league_id=15754&result_offset=${offset}" > ${file}
done

ls -l $dir


