cat silver/transactions/* | sort -u | grep -v "2023-0[34]" |head -20 > gold/transactions/2023-2024.csv
