import os

os.system('cp -r dielectric BEC')
os.chdir('BEC')
os.system('cp ~/FHIaims/utilities/BEC.py .')
os.system("sed -i '/DFPT/d' control.in") 
os.system("rm slurm* aims.out")

atoms = ['Ba','Zr']
coordinates = ['1','2','3']
#wyckoff = ['5','6','7','8','9','10','11','12']
for i in atoms:
    for j in coordinates:
            print(i,j)
            os.system("python3 BEC.py --name %s --kx 16 16 16 --ky 16 16 16 --kz 16 16 16 -c %s >> output_%s_%s"%(i,j,i,j))
            os.system('pwd')
            os.system("mv %s_disp_0.0 %s_disp_0.0_%s"%(i,i,j))
            os.system("mv %s_disp_0.0025 %s_disp_0.0025_%s"%(i,i,j))
