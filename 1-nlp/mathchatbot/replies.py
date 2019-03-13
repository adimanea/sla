######################################################################
# File: replies.py
# Description: Predefined replies for the (rudimentary) MathChatBot.
# Author: Adrian Manea.
# Disclaimer: Yes, they are elementary. But I had fun writing it.
######################################################################
# HELLOS
######################################################################
he1 = 'Hi, how can I help you today?'
he2 = 'Hello there! How can I help you?'
he3 = 'Howdy! How can I be of service?'
he4 = 'Hi! What would you like to talk about?'
he5 = "Greetings! Tell me what you're interested in."
he = [he1, he2, he3, he4, he5]

######################################################################
# GOODBYES
######################################################################
leave1 = 'You can always end the conversation saying goodbye.'
leave2 = 'Saying goodbye closes the conversation.'
leave3 = "Write 'bye' whenever you want to exit."
leave4 = "Adding 'bye' to your reply exits the conversation."
leave5 = "Writing 'bye' closes the program."
leave = [leave1, leave2, leave3, leave4, leave5]

######################################################################
# WHAT I KNOW
######################################################################
topics1 = "Here are the topics I know something about:"
topics2 = "Here's what I can talk about:"
topics3 = "Here's what I know so far:"
topics4 = "So far, I've learned about:"
topics5 = "I have been taught about:"
topics = [topics1, topics2, topics3, topics4, topics5]

######################################################################
# MORE?
######################################################################
more1 = 'What else do you want to talk about?'
more2 = 'Is there any other subject you would like to talk about?'
more3 = 'What else interests you?'
more4 = 'Right. What else shall we talk about?'
more5 = 'More topics in your mind?'
more = [more1, more2, more3, more4, more5]

######################################################################
# PRACTICE STARTER
######################################################################
practice1 = 'Practice makes perfect, you know?'
practice2 = 'Practice is always a good idea!'
practice3 = 'Practice will do you good, for sure!'
practice4 = 'When in doubt, practice!'
practice5 = 'There is no way of getting better but practice!'
practiceLs = [practice1, practice2, practice3, practice4, practice5]

######################################################################
# INVALID INPUT
######################################################################
notu1 = "Sorry, I don't understand. Could you try something else, please?"
notu2 = "I'm not sure I know what you mean. Could you retry?"
notu3 = "You got me confused with that. Please retry."
notu4 = "That's something that I don't quite get. Please try rephrasing."
notu5 = "I can't quite make anything of that. Please retry."
notu = [notu1, notu2, notu3, notu4, notu5]

######################################################################
# IF YOU WANT TO STUDY
######################################################################
studyR1 = "I'm sure there are many resources you can check out. " + \
    "You can start by reading some Wikipedia."
studyR2 = "You should start by reading from the course textbook."
studyR3 = "Reading your course notes is always a good start."
studyR4 = "You can get together with some colleagues and try studying " + \
    "through discussions and debates if that works for you."
studyR5 = "Set aside at least 30 minutes each day and read through your notes."
studyReplies = [studyR1, studyR2, studyR3, studyR4, studyR5]

######################################################################
# IF YOU WANT TO PRACTICE
######################################################################
practiceR1 = "You can always start with the exercises in the textbook."
practiceR2 = "First, read the theory, then try solving some exercises " + \
    "in the textbook. See how that works for you."
practiceR3 = "You can find some good exercises on Project Euler."
practiceR4 = "Get a list of exercises from you professor and try " + \
    "solving those first."
practiceR5 = "It's always a good idea to start by reading the theory, though."
practiceReplies = [practiceR1, practiceR2, practiceR3, practiceR4, practiceR5]
