
def christianity():
  welcome_ = 'Hello, here are some questions based on the Bible.'
  print(welcome_)
  Instructions = "Here are the instructions:\n -There exactly 10 questions in both quizes, answer all of them\n-To type an answer simply type a, b, c or d  in the textbox\n -When you answer each question correctly you will be given 1 points, but if you answer a question wrongly answer a question 0.5 points will be deducted "
  print(Instructions)
  score_ = 0

  question_CH_1 = input(
    '1.How many brothers did Joseph have?(answer this question by using numbers)\n a. 11 \n b. 12 \n c. 0 \n d. 10:     ')  # Question 1 # If statement saying; if the question is correct it will add one to your score and tell you your answer is corrct. It is the same for all the questions
  if question_CH_1.lower() == 'a':
    print('Your answer is correct')
    score_ = score_ + 1  # If it is wrong it will move on to the next question ad deduct 0.5 from your score. It is the same for all the questions
  else:
    print('You are wrong. Joseph had 11 brothers')
    score_ = score_ - 0.5
    print('your score is {}'.format(score_))

  question_CH_2 = input(
    '2.What did Moses say God commanded the Pharaoh to do?\n a. make israel slaves \n  b. worship God \n c. let his people go \n d. appoint him as a governor:     ')  # Question 2
  if question_CH_2.lower() == 'c':
    print('You are correct')
    score_ = score_ + 1
    print('your score is {}'.format(score_))
  else:
    print('you are wrong. Moses said God commanded the Pharaoh to let his people go ')
    score_ = score_ - 0.5
    print('your score is {}'.format(score_))

  question_CH_3 = input(
    ' 3.What golden image did the Israelites make at Mt. Sinai?\n a. a golden pig \n b. a sun \n c. a golden chicken \n d. a golden calf :       ')  # Question 3
  if question_CH_3.lower() == 'd':
    print('You are correct')
    score_ = score_ + 1
    print('your score is {}'.format(score_))
  else:
    print('You are wrong. They made a golden calf')
    score_ = score_ - 0.5
    print('your score is {}'.format(score_))

  question_CH_4 = input(
    '4.Who was Jesus’ birth father?\n a. God \n b. Joseph\n c. The spirit \n d. Mary:   ')  # Question 4
  if question_CH_4.lower() == 'a':
    print('you are correct')
    score_ = score_ + 1
    print('your score is {}'.format(score_))
  else:
    print('You are wrong.Jesus’ birth father is God')
    score_ = score_ - 0.5
    print('your score is {}'.format(score_))

  question_CH_5 = input(
    "5.Name Jesus' hometown.\n a. Bethlehem \n b. Nazareth \n c. Jerusalem \n d. heaven :  ")  # Question 5
  if question_CH_5.lower() == 'b':
    print('you are correct')
    score_ = score_ + 2
    print('your score is {}'.format(score_))
  else:
    print("You are wrong. Jesus' hometown is Nazareth")
    score_ = score_ - 0.5

  question_CH_6 = input(
    '6.When God showed Abram the stars in the sky, what did he promise?\n a. That Abram would have equal descendants than the number of stars. \n b. That Abram would have more descendants than the number of stars.  \n c. That Abram would have less descendants than the number of stars. \n d.That Abram would have 10 descendants.:     ')  # Question 6
  if question_CH_6.lower() == 'b':
    print('Your answer is correct')
    score_ = score_ + 1
  else:
    print('You are wrong.the answer is: That Abram would have equal descendants than the number of stars.')
    score_ = score_ - 0.5
    print('your score is {}'.format(score_))

  question_CH_7 = input(
    '7. Who did Laban trick Jacob into marrying??\n a. Sarah \n  b. Esther \n c. Rachael \n d. Leah.:     ')  # Question 7
  if question_CH_7.lower()=='d':
    print('You are correct')
    score_ = score_ + 1
    print('your score is {}'.format(score_))
  else:
    print('you are wrong. Laban trick Jacob into marrying Leah ')
    score_ = score_ - 0.5
    print('your score is {}'.format(score_))

  question_CH_8 = input(
    ' 8.Who was Paul with when he wrote the letter to Philemon?\n a.Himself \n b. Timothy \n c. God \n d. Jesus :       ')  # Question 8
  if question_CH_8.lower() == 'b':
    print('You are correct')
    score_ = score_ + 1
    print('your score is {}'.format(score_))
  else:
    print('You are wrong. Paul was with Timothy when he wrote the letter to Philemon')
    score_ = score_ - 0.5
    print('your score is {}'.format(score_))

  question_CH_9 = input('9.Who killed Absalom??\n a. David \n b. Saul\n c. Sammuel \n d. Joab:   ')  # Question 9
  if question_CH_9.lower() == 'd':
    print('you are correct')
    score_ = score_ + 1
    print('your score is {}'.format(score_))
  else:
    print('You are wrong.Joab killed Absalom')
    score_ = score_ - 0.5
    print('your score is {}'.format(score_))

  question_CH_10 = input(
    "10.Who returned to Israel to build up the walls of Jerusalem?.\n a. Nehemiah \n b. Esther \n c. Cyrus \n d. John :  ")  # Question 6
  if question_CH_10.lower() == 'a':
    print('you are correct')
    score_ = score_ + 3
    print('your score is {}'.format(score_))

  else:
    print("You are wrong. Nehemiah is the one who returned to Israel to build up the walls of Jerusalem ")
    score_ = score_ - 0.5

  if score_ >= 9:
    print('(distinction) Excellent you pass')
  elif score_ >= 6:
    print('(Merit) Very good you pass')
  elif score_ >= 4:
    print('(pass) Well done, but work harder next time')
  else:
    print('(Fail) Sorry but you did no get enough points')


def islam():
  welcome_ = 'Hello, here are some questions based on the Quran.'
  print(welcome_)
  Instructions = 'Here are the instructions:\n -There exactly 10 questions in both quizes, answer all of them\n-To type an answer simply type a, b, c or d  in the textbox\n -When you answer each question correctly you will be given 4 points, but if you answer a question wrongly answer a question 2.5 points will be deducted '
  print(Instructions)
  score_ = 0

  question_is_1 = input('1.Who will get their book of deeds in the right hand on the Day of Judgment?\n a.The disbelievers\n b.The believers\n c.The hypocrites\n d. The leaders :   ')  # Question 1
  if question_is_1.lower() == 'b':
    print('You are correct')
    score_ = score_ + 1
    print('your score is {}'.format(score_))
  else:
    print('You are wrong.the believers will get their book of deeds in the right hand on the Day of Judgment')
    score_ = score_ - 0.5
    print('your score is {}'.format(score_))

  question_is_2 = input(
    "2.What was the relation between Prophet Musa (alayhi as-salaam) & Prophet Haroon (alayhi as-salaam)?\n a. Cousins\n b. Brothers \n c.Father & son \n d. Friends :")  # Question 2
  if question_is_2.lower() == 'a':
    print('You are correct')
    score_ = score_ + 1
    print('your score is {}'.format(score_))
  else:
    print(
      'You are wrong. the relation between Prophet Musa (alayhi as-salaam) & Prophet Haroon (alayhi as-salaam) is cousins')
    score_ = score_ - 0.5
    print('your score is {}'.format(score_))

  question_IS_3 = input(
    '3.What is Az-Zaqqum?\n a. Food for the people of hellfire\n b. Drink for the people of hellfire \n c. Home for the people of hellfire \n d. Clothes for the people of hellfire :')  # Question 3
  if question_IS_3.lower() == 'a':
    print('you are correct')
    score_ = score_ + 1
    print('your score is {}'.format(score_))
  else:
    print('You are wrong. Az-Zaqqum is food for the people of hellfire')
    score_ = score_ - 0.5
    print('your score is {}'.format(score_))

  question_IS_4 = input(
    '4.What does Zam Zam mean?\n a. Holy water\n b. Water well \n c. Stop \n d. Drink :')  # Question 4
  if question_IS_4.lower() == 'c':
    print('you are correct')
    score_ = score_ + 1
    print('your score is {}'.format(score_))
  else:
   print('You are wrong.Zam Zam means stop')
  score_ = score_ - 0.5
  print('your score is {}'.format(score_))

  question_IS_5 = input(
    '5.What is the virtue of reciting Ayatul Kursi before going to bed at night to sleep?\n a. Takes away hunger\n b. Gives you strength \n c. You are protected from harm till sunrise \n d. House in Jannah :')  # Question 5
  if question_IS_5.lower() == 'c':
    print('you are correct')
    score_ = score_ + 2
    print('your score is {}'.format(score_))
  else:
    print(
      'You are wrong. the virtue of reciting Ayatul Kursi before going to bed at night to sleep is you are protected from harm till sunrise')
    score_ = score_ - 0.5
  print('your score is {}'.format(score_))

  question_IS_6 = input(
    '6.Which Angel is Hellfire’s gatekeeper?\n a. Jibraeel (as) \n b. Mikaeel (as)\n c.Maalik (as) \n d. Israfeel (as) :   ')  # Question 6
  if question_IS_6.lower() == 'c':
    print('You are correct')
    score_ = score_ + 1
    print('your score is {}'.format(score_))
  else:
    print('You are wrong.')
    score_ = score_ - 0.5
    print('your score is {}'.format(score_))

  question_IS_7 = input(
    '7.Which of the following is the name of Allah with the meaning – The Most Loving One?\n a. Al-Majeed\n b. Al-Wadud \n c. Al-Muqtadir\n d Al-Waarith :    ')  # Question7
  if question_IS_7.lower() == 'b':
    print('You are correct')
    score_ = score_ + 1
    print('your score is {}'.format(score_))
  else:
   print('You are wrong. the name of Allah with the meaning the Most Loving One is Al-Wadud')
   score_ = score_ - 0.5
   print('your score is {}'.format(score_))

  question_IS_8 = input('8.What is the name of Madinah in the Quran?\n a.Bakkah\n b. Quds\n c. Marwah\n d.Yathrib  :    ')  # Question 8
  if question_IS_8.lower() == 'd':
    print('you are correct')
    score_ = score_ + 1
    print('your score is {}'.format(score_))
  else:
    print('You are wrong. the name of Madinah in the Quran is Yathrib ')
    score_ = score_ - 0.5
    print('your score is {}'.format(score_))

  question_IS_9 = input(
    '9.Why we should not curse time?\n a. Because it will bring bad luck\n b.Because Allah says He is Time\n c.  Because Allah says He will cut our time\n d. Because it will bring good luck :    ')  # Question 9
  if question_IS_9.lower() == 'b':
    print('you are correct')
    print('your score is {}'.format(score_))
    score_ = score_ + 1
  else:
    print('You are wrong. We should not curse time because Allah says he is time')
    score_ = score_ - 0.5
    print('your score is {}'.format(score_))

  question_IS_10 = input(
    '10.Allah says, with His knowledge, He is more closer to us than our ________?\n a. Thoughts \n b. Heart \n c. Jugular Vein \n d. Blood :      ')  # Question 10
  if question_IS_10.lower() == 'c':
    print('you are correct')
    score_ = score_ + 3
    print('your score is {}'.format(score_))
  else:
    print('You are wrong. Allah says, with His knowledge, He is more closer to us than our jugular vein')
    score_ = score_ - 0.5
    print('your score is {}'.format(score_))

  if score_ >= 9:
   print('(distinction) Excellent you pass')
  elif score_ >= 6:
    print('(Merit) Very good you pass')
  elif score_ >= 3:
    print('(pass) Well done, but work harder next time')
  else:
    print('(Fail) Sorry but you did no get enough points')

def hinduism():
  welcome_='Hello, here are some questions based on the Vedas and Bagavad gita.'
  print(welcome_)
  Instructions='Here are the instructions:\n -There exactly 10 questions in both quizes, answer all of them\n-To type an answer simply type a, b, c or d  in the textbox\n -When you answer each question correctly you will be given 1 point, but if you answer a question wrongly answer a question 2.5 points will be deducted '
  print(Instructions)
  score_=0

  question_HI_1=input('1. Badrinath is situated on the bank of river\n(a) Ganga\n(b) Yamuna\n(c) Alaknanda\n(d) Saraswath :   ')# Question 1
  if question_HI_1.lower()=='c' :
    print('You are correct')
    score_ = score_ + 1
    print('your score is {}'.format(score_))
  else :
    print('You are wrong.Badrinath is situated on the bank of river Alaknanda')
    score_ = score_ - 0.5
    print('your score is {}'.format(score_))

  question_HI_2=input('2.Who is the king of wealth?\n(a) Agni\n(b) Vayu\n(c) Indra\n(d) Kubera :  ')# Question 2
  if question_HI_2.lower()=='d' :
    print('You are correct')
    score_ = score_ + 1
    print('your score is {}'.format(score_))
  else :
    print('You are wrong.the king of wealth is Kubera')
    score_ = score_ - 0.5
    print('your score is {}'.format(score_))

  question_HI_3=input('3.The Rock cut temple of Kailashnath is situated at?\n(a) Ajanta\n(b) Ellora\n(c) Elephants\n(d) Mamallapuram :  ')# Question 3
  if question_HI_3.lower()=='b' :
    print('you are correct')
    score_ = score_ + 1
    print('your score is {}'.format(score_))
  else :
    print('You are wrong. The Rock cut temple of Kailashnath is situated at Ellora')
    score_ = score_ - 0.5
    print('your score is {}'.format(score_))

  question_HI_4=input('4.“Hindu Political Thought” means?\n a.(a) Political Thought of Hindu religion\n(b) Political Thought given in Vedas\n(c) Political Thought of Hindu Rajas\n(d) Political Thought which originated in the Indian continent :  ')# Question 4
  if question_HI_4.lower()=='d' :
    print('you are correct')
    print('your score is {}'.format(score_))
    score_ = score_ + 1
  else :
    print('You are wrong.“Hindu Political Thought” means Political Thought which originated in the Indian continent')
    score_ =score_-0.5
    print('your score is {}'.format(score_))

  question_HI_5=input('5.Where is Tirupati Balaji (Tirumala Venkateswara Temple) present?\n(a) Chittor, Andhra Pradesh\n(b) Vishakapatnam, Andhra Pradesh\n(c) Kolkata, West Bengal\n(d) Cuttack, Odisha :')# Question 5
  if question_HI_5.lower()=='a' :
    print('you are correct')
    score_=score_+2
    print('your score is {}'.format(score_))
  else :
    print('You are wrong. Tirupati Balaji (Tirumala Venkateswara Temple) present in Chittor, Andhra Pradesh')
    score_=score_-0.5
    print('your score is {}'.format(score_))

  question_HI_6=input('6.Who is the wife of ‘Ravana’?\n(a) Shrutakirti\n(b) Simhika\n(c) Mandavi\n(d) Mandodari :   ')# Question 6
  if question_HI_6.lower()=='d' :
    print('You are correct')
    score_=score_+1
    print('your score is {}'.format(score_))
  else :
    print('You are wrong.the wife of ‘Ravana’ is Mandodari')
    score_=score_-0.5
    print('your score is {}'.format(score_))

  question_HI_7=input('7. “Yama’, the God of death in Hinduism, uses what animal as his transport?\n(a) Buffalo\n(b) Raven\n(c) Elephant\n(d) Camel :    ')# Question7
  if question_HI_7.lower()=='a' :
    print('You are correct')
    score_=score_+1
    print('your score is {}'.format(score_))
  else :
    print('You are wrong. “Yama’, the God of death in Hinduism, uses a Buffalo')
    score_=score_-0.5
    print('your score is {}'.format(score_))

  question_HI_8=input('8.Where is Padmanabhaswamy Temple lo­cated?\n(a) Kedarnath, Uttarakhand\n(b) Mumbai, Maharashtra\n(c) Thiruvananthapuram, Kerala\n(d) Hyderabad, Andhra Pradesh  :    ')# Question 8
  if question_HI_8.lower()=='c' :
    print('you are correct')
    score_=score_+1
    print('your score is {}'.format(score_))
  else :
    print('You are wrong. t Padmanabhaswamy Temple lo­cated in Thiruvananthapuram ')
    score_=score_-0.5
    print('your score is {}'.format(score_))

  question_HI_9=input('9. “Dharma” means?\n(a) Virtuous path\n(b) Higher Truth\n(c) The right duty of a person\n(d) All the above :    ')# Question 9
  if question_HI_9.lower()=='d' :
    print('you are correct')
    score_=score_+1
    print('your score is {}'.format(score_))
  else :
    print('You are wrong.“Dharma” means All the above')
    score_=score_-0.5
    print('your score is {}'.format(score_))

  question_HI_10=input('10.Which is the sacred text of Hinduism?\n(a) The Vedas\n(b) The Bhagavad Gita\n(c) The epics of the Mahabharata and the Ramayana\n(d) All of the above :      ')# Question 10
  if question_HI_10.lower()=='d' :
    print('you are correct')
    score_=score_+3
    print('your score is {}'.format(score_))
  else :
    print('You are wrong. the sacred text of Hinduism is All of the above')
    score_=score_-0.5
    print('your score is {}'.format(score_))

  if score_>=9 :
    print('(distinction) Excellent you pass')
  elif score_>=6 :
    print('(Merit) Very good you pass')
  elif score_>=3 :
    print('(pass) Well done, but work harder next time')
  else :
    print('(Fail) Sorry but you did no get enough points')


Name=input('What is your name? :    ')
Religion=input("Welcome to the Religious quiz game {}. What is your religion(type'c' Christianity , Islam 'i' or Hinduism 'h'):     ".format(Name))

if Religion.lower() == 'c':
  print(christianity())
elif Religion.lower() == 'i':
  print(islam())
elif Religion.lower() == 'h':
  print(hinduism())
else:
  print('Error: invalid religion')