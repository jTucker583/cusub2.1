# Helpful Links

## Removing password requirement for ssh 

### Windows:
- 1: If you have ever run `ssh-keygen`, skip this step. Otherwise, run `ssh-keygen`
- 2: Run the following command, replacing `my_name` with your username and `laz@192.168.1.103` with whatever you are trying to ssh into
```type c:\users\my_name\.ssh\id_rsa.pub | ssh root@172.110.1.171 "cat >> ~/.ssh/authorized_keys"```
- 3: Confused? Check out [this link.](https://superuser.com/questions/96051/ssh-from-windows-to-linux-without-entering-a-password)

### Linux:
- 1: Run this command to check if existing SSH keys are present `ls -al ~/.ssh/id_*.pub`. If keys exist, skip to step 5.
- 2: Run `ssh-keygen`
- 3: Press enter and accept the default save location
- 4: Enter passphrase if you want, else press enter. We reccomend no password.
- 5: Type `ssh-copy-id laz@192.168.1.103`, replacing `laz@192.168.1.103` with your target device.
- 6: You will be prompted to enter the target device's password. You should now be able to ssh without typing the password!
- Confused? Check out [this link.](https://linuxize.com/post/how-to-setup-passwordless-ssh-login/)
