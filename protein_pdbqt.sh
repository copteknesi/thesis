#!/bin/bash

base_dir="/home/methionin/CASF-2016/coreset"
log_file="receptor_failures.log"
> "$log_file"  # eski logu temizle

find "$base_dir" -type f -name "*_protein.pdb" | while read -r pdb_file; do
    base_name="${pdb_file%.pdb}"
    echo "Processing: $pdb_file"

    if mk_prepare_receptor.py -i "$pdb_file" -o "$base_name" -p -a; then
        echo "✓ Success: $pdb_file"
    else
        echo "✗ Failed: $pdb_file" | tee -a "$log_file"
    fi
done

echo "İşlem tamamlandı. Hatalı dosyalar '$log_file' içinde listelendi."
