from diaries.AbstractDiary import AbstractDiary


class TakamotoDiaryNew(AbstractDiary):

    def get_date(self):
        return "2020-11-26"

    def get_summary(self):
        return "資料が全然なくて焦った（受け売り）"

    def get_author(self):
        return "Takamoto"