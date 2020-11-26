from diaries.DiarySample import DiarySample
from diaries.takamotoDiaryNew import TakamotoDiaryNew

diaries = [DiarySample(), TakamotoDiaryNew(), ]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()