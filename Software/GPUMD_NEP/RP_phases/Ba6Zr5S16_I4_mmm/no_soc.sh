#cd pbesol_BS
#rm -r soc
#mkdir soc
#cp ../rename .
#cd soc
#cp ../*band* .
#rm *no_soc 
#cp ../control.in .
#sed -i '/dos/d' control.in
#cp ../geometry.in . 
#cp ~/FHIaims/utilities/aimsplot.py .
#python aimsplot.py --Emin -5. --Emax 5.
#cp aimsplot.png ../Ba2ZrS4_I4_mmm_pbesol.png
#cd ../
#
#
#rm -r no_soc
#mkdir no_soc
#cd no_soc
#cp ../*no_soc .
#cp ../rename .
#cp ../control.in .
#sed -i '/dos/d' control.in
#cp ../geometry.in . 
#bash rename
#cp ~/FHIaims/utilities/aimsplot.py .
#python aimsplot.py --Emin -5. --Emax 5.
#cp aimsplot.png ../Ba2ZrS4_I4_mmm_pbesol_no_soc.png
#cd ../
#
#cd ../
#cd pbe_BS
#rm -r soc
#mkdir soc
#cp ../rename .
#cd soc
#cp ../*band* .
#rm *no_soc 
#cp ../control.in .
#sed -i '/dos/d' control.in
#cp ../geometry.in . 
#cp ~/FHIaims/utilities/aimsplot.py .
#python aimsplot.py --Emin -5. --Emax 5.
#cp aimsplot.png ../Ba2ZrS4_I4_mmm_pbe.png
#cd ../
#
#
#rm -r no_soc
#mkdir no_soc
#cd no_soc
#cp ../*no_soc .
#cp ../rename .
#cp ../control.in .
#sed -i '/dos/d' control.in
#cp ../geometry.in . 
#bash rename
#cp ~/FHIaims/utilities/aimsplot.py .
#python aimsplot.py --Emin -5. --Emax 5.
#cp aimsplot.png ../Ba2ZrS4_I4_mmm_pbe_no_soc.png
#cd ../
#
#cd ../
cd hse06_BS
rm -r soc
mkdir soc
cp ../rename .
cd soc
cp ../*band* .
rm *no_soc 
cp ../control.in .
sed -i '/dos/d' control.in
cp ../geometry.in . 
cp ~/FHIaims/utilities/aimsplot.py .
python aimsplot.py --Emin -5. --Emax 5.
cp aimsplot.png ../Ba2ZrS4_I4_mmm_hse06.png
cd ../


rm -r no_soc
mkdir no_soc
cd no_soc
cp ../*no_soc .
cp ../rename .
cp ../control.in .
sed -i '/dos/d' control.in
cp ../geometry.in . 
bash rename
cp ~/FHIaims/utilities/aimsplot.py .
python aimsplot.py --Emin -5. --Emax 5.
cp aimsplot.png ../Ba2ZrS4_I4_mmm_hse06_no_soc.png
cd ../

#cd ../
#cd scan_BS
#rm -r soc
#mkdir soc
#cp ../rename .
#cd soc
#cp ../*band* .
#rm *no_soc 
#cp ../control.in .
#sed -i '/dos/d' control.in
#cp ../geometry.in . 
#cp ~/FHIaims/utilities/aimsplot.py .
#python aimsplot.py --Emin -5. --Emax 5.
#cp aimsplot.png ../Ba2ZrS4_I4_mmm_scan.png
#cd ../
#
#
#rm -r no_soc
#mkdir no_soc
#cd no_soc
#cp ../*no_soc .
#cp ../rename .
#cp ../control.in .
#sed -i '/dos/d' control.in
#cp ../geometry.in . 
#bash rename
#cp ~/FHIaims/utilities/aimsplot.py .
#python aimsplot.py --Emin -5. --Emax 5.
#cp aimsplot.png ../Ba2ZrS4_I4_mmm_scan_no_soc.png
#cd ../
