import time
import math

# Q1 : Write a function using only list filter lambda that can tell whether a number is a Fibonacci number or not. 
# You can use a pre-calculated list/dict to store fab numbers till 10000 PTS:50
fibonacci = [2,3]
for i in range(1,9999):
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

def check_fibonacci(number):
    val = list(filter(lambda x : x in fibonacci, [number]))
    if val:
        return True
    else:
        return False









# Q2 : Using list comprehension (and zip/lambda/etc if required) write expressions that: PTS: 100
#       a. add 2 iterables a and b such that a is even and b is odd
#       b. strips every vowel from a string provided (tsai>>t s)
#       c. acts like a sigmoid function for a 1D array
#       d. takes a small character string and shifts all characters by 5 (handle boundary conditions) tsai>>yxfn

# a. add 2 iterables a and b such that a is even and b is odd
x = [1,3,5,2,4,8]
y = [1,2,3,2,9,1]
[x[i] + y[i] for i in range(len(x)) if x[i]%2==0 if y[i]%2==1]

# b. strips every vowel from a string provided (tsai>>t s)
text = 'tsai'
''.join([c for c in text if c not in ['a','e','i','o','u']])

# c. acts like a sigmoid function for a 1D array
import math
1d_array = [1,2,3,4,5]
[1 / (1 + math.exp(-x)) for x in [1,2,3]]

# d. takes a small character string and shifts all characters by 5 (handle boundary conditions) tsai>>yxfn
def get_shifted_char(input):
    raw = 'abcdefghijklmnopqrstuvwxyz'
    shifted = 'fghijklmnopqrstuvwxyzabcde'
    for idx,val in enumerate(raw):
        if input==val:
            target_idx = idx
    return shifted[target_idx]

string = 'abyz'
''.join(list(map(get_shifted_char,string)))








# Q3 - A list comprehension expression that takes a ~200-word paragraph, and checks whether it has any of the swear words
#  mentioned in https://github.com/RobertJGabriel/Google-profanity-words/blob/master/list.txt PTS:100

swear_words = ['4r5e', '5h1t', '5hit', 'a55', 'anal', 'anus', 'ar5e', 'arrse', 'arse', 'ass', 'ass-fucker', 'asses', 'assfucker', 'assfukka', 'asshole', 'assholes', 'asswhole', 'a_s_s', 'b!tch', 'b00bs', 'b17ch', 'b1tch', 'ballbag', 'balls', 'ballsack', 'bastard', 'beastial', 'beastiality', 'bellend', 'bestial', 'bestiality', 'bi+ch', 'biatch', 'bitch', 'bitcher', 'bitchers', 'bitches', 'bitchin', 'bitching', 'bloody', 'blow job', 'blowjob', 'blowjobs', 'boiolas', 'bollock', 'bollok', 'boner', 'boob', 'boobs', 'booobs', 'boooobs', 'booooobs', 'booooooobs', 'breasts', 'buceta', 'bugger', 'bum', 'bunny fucker', 'butt', 'butthole', 'buttmunch', 'buttplug', 'c0ck', 'c0cksucker', 'carpet muncher', 'cawk', 'chink', 'cipa', 'cl1t', 'clit', 'clitoris', 'clits', 'cnut', 'cock', 'cock-sucker', 'cockface', 'cockhead', 'cockmunch', 'cockmuncher', 'cocks', 'cocksuck', 'cocksucked', 'cocksucker', 'cocksucking', 'cocksucks', 'cocksuka', 'cocksukka', 'cok', 'cokmuncher', 'coksucka', 'coon', 'cox', 'crap', 'cum', 'cummer', 'cumming', 'cums', 'cumshot', 'cunilingus', 'cunillingus', 'cunnilingus', 'cunt', 'cuntlick', 'cuntlicker', 'cuntlicking', 'cunts', 'cyalis', 'cyberfuc', 'cyberfuck', 'cyberfucked', 'cyberfucker', 'cyberfuckers', 'cyberfucking', 'd1ck', 'damn', 'dick', 'dickhead', 'dildo', 'dildos', 'dink', 'dinks', 'dirsa', 'dlck', 'dog-fucker', 'doggin', 'dogging', 'donkeyribber', 'doosh', 'duche', 'dyke', 'ejaculate', 'ejaculated', 'ejaculates', 'ejaculating', 'ejaculatings', 'ejaculation', 'ejakulate', 'f u c k', 'f u c k e r', 'f4nny', 'fag', 'fagging', 'faggitt', 'faggot', 'faggs', 'fagot', 'fagots', 'fags', 'fanny', 'fannyflaps', 'fannyfucker', 'fanyy', 'fatass', 'fcuk', 'fcuker', 'fcuking', 'feck', 'fecker', 'felching', 'fellate', 'fellatio', 'fingerfuck', 'fingerfucked', 'fingerfucker', 'fingerfuckers', 'fingerfucking', 'fingerfucks', 'fistfuck', 'fistfucked', 'fistfucker', 'fistfuckers', 'fistfucking', 'fistfuckings', 'fistfucks', 'flange', 'fook', 'fooker', 'fuck', 'fucka', 'fucked', 'fucker', 'fuckers', 'fuckhead', 'fuckheads', 'fuckin', 'fucking', 'fuckings', 'fuckingshitmotherfucker', 'fuckme', 'fucks', 'fuckwhit', 'fuckwit', 'fudge packer', 'fudgepacker', 'fuk', 'fuker', 'fukker', 'fukkin', 'fuks', 'fukwhit', 'fukwit', 'fux', 'fux0r', 'f_u_c_k', 'gangbang', 'gangbanged', 'gangbangs', 'gaylord', 'gaysex', 'goatse', 'God', 'god-dam', 'god-damned', 'goddamn', 'goddamned', 'hardcoresex', 'hell', 'heshe', 'hoar', 'hoare', 'hoer', 'homo', 'hore', 'horniest', 'horny', 'hotsex', 'jack-off', 'jackoff', 'jap', 'jerk-off', 'jism', 'jiz', 'jizm', 'jizz', 'kawk', 'knob', 'knobead', 'knobed', 'knobend', 'knobhead', 'knobjocky', 'knobjokey', 'kock', 'kondum', 'kondums', 'kum', 'kummer', 'kumming', 'kums', 'kunilingus', 'l3i+ch', 'l3itch', 'labia', 'lmfao', 'lust', 'lusting', 'm0f0', 'm0fo', 'm45terbate', 'ma5terb8', 'ma5terbate', 'masochist', 'master-bate', 'masterb8', 'masterbat*', 'masterbat3', 'masterbate', 'masterbation', 'masterbations', 'masturbate', 'mo-fo', 'mof0', 'mofo', 'mothafuck', 'mothafucka', 'mothafuckas', 'mothafuckaz', 'mothafucked', 'mothafucker', 'mothafuckers', 'mothafuckin', 'mothafucking', 'mothafuckings', 'mothafucks', 'mother fucker', 'motherfuck', 'motherfucked', 'motherfucker', 'motherfuckers', 'motherfuckin', 'motherfucking', 'motherfuckings', 'motherfuckka', 'motherfucks', 'muff', 'mutha', 'muthafecker', 'muthafuckker', 'muther', 'mutherfucker', 'n1gga', 'n1gger', 'nazi', 'nigg3r', 'nigg4h', 'nigga', 'niggah', 'niggas', 'niggaz', 'nigger', 'niggers', 'nob', 'nob jokey', 'nobhead', 'nobjocky', 'nobjokey', 'numbnuts', 'nutsack', 'orgasim', 'orgasims', 'orgasm', 'orgasms', 'p0rn', 'pawn', 'pecker', 'penis', 'penisfucker', 'phonesex', 'phuck', 'phuk', 'phuked', 'phuking', 'phukked', 'phukking', 'phuks', 'phuq', 'pigfucker', 'pimpis', 'piss', 'pissed', 'pisser', 'pissers', 'pisses', 'pissflaps', 'pissin', 'pissing', 'pissoff', 'poop', 'porn', 'porno', 'pornography', 'pornos', 'prick', 'pricks', 'pron', 'pube', 'pusse', 'pussi', 'pussies', 'pussy', 'pussys', 'rectum', 'retard', 'rimjaw', 'rimming', 's hit', 's.o.b.', 'sadist', 'schlong', 'screwing', 'scroat', 'scrote', 'scrotum', 'semen', 'sex', 'sh!+', 'sh!t', 'sh1t', 'shag', 'shagger', 'shaggin', 'shagging', 'shemale', 'shi+', 'shit', 'shitdick', 'shite', 'shited', 'shitey', 'shitfuck', 'shitfull', 'shithead', 'shiting', 'shitings', 'shits', 'shitted', 'shitter', 'shitters', 'shitting', 'shittings', 'shitty', 'skank', 'slut', 'sluts', 'smegma', 'smut', 'snatch', 'son-of-a-bitch', 'spac', 'spunk', 's_h_i_t', 't1tt1e5', 't1tties', 'teets', 'teez', 'testical', 'testicle', 'tit', 'titfuck', 'tits', 'titt', 'tittie5', 'tittiefucker', 'titties', 'tittyfuck', 'tittywank', 'titwank', 'tosser', 'turd', 'tw4t', 'twat', 'twathead', 'twatty', 'twunt', 'twunter', 'v14gra', 'v1gra', 'vagina', 'viagra', 'vulva', 'w00se', 'wang', 'wank', 'wanker', 'wanky', 'whoar', 'whore', 'willies', 'willy', 'xrated', 'xxx']

input_para = """There are two paths a human's soul may take. One that goes on a journey towards the outer world, to create great things, 
                to learn about anything material, to earn money, fame, power  etc. The other path is a U-turn, where one tries to learn the self. 
                It is not the 'self' that python understands, but a human's self. This second study is spirutuality. 
                One can learn it by studying upanishads. It has the power to change your life and bring peace in your life.

                However, Spirituality is not for the faint hearted. One must have balls to be able to pursue this path. You will need to question
                your actions regularly and understand the reasons why you take these actions.

                It is often said that to be able to appreciate spiritualty, one must pursue thier dreams and give their best to achieve them.
                After attaining such successes a couple of times, its easier to realize that a kind of emptiness stays with you, even after
                achieving the goals you had decided. And you would be more open and ready for understanding SELF now.
            """
[word for word in input_para.split() if word in swear_words]










#  Q4 Using reduce function: PTS:100

# a. add only even numbers in a list
from functools import reduce
reduce( (lambda a,b : a+b) , [x for x in [1,2,3,4,5,6] if x%2==0] )

# b. find the biggest character in a string (printable ASCII characters)
find the biggest character in a string (printable ASCII characters)
reduce( lambda a,b : a if ord(a) > ord(b) else b, 'whoami' )

# c. adds every 3rd number in a list
my_list =[1,2,3,4,5,6,7,8,9,10]
reduce( (lambda a,b : a+b) , [my_list[i] for i in range(len(my_list)) if i%3==0] )










# Q5 - Using randint, random.choice and list comprehensions, write an expression that generates 15 random KADDAADDDD number plates, 
# where KA is fixed, D stands for a digit, and A stands for Capital alphabets. 10<<DD<<99 & 1000<<DDDD<<9999

import string
['KA' + str(random.choice(range(10,99))) + ''.join([random.choice(string.ascii_uppercase) for _ in range(2)]) + str(random.choice(range(1000,9999))) for i in range(15)]











# Q6 - Write the above again from scratch where KA can be changed to DL, and 1000/9999 ranges can be provided. 
# Now use a partial function such that 1000/9999 are hardcoded, but KA can be provided PTS:50¶