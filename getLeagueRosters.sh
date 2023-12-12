
dir=raw/rosters
mkdir -p $dir
file=${dir}/`date '+%Y-%m-%d'`.json
echo ${file}

curl 'https://www.fleaflicker.com/api/FetchLeagueRosters?sport=NHL&league_id=15754' > ${file}

ls -l $dir


