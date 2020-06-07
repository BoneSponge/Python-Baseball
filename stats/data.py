import os
import glob
import pandas as pd

game_files = glob.glob(os.path.join(os.getcwd(),"games",'*.EVE'))

game_files.sort()

game_frames = []
for game_file in game_files:
    game_frame = pd.read_csv(game_file, names = ["type",'multi2','multi3','multi4','multi5','multi6','event'])
    game_frames.append(game_frame)

games = pd.concat(game_frames)

games.loc[games['multi5'] == "??", ['multi5']] = "" # 1st arg denotes "??" values in rows of column multi5, 2nd arg denotes which column to change values in

identifiers = games['multi2'].str.extract(r'(.LS(\d{4})\d{5})')

identifiers = identifiers.fillna(method="ffill")

identifiers.columns = ['game_id','year'] # .columns permits setting of column labels to a given list

games = pd.concat([games, identifiers], axis=1, sort=False)
games = games.fillna('')
games.loc[:,'type'] = pd.Categorical(games.loc[:,'type']) # ":" denotes all rows

print(games.head())
