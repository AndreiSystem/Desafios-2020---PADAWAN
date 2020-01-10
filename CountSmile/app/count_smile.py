# valid_list = [':)', ':D', ';-D', ':~)', ';D', ':-D', ':-)', ';~)']

class SmileFace:

    def smile_face_check(self, faces_list: list):
        _result = 0
        for face in faces_list:
            if self._has_eyes(face) and self._has_noses(face) and self._has_smile(face):
                _result += 1
        return _result

    def _has_eyes(self, face: str) -> bool:
        if ':' in face or ';' in face:
            return True
        else:
            return False

    def _has_noses(self, face: str) -> bool:
        face = face.strip()
        if len(face) == 2:
            return True

        if '-' in face or '~' in face:
            return True
        else:
            return False

    def _has_smile(self, face: str) -> bool:
        if 'D' in face or ')' in face:
            return True
        else:
            return False


