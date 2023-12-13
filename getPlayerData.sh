
cnt=${1:-5}    

dir="raw/player"

mkdir -p ${dir}


#curl 'https://www.fleaflicker.com/api/FetchPlayerListing?sport=NHL&league_id=15754&result_offset=0' > ${file}

for (( i = 0; i < $cnt; i++ )); do  
   offset=$(( i * 30 ))
   file=${dir}/`date '+%Y-%m-%d'`.$i.json
   echo "${file}   $offset"
   curl "https://www.fleaflicker.com/api/FetchPlayerListing?sport=NHL&league_id=15754&result_offset=${offset}" > ${file}
done
