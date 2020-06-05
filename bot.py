import random

from credentials import IAM_AUTHENTICATOR, SERVICE_URL
from const import NEGATIVE_EMOTIONS, POSITIVE_EMOTIONS, MESSAGES, MOODS
from tone import Tone


class Bot():
    def __init__(self):
        self.current_mood=0
        self.tone = Tone(IAM_AUTHENTICATOR, SERVICE_URL)

    def _check_mood_tone(self, user_tones):
        #  check mood: -1 means sad, 0 - neutral, 1 - happy
        user_emotions = [tone['tone_id'] for tone in user_tones]
        tones_mapper = lambda emotion: 1 if emotion in POSITIVE_EMOTIONS else (-1 if emotion in NEGATIVE_EMOTIONS else 0)
        return sum(map(tones_mapper, user_emotions))

    def _get_feedback_message(self):
        return random.choice(MESSAGES[self.current_mood])

    def _update_mood(self, user_moods):
        mood_tone = self._check_mood_tone(user_moods)
        new_mood = self.current_mood + mood_tone
        #  update mood if it in allowed mood state range [-1; 1]
        if new_mood in range(-1,2):
            self.current_mood = new_mood

    def _handle_mood_command(self):
        return MOODS[self.current_mood]

    def handle_user_message(self, msg):
        if msg.lower() == 'mood':
            return self._handle_mood_command()
        else:
            user_moods = self.tone.get_tone(msg)
            if len(user_moods):
                self._update_mood(user_moods)
            return self._get_feedback_message()
