from struct import pack, unpack
from argparse import ArgumentParser

START_OFFSET = 0x800

def main():
    parser = ArgumentParser()
    parser.add_argument('image', help='Bootloader image (fastboot.img)')
    args = parser.parse_args()

    with open(args.image, 'rb') as f:
        f.seek(START_OFFSET)
        header = unpack('<I16sII', f.read(28))

    print('First command: 0x%08x' % header[0])
    print('Magic: %s' % header[1].decode('ascii'))
    print('Load address: 0x%08x' % header[2])
    print('End address: 0x%08x' % header[3])

if __name__ == '__main__':
    main()
