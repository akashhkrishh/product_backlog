grep -o "Delivered" order.txt | wc -l
cut -d "|" -f1 customers.txt | sort | uniq -c | sort -nr | head -n 1
grep -i "ProductName" products.txt || echo "Product Not Found"
awk -F"|" '{sum += $5} END {if (NR > 0) print sum / NR}' products.txt
grep "ProductId" customers.txt | cut -d "|" -f1,2 | sort -t "|" -k1,1r
cut -d "|" -f1 Customers.txt | sort | uniq -c | awk '$1 == 5 {print $2}' | sort -nr

