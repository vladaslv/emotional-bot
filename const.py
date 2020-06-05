MOODS={
    -1:'negative',
    0:'neutral',
    1:'positive',
}
NEGATIVE_EMOTIONS=['anger', 'sadness', 'fear']
POSITIVE_EMOTIONS=['joy']
MESSAGES={
    -1: [
        'It hurts my feelings',
        'I feel so bad about what you wrote',
        'Your message make me sad',
        'I\'m very sorry to hear that',
        'Sorry, things aren\'t working for you'],
    0: [
        'I like your way of thinking',
        'I understand',
        'I see',
        'Interesting, Ok',
        'That\'s Ok'],
    1: [
        'Fine, tell me more!',
        'Wow, sounds great!',
        'That\'s good news!',
        'Oh, that\'s very kind of you',
        'That\'s wonderful! Tell me everything from start to finish!']
}
GRAPH_URL='https://graph.facebook.com/v7.0/me/messages?access_token='