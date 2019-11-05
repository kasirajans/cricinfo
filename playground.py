#!/usr/local/bin/python3

from pycricbuzz import Cricbuzz
from prettytable import PrettyTable
import pandas as pd
import argparse

def get_matchs(cricObj):
    matches=cricObj.matches()
    return matches

def get_live_score(matchs):
    
    for i in range(len(matchs)):
        if matchs[i]['mchstate'] == 'complete':
            return matchs[i]

def get_match_status(matchs):
    matchsList=[]
    for i in range(len(matchs)):
        if matchs[i]['mchstate'] == 'complete':
            matchsList.append(matchs[i])        
    return matchsList

def get_match_all(matchs):
    matchsList=[]
    for i in range(len(matchs)):
       matchsList.append(matchs[i])
        
    return matchsList

def get_match_live(matchs,cricObj):
    matchsList=[]
    matchDetails=[]
    for i in range(len(matchs)):
        if matchs[i]['mchstate'] == 'inprogress':
            matchsList.append(matchs[i])
    for i in range(len(matchsList)):
        matchDetails.append(cricObj.livescore(matchs[i]['id']))
    # print(matchDetails)
    return matchDetails

def Main():

    parser = argparse.ArgumentParser(description='Get Cricket Scores')
    parser.add_argument('-id',action="store", dest="userId" )
    parser.add_argument('-status',action='store_true')
    parser.add_argument('-all',action='store_true')
    parser.add_argument('-complete',action='store_true')
    parser.add_argument('-live',action='store_true')   
    args=parser.parse_args()

    cricObj = Cricbuzz()
    tableObj = PrettyTable()
    tableObj.field_names=['TournamentName','MatchType','Status']

    matchs=get_matchs(cricObj)
    # liveScore=get_live_score(matchs)
    # matchStatus=get_match_status(matchs)
    # print(matchStatus)
    if args.all:
        tableObj.field_names=['TournamentName','MatchType','Status']
        matchStatus=get_match_all(matchs)
    # matchStatusDt=pd.DataFrame(matchStatus)
        for i in range(len(matchStatus)):
            tableObj.add_row([matchStatus[i]['srs'],matchStatus[i]['type'],matchStatus[i]['status']])
        if not len(matchStatus):
            print('Match is not in progress')
        else:
            print((tableObj))
    if args.complete:
        matchStatus=get_match_status(matchs)
    # matchStatusDt=pd.DataFrame(matchStatus)
        for i in range(len(matchStatus)):
            tableObj.add_row([matchStatus[i]['srs'],matchStatus[i]['type'],matchStatus[i]['status']])

    if args.live:
        tableObj.field_names=['TournamentName','MatchType','Status']
        matchStatus=get_match_live(matchs,cricObj)
    # matchStatusDt=pd.DataFrame(matchStatus)
        # print(matchStatus)
        for i in range(len(matchStatus)):
            tableObj.add_row([matchStatus[i]['srs'],matchStatus[i]['type'],matchStatus[i]['status']])
            # tableObj.add_row([matchStatus[i]['batting']['team']])
        # for i in range(len(matchStatus)):
        #     tableObj.add_row([matchStatus[i]['srs'],matchStatus[i]['type'],matchStatus[i]['status']])
        if not len(matchStatus):
            print('Match is not in progress')
        else:
            print((tableObj))
    

if __name__ == "__main__":
    Main()