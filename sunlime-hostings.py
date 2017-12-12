#! python 3
# sunlime-hostings.py - create hosting contract change documents

hostingSalutation = 0
hostingContinue = 0
hosting = 0 # string to identify the hosting package; for EDIS it would be
domain = 0 #
date_1 = 0 # date for latest notification
date_2 = 0 # date when server will be deleted
gender = 0
ms = 'Frau'
mr = 'Herr'
choose = 'Choose how you want to address the client.'
enterMs = 'Enter 1 for \"Frau\".'
enterMr = 'Enter 2 for \"Herr\".'
hostingSalutationMs = 'Sehr geehrte Frau '
hostingSalutationMr = 'Sehr geehrter Herr '

#################
# Choose "Anrede"
#################

def hostingSalutationSet(hostingSalutation):
  print('{} \n {} \n {}'.format(choose,enterMs,enterMr))
  hostingSalutation = eval(input('>>> '))
  if hostingSalutation in range(1, 3):
    if hostingSalutation == 1:
      gender = ms
      print('You have entered **{}** and chosen {} as the salutation for your letter.'.format(hostingSalutation, gender))
      print('Enter the surname of the client:')
      hostingSalutationName = input('>>> ')
      hostingSalutation = hostingSalutationMs + hostingSalutationName
      print('Your salutation is: **{}**'.format(hostingSalutation))
      return hostingSalutation

    elif hostingSalutation == 2:
      gender = mr
      print('You have entered **{}** and chosen {} as the salutation for your letter.'.format(hostingSalutation, gender))
      return hostingSalutation

  else:
    print('You haven\'t entered a correct number!','Let\'s start all over again!')
    print('=================================================================')
    hostingSalutationSet(hostingSalutation)


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
  hostingSalutationStatus = hostingSalutationSet(hostingSalutation)
  hostingContinueStatus = hostingContinueSet(hostingContinue)

