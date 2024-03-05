try:
    import os
    import sys

except ImportError:
    print('Failed to import, running setup.bat...')
    os.system('setup.bat')


def main(file_input, file_output):
    while True:
        option = input('Would you like to trim the video? (y/n): ')
        if option.lower() == 'y' or option.lower() == 'yes':
            print(file_input, file_output)  # debug
            start = input('Where should the video start? (00:00:00) ')
            end = input('Where should the video end? (00:00:00) ')
            os.system(
                f'ffmpeg -i "{file_input}" -ss {start} -to {end} -c:v copy -c:a copy "{file_output}"')
            os.system(
                f'call compress.bat "{file_output}" "{os.getcwd()}\output\output.mp4"')
            os.remove(file_output)  # remove afterwards
            break
        elif option.lower() == 'n' or option.lower() == 'no':
            print(file_input, file_output)  # debug
            os.system(
                f'call compress.bat "{file_input}" "{os.getcwd()}\output\output.mp4"')
            break


if __name__ == '__main__':
    if os.path.exists('output'):
        pass
    else:
        os.system('mkdir output')
    file_input = (sys.argv[1])
    file_output = (sys.argv[2])
    main(file_input, file_output)
