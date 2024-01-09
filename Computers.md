
## Archer2 (national supercomputer)

- Ask Lucy to request access via the [MCC](https://www.ucl.ac.uk/klmc/mcc/)
- To use Archer2, first register using SAFE: https://safe.epcc.ed.ac.uk/.
- There is a decent training programme associated with Archer2. There is the Archer2 driving test which outlines how Archer2 works and gives you a small amount of resources to use: https://www.archer2.ac.uk/training/. There are also some more advanced programmes on MPI/OpenMP etc.
- Note that Archer has three file systems: `/home` (for logging in and keeping scripts/binaries), `/work` (for running jobs) and `/epsrc` (for file storage). Do not try to submit jobs from `/home` - your job will not run here.

| Nodes    | 5,860 nodes: 5,276 standard memory, 584 high memory|
|----------|----------------------------------------------------|
| Procs    | 2× AMD EPYCTM 7742, 2.25 GHz, 64-core|
| Memory   |  256 GB (standard memory), 512 GiB (high memory)|
| Cores per node | 128 (2× 64-core processors)|

More details on hardware can be found [here](https://www.archer2.ac.uk/about/hardware.html)

## Young (National supercomputer at UCL)
| Nodes    | 582 nodes: 576 standard memory, 6 high memory|
|----------|----------------------------------------------------|
| Procs    | x86 Xenon Cascade Lake|
| Memory   |  192 GB (standard memory), 3x1.5 TB (high memory), 3x2TB (high memory) |
| Cores per node | 40 (2× 64-core processors)|

More info can be found [here](https://www.rc.ucl.ac.uk/docs/Clusters/Young/)

## Northumbria servers

- To access computers on the Northumbria network (Oswald or Dade) from home you will also need to request a login on Garrett (again by raising a ticket with IT) and ssh in via Garrett. The SSH setup is a little finicky (via a Proxy command) - the ssh config files that work for Lucy (stored as `~.ssh/config`) are [here](https://github.com/lucydot/ssh_config/blob/main/config)
- Note that to access computers on the Northumbria network (use the Sky Guest Wifi as the NU Simply Web, NU staff does not allow SSH) from campus you do not need to "hop through" the Garrett proxy.

## Oswald (Northumbria University supercomputer)

- To access Oswald, raise a ticket with IT (For the attention of Jimmy Gibson or Ben Levien).
- To login from campus use `ssh username@oswald`. To login from home see the notes above.
- Oswald uses Slurm to handle job submissions; example submission script for vasp is [here](https://github.com/NU-CEM/Group_wiki/blob/main/oswald_submission.slm).

| Nodes    | 32 compute nodes |
|----------|----------------------------------------------------|
| Procs    | 2× Intel Xeon E5-2680 v4 14 core 2.4GHz CPU|
| Memory   | 64 GB RAM, 120 GB SSD|
| Cores per node | 28 (2x 14-core processors)|

## Dade (group workstation)

- Specs - **processors**: 2* Intel Xeon 6230 2.1 2933MHz 20C (40 physical cores total), **memory**: 192GB (6x32GB) DDR4 2933 DIMM ECC Registered 2CPU Memory

- To access Dade please ask Lucy to create a user account
- To access Dade from home please see the notes above.

From Jimmy: 
> I've copied v6.2.1 to your Downloads/VASP directory.  If you can compile and you are satisfied with the testsuite results I will install in the modules environment to make VASP available to other users.
> I've created a shared area in /home/SHARED-DATA where members of the vaspusers group have write access to.  Currently only you, Ben and myself are members.
> I've created a script to allow you to grant access to the workstation to users in your research group and also add them to the vaspusers group, so they will automatically have access to the shared area.  Run it using the following command: 
> `sudo /root/bin/add-vasp-user <USERNAME>`
> Where <USERNAME> the University ID of the user.  You will be prompted for your password.  Users will then login using their University ID and password. 
 
## Angelina (Lucy's iMac)
