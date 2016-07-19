from glob import glob
from Sector1 import GenericBootRecord as BootRecord

def listDrives():
    drives = []
    drives.extend(glob('/dev/sd*'))
    drives.extend(glob('/dev/mmc*'))

    return drives

def readBootSector(drive):
    with open(drive, 'rb') as drive:
        bootSector = drive.read(512)

    return bootSector


if __name__ == '__main__':
    print(len((readBootSector('/dev/sdb'))))
    br = BootRecord(readBootSector('/dev/sdb'))
    print(br)
