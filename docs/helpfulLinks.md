# Helpful Links:

## Removing password requirement for ssh 

### Windows:
```type c:\users\my_name\.ssh\id_rsa.pub | ssh root@172.110.1.171 "cat >> ~/.ssh/authorized_keys"```
