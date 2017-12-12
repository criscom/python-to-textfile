#! python 3
# sunlime-hostings.py - create hosting contract change documents

hostingOpening = 0
hosting = 0 # string to identify the hosting package; for EDIS it would be
domain = 0 #
date_1 = 0 # date for latest notification
date_2 = 0 # date when server will be deleted
choose = 'Choose how you want to address the client.'
ms = 'Enter 1 for \"Frau\".'
mr = 'Enter 2 for \"Herr\".'

def hostingOpeningSet(hostingOpening):
  print('{} \n {} \n {}'.format(choose,ms,mr))
  hostingOpening = eval(input())
  if hostingOpening in range(1, 3):
    if hostingOpening == 1:
      print('You have entered **{}** and chosen \"Frau\" as the opening greeting for your letter.'.format(hostingOpening))
      return hostingOpening

    elif hostingOpening == 2:
      print('You have entered **{}** and chosen \"Herr\" as the opening greeting for your letter.'.format(hostingOpening))
      return hostingOpening

  else:
    print('You haven\'t entered a correct number!','Let\'s start all over again!')
    print('=================================================================')
    hostingOpeningSet(hostingOpening)



##################
# Start of script
##################

hostingOpeningStatus = hostingOpeningSet(hostingOpening)
  
  # quit = input('Quit program? \'q\' for quit, \'c\' for contiune : ')
  # if quit == 'q':
  #   print('Thank you for using my script! Have a good day!')
  #   print ('Copyright Sunlime Web Innovations GmbH, 2018')
  #   break
  # else:
  #   print('Let\'s continue.')