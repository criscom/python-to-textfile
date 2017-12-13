#! python 3
# sunlime-hostings.py - create hosting contract change documents

hosting = 0 # string to identify the hosting package; for EDIS it would be
hostingContinue = 0
hostingGender = 0
hostingName = 0
domain = 0 #
date_1 = 0 # date for latest notification
date_2 = 0 # date when server will be deleted
gender = 0
ms = 'Frau'
mr = 'Herr'
choose = 'Choose how you want to address the client.'
enterMs = 'Enter 1 for \"Frau\".'
enterMr = 'Enter 2 for \"Herr\".'
hostingSalutationMs = 'Sehr geehrte Frau'
hostingSalutationMr = 'Sehr geehrter Herr'

#################
# Choose gender
#################

def hostingGenderSet():
  print('{} \n {} \n {}'.format(choose,enterMs,enterMr))
  hostingGender = eval(input('>>> '))

  if hostingGender in range(1, 3):
    if hostingGender == 1:
      gender = ms
      print('You have entered **{}** and chosen {} as the salutation for your letter.'.format(hostingGender, gender))
      hostingGender = hostingSalutationMs
      print('Your salutation is: **{}**'.format(hostingGender))
      return hostingGender

    elif hostingGender == 2:
      gender = mr
      print('You have entered **{}** and chosen {} as the salutation for your letter.'.format(hostingGender, gender))
      hostingGender = hostingSalutationMr
      print('Your salutation is: **{}**'.format(hostingGender))
      return hostingGender

  else:
    print('You haven\'t entered a correct number!','Let\'s start all over again!')
    print('=================================================================')
    hostingGenderSet(hostingGender)

###########
# Choose name
###########
def hostingNameSet():
  print('Enter the surname of the client:')
  hostingName = input('>>> ')
  return hostingName

###################
# Create salutation
###################
def hostingSalutationSet():
  print('hostingGender = {}, hostingName = {}'.format(hostingGenderStatus, hostingNameStatus))
  # hostingSalutation = str(hostingGenderStatus) + str(hostingNameStatus) + '!'
  hostingSalutation = '{} {}!'.format(hostingGenderStatus, hostingNameStatus)
  print('{}'.format(hostingSalutation))
  return hostingSalutation

###########
# Choose ID
###########

def hostingIDSet():
  print('Enter the client ID from easybill: ')
  hostingID = input('>>> ')
  return hostingID

##################
# Continue or quit
##################

def hostingContinueSet(hostingContinue):
  quit = input('Quit program? \'q\' for quit, \'c\' for continue : ')
  if quit == 'q':
    print('Thank you for using my script! Have a good day!')
    exit('Copyright Sunlime Web Innovations GmbH, 2018')
  else:
    print('Let\'s continue.')

##################
# Start of script
##################

while True:
  hostingGenderStatus = hostingGenderSet()
  hostingNameStatus = hostingNameSet()
  hostingSalutationStatus = hostingSalutationSet()
  hostingIDStatus = hostingIDSet()
  print('{}'.format(hostingSalutationStatus), file=open('{}-{}.txt'.format(hostingIDStatus, hostingNameStatus), 'a'))
  hostingContinueStatus = hostingContinueSet(hostingContinue)

