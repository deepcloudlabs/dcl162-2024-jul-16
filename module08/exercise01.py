"""
installation: https://courseware.deepcloudlabs.com/software/stage2022a-python.programming.zip
              unzip to c:\
1. start mysql server
   c:\DEVEL\stage\var\scripts\start-mysqld.bat:
    call setenv.bat
    mysqld --console
   c:\DEVEL\stage\var\scripts\setenv.bat:
    echo off
    set user=root
    set password=Secret_123
    set drive=C:
    set mysqlpath=%drive%\DEVEL\stage\opt\mysql-8.2.0\bin
    %drive%
    cd %mysqlpath%
    echo on

   2024-07-18T07:21:13.966497Z 0 [System] [MY-010931] [Server] C:\DEVEL\stage\opt\mysql-8.2.0\bin\mysqld.exe: ready for connections. Version: '8.2.0'  socket: ''  port: 3306  MySQL Community Server - GPL.

2.  c:\DEVEL\stage\var\scripts\mysql-cli.bat

3. mysql-connector-python
"""