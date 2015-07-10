#coding=utf-8
#!/usr/bin/python

__author__ = 'yanni'

import os
import shutil
import errno
import datetime

class helper:

    backup_size = 0
    target_folder = ''
    today_backup_folder = ''

    def __init__(self, target, bsize=5):
        self.target_folder = target
        self.backup_size = bsize

        today = datetime.date.today().strftime('%Y%m%d')
        self.today_backup_folder = self.target_folder + os.sep + today
        if not os.path.exists(self.today_backup_folder):
            os.makedirs(self.today_backup_folder)
        self.__prepare()

    def __prepare(self):
        backups = os.listdir(self.target_folder)
        backups.sort(reverse=True)
        index = 0
        # 只保留backup_size设定天数的备份纪录
        for folder in backups:
            index += 1
            if index > self.backup_size:
                os.removedirs(self.target_folder + os.sep + folder)

    def backupfolder(self, folder):
        if os.path.exists(folder):
            split = os.path.split(folder)
            dst = self.today_backup_folder + os.sep + split[1]
            index = 0
            while os.path.exists(dst):
                index += 1
                dst = self.today_backup_folder + os.sep + split[1] + '_' + str(index)
                print dst
            #TODO: 文件长度名不能超过255
            try:
                shutil.copytree(folder, dst)
            except OSError as exc:
                if exc.errno == errno.ENOTDIR:
                    shutil.copy(folder, dst)
                else:
                    raise
        else:
            print 'Folder %s most likely does not exist' % folder

    def backupfile(self, filepath):
        if os.path.exists(filepath):
            filename = filepath.replace('/', '__')[1:]
            #TODO: 文件长度名不能超过255
            dst = self.today_backup_folder + os.sep + filename
            index = 0
            while os.path.exists(dst):
                index += 1
                dst = self.today_backup_folder + os.sep + filename + '_' + str(index)
                print dst
            try:
                shutil.copyfile(filepath, dst)
            except OSError as exc:
                print exc
        else:
            print 'File %s most likely does not exist' % filepath

    def findbackup(self, dir, file):
        flist = []
        for root, subFolders, files in os.walk(dir):
            for f in files:
                if f.find(file) != -1:
                    flist.append(os.path.join(root, f))

        for f in flist:
            self.backupfile(f)