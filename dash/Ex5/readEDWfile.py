import configparser

def readEDW(fileFullPath):
    config = configparser.ConfigParser()
    config.read(fileFullPath)

    load=list(map(int, config['Section_1']['LoadData'].split(',')))
    pos=list(map(int, config['Section_1']['PositionData'].split(',')))
    numPeriods=int(config['Section_1']['NumPeriods'])
    periodsLen=list(map(int, config['Section_1']['PeriodsLen'].split(',')))
    
    y = [[]] * numPeriods
    x = [[]] * numPeriods
    curPos=0
    
    for i in range(0, numPeriods):
        x[i] = pos[curPos:curPos+periodsLen[i]-1]
        x[i].append(x[i][0])

        y[i] = load[curPos:curPos+periodsLen[i]-1]
        y[i].append(y[i][0])

        curPos+=periodsLen[i]
    
    return x,y

# config = configparser.ConfigParser()
#  config['DEFAULT'] = {'ServerAliveInterval': '45',
#                       'Compression': 'yes',
#                       'CompressionLevel': '9'}

# config['bitbucket.org'] = {}
# config['bitbucket.org']['User'] = 'hg'

# config['topsecret.server.com'] = {}
# topsecret = config['topsecret.server.com']
# topsecret['Port'] = '50022'     # mutates the parser
# topsecret['ForwardX11'] = 'no'  # same here

# config['DEFAULT']['ForwardX11'] = 'yes'

# with open('example.ini', 'w') as configfile:
#     config.write(configfile)

# config.read('example.ini')
# config['bitbucket.org']['User']



# columns = ('Name', 'X', 'Y')
# lines = []

# with open('somefile.txt') as fh:
#     for line in fh:
#         if line.startswith('Name'):
#             # the name looks like it's always the second
#             # non-space string, so unpack it like so

#             _, name, *_ = line.split(' ')
#             # iterate over the next few lines until a blank is hit
#             while True:
#                 try: 
#                     line = next(fh).strip()
#                 except StopIteration:
#                     break

#                 if not line:
#                     break
#                 lines.append(dict(zip(columns, [name, *(x.strip() for x in line.split(','))])))


# print(lines)