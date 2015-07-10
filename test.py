#coding=utf-8
#!/usr/bin/python

__author__ = 'yanni'

import backup


backuper = backup.helper('/Users/yanni/Downloads/backup')
backuper.backupfolder('/Users/yanni/Downloads/TestRemoteProcess')
backuper.findbackup('/Users/yanni/Downloads/TestRemoteProcess', 'values.xml')
