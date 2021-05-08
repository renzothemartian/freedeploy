# Network Drive Mounting

## Installing Software
- the command is `sudo apt install curlftpfs`

## Adding Mount Point
- this just adds a spot for curlftpfs to mount the drive to
- the command is `mkdir /mnt/<FTPDRIVENAME>`

## Add FTP server
- this actually adds the ftp server specified within client_instructions.json
- here it izz `curlftpfs <FTPUSERNAME>@FTPDRIVELOCATION> /mnt/<FTPDRIVENAME>`