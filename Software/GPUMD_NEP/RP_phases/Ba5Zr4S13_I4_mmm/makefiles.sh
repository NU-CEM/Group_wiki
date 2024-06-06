mkdir pbesol_BS
cd pbesol_BS
cp ../geometry.in.next_step geometry.in
cp ../run.slm .
cp ../control.in .
sed -i '/relax_/d' control.in
sed -i '/sc_accuracy_forces/d' control.in
sed -i '/sc_accuracy_rho       1E-7/a include_spin_orbit\noutput band   0.00000  0.00000  0.00000  -0.50000  0.50000  0.00000   46 G  X\n output band  -0.50000  0.50000  0.00000  -0.50000  0.50000 -0.05002    5 X  Y\n   output band  -0.50000  0.50000 -0.05002  -0.27501  0.27501 -0.27501   29 Y  S\n output band  -0.27501  0.27501 -0.27501   0.00000  0.00000  0.00000   36 S  G\n output band   0.00000  0.00000  0.00000   0.50000  0.50000 -0.50000   21 G  Z\n output band   0.50000  0.50000 -0.50000   0.27501  0.72499 -0.72499   29 Z  S1\n output band   0.27501  0.72499 -0.72499   0.00000  0.50000 -0.50000   11 S1 N\n output band   0.00000  0.50000 -0.50000  -0.25000  0.75000 -0.25000   33 N  P\n output band  -0.25000  0.75000 -0.25000   0.05002  0.94998 -0.50000   11 P  Y1\n output band   0.05002  0.94998 -0.50000   0.50000  0.50000 -0.50000   41 Y1 Z\n output band  -0.50000  0.50000  0.00000  -0.25000  0.75000 -0.25000   10 X  P\n output dos                         -10 10 51 0.1\n' control.in
sbatch run.slm

cd ../
mkdir pbe_BS
cd pbe_BS
cp ../geometry.in.next_step geometry.in
cp ../run.slm .
cp ../pbesol_BS/control.in .
sed -i 's/pbesol/pbe/g' control.in
sbatch run.slm

cd ../
mkdir hse06_BS
cd hse06_BS
cp ../geometry.in.next_step geometry.in
cp ../run.slm .
cp ../pbesol_BS/control.in .
sed -i 's/pbesol/hse06 0.11/g' control.in
sed -i '/xc               hse06 0.11/a hse_unit bohr-1\nexx_band_structure_version 1' control.in
#sbatch run.slm

cd ../
mkdir scan_BS
cd scan_BS
cp ../geometry.in.next_step geometry.in
cp ../run.slm .
cp ../pbesol_BS/control.in .
sed -i 's/pbesol/scan/g' control.in
sbatch run.slm
