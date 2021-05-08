# To Do

## client_instructions.json
### Description: stores instructions using json
- update/install progs using apt
  - [ ] `sudo apt update` 
  - [ ] wait until update done
  - [ ] `sudo apt upgrade`
  - [ ] `sudo apt install <PROGRAMS>`
    - [ ] <PROGRAMS> TDB loop through the jsons tho
- map network drives
  - Big ?

# List of bash commands

## Updating
- first run `sudo apt update`
- second run `sudo apt upgrade`

## install programs
- `sudo apt install <PROGRAMS>`
# Network Drive Mounting

## Installing Software
- the command is `sudo apt install curlftpfs`

## Adding Mount Point
- this just adds a spot for curlftpfs to mount the drive to
- the command is `mkdir /mnt/<FTPDRIVENAME>`

## Add FTP server
- this actually adds the ftp server specified within client_instructions.json
- here it izz `curlftpfs <FTPUSERNAME>@FTPDRIVELOCATION> /mnt/<FTPDRIVENAME>`

## Modding permissions so that users other than root can access the FTP mount
- here it is `chmod 777 /mnt/<FTPDRIVENAME>`