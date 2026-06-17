from EmotionDetection.emotion_detection import emotion_detector
import unittest


testcases = [
    ("I am glad this happened", "joy"),
    ("I am really mad about this", "anger"),
    ("I feel disgusted just hearing about this","disgust"),
    ("I am so sad about this sadness","sadness"),
    ("I am really afraid that this will happen","fear")
]


class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        for text, emotion in testcases:
            output = emotion_detector(text)
            self.assertEqual(emotion, output["dominant_emotion"])


unittest.main()