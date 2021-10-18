
## Archer2 (national supercomputer)

- Ask Lucy to request access via the [MCC](https://www.ucl.ac.uk/klmc/mcc/)

## Oswald (Northumbria University supercomputer)

- To access Oswald, raise a ticket with IT (For the attention of Jimmy Gibson or Ben Levien).
- To access Oswald from home you will also need to request a login on Garrett (again by raising a ticket with IT).
- The SSH setup is a little finicky, the ssh config files that work for Lucy (stored as `~.ssh/config`) are [here](https://github.com/lucydot/ssh_config/blob/main/config)
- Oswald uses Slurm to handle job submissions; example submission script for vasp is [here](https://github.com/NU-CEM/Group_wiki/blob/main/oswald_submission.slm).

## Dade (group workstation)

- To access Dade please ask Lucy to create a user account
- To access Dade from home you will also need to request a login on Garrett (again by raising a ticket with IT).
- The SSH setup is a little finicky, the ssh config files that work for Lucy (stored as `~.ssh/config`) are [here](https://github.com/lucydot/ssh_config/blob/main/config)

From Jimmy: 
> I've copied v6.2.1 to your Downloads/VASP directory.  If you can compile and you are satisfied with the testsuite results I will install in the modules environment to make VASP available to other users.
> I've created a shared area in /home/SHARED-DATA where members of the vaspusers group have write access to.  Currently only you, Ben and myself are members.
> I've created a script to allow you to grant access to the workstation to users in your research group and also add them to the vaspusers group, so they will automatically have access to the shared area.  Run it using the following command: 
> `sudo /root/bin/add-vasp-user <USERNAME>`
> Where <USERNAME> the University ID of the user.  You will be prompted for your password.  Users will then login using their University ID and password. 
 
## Angelina (Lucy's iMac)
