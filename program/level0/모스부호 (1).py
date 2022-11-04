def solution(letter):
    answer = ''
    answer_list = []
    letter_split = []
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
    }
    letter_split = letter.split()
    for i in range(len(letter_split)):
        answer_list.append(morse.get(letter_split[i]))
        answer = ''.join(map(str, answer_list))
    return answer