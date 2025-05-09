import os
import numpy as np

input_base = '/home/methionin/CASF-2016/coreset'
output_base = '/home/methionin/CASF-2016/coreset-pdbqt'

for pdb_id in os.listdir(input_base):
    pocket_path = os.path.join(input_base, pdb_id, f'{pdb_id}_pocket.pdb')
    output_dir = os.path.join(output_base, pdb_id)
    output_path = os.path.join(output_dir, 'box_center.txt')

    coords = []
    with open(pocket_path, 'r') as f:
        for line in f:
            if line.startswith(('ATOM', 'HETATM')):
                try:
                    x = float(line[30:38])
                    y = float(line[38:46])
                    z = float(line[46:54])
                    coords.append([x, y, z])
                except ValueError:
                    continue

    if coords:
        coords = np.array(coords)
        center = coords.mean(axis=0)
        os.makedirs(output_dir, exist_ok=True)
        with open(output_path, 'w') as out:
            out.write(f'{center[0]:.3f} {center[1]:.3f} {center[2]:.3f}\n')
        print(f'[OK] {pdb_id} -> {output_path}')
    else:
        print(f'[EMPTY] No valid atoms in {pocket_path}')
