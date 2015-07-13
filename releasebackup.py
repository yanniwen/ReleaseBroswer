#coding=utf-8
#!/usr/bin/python

__author__ = 'yanni'

import backup


backuper = backup.helper('/data/jenkinsbak')
backuper.backupfolder('/opt/version')
backuper.findbackup('/var/lib/jenkins/jobs', 'config.xml')