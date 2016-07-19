from binascii import hexlify


class GenericBootRecord:
    def __init__(self, hexs):
        self.hexs = hexs
        self.bootstrap = hexs[:446]
        self.part1 = hexs[446:462]
        self.part2 = hexs[462:478]
        self.part3 = hexs[478:494]
        self.part4 = hexs[494:510]
        self.brSignature = hexs[510:]

    def __str__(self):
        s = []
        s.append('BootStrap:\n{}'.format(hexlify(self.bootstrap)))
        s.append('Part1:\n{}'.format(hexlify(self.part1)))
        s.append('Part1:\n{}'.format(hexlify(self.part2)))
        s.append('Part1:\n{}'.format(hexlify(self.part3)))
        s.append('Part1:\n{}'.format(hexlify(self.part4)))
        s.append('Boot Record Signature:\n{}'.format(hexlify(self.brSignature)))

        return '\n'.join(s)


class Sector1:
    def __init__(self, hexs):
        self.hexs = hexs
        self.bootstrap = hexs[:446]
        self.timeStamp = hexs[218:224]
        self.diskSignatur = hexs[440:444]
        self.copyProtection = hexs[444:446]
        self.part1 = hexs[446:462]
        self.part2 = hexs[462:478]
        self.part3 = hexs[478:494]
        self.part4 = hexs[494:510]
