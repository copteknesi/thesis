find /home/methionin/CASF-2016/coreset -type f -name "*_ligand.mol2" | while read mol2_file; do
    pdbqt_file="${mol2_file%.mol2}.pdbqt"
    mk_prepare_ligand.py -i "$mol2_file" -o "$pdbqt_file"
done
