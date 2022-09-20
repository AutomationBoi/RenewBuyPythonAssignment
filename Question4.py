"""
Assuming we are getting a dict of list of clubs

"""

import pandas as pd

def bestFootBallClub(listOfClubs):
    df=pd.DataFrame(listOfClubs)
    df['totalPoints']=df['wins'].apply(lambda x: 3*x)+df['draws'].apply(lambda x: 1*x)
    df['goalDiff'] = df['scored']-df['conceded']
    df.sort_values(['totalPoints','goalDiff'],inplace=True,ascending=False)
    df.reset_index(drop=True,inplace=True)
    return dict(df.iloc[0])


if __name__=='__main__':
    listOfClubs = [{"name": "Manchester United", "wins": 30, "loss": 3, "draws": 9, "scored": 88,
                    "conceded": 20}, {"name": "Real Madrid", "wins": 21, "loss": 4, "draws": 5, "scored": 80,
                                      "conceded": 19},
                   {"name": "Arsenal", "wins": 32, "loss": 3, "draws": 3, "scored": 90,
                    "conceded": 30}
        , {"name": "Barcelona", "wins": 28, "loss": 7, "draws": 6, "scored": 90,
           "conceded": 25}]
    print(bestFootBallClub(listOfClubs))


"""
TEST CASE

1. 
    listOfClubs = [{"name": "Manchester United", "wins": 30, "loss": 3, "draws": 5, "scored": 88,
                    "conceded": 20}, {"name": "Real Madrid", "wins": 21, "loss": 4, "draws": 5, "scored": 80,
                                      "conceded": 19},
                   {"name": "Arsenal", "wins": 32, "loss": 3, "draws": 3, "scored": 90,
                    "conceded": 30}
        , {"name": "Barcelona", "wins": 28, "loss": 7, "draws": 6, "scored": 90,
           "conceded": 25}]

    Expected: Arsenal [max score]
    Actual: Arsenal

2.
    listOfClubs = [{"name": "Manchester United", "wins": 30, "loss": 3, "draws": 9, "scored": 88,
                    "conceded": 20}, {"name": "Real Madrid", "wins": 21, "loss": 4, "draws": 5, "scored": 80,
                                      "conceded": 19},
                   {"name": "Arsenal", "wins": 32, "loss": 3, "draws": 3, "scored": 90,
                    "conceded": 30}
        , {"name": "Barcelona", "wins": 28, "loss": 7, "draws": 6, "scored": 90,
           "conceded": 25}]
    Expected: Manchester United[max goal diff]
    Actual: Manchester United
"""