import random

from const import NEGATIVE_EMOTIONS, POSITIVE_EMOTIONS, MESSAGES

class Bot():
    def __init__(self):
        self.current_mood=0

    def _check_mood_tone(self, user_tones):
        user_emotions = [tone['tone_id'] for tone in user_tones]
        tones_mapper = lambda emotion: 1 if emotion in POSITIVE_EMOTIONS else (-1 if emotion in NEGATIVE_EMOTIONS else 0)
        return sum(map(tones_mapper, user_emotions))

    def get_message(self):
        return MESSAGES[self.current_mood][random.randint(0, 4)]

    def change_mood(self, user_moods):
        mood_tone = self._check_mood_tone(user_moods)
        new_tone = self.current_mood + mood_tone
        if new_tone >= -1 and new_tone <= 1:
            this.current_mood = new_tone