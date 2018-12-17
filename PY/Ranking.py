import csv
import pandas as pd
import pygal as pg

def data_input():
    """ Convert information from csv into python """
    reader   = pd.read_csv("C:/Users/Mix/Desktop/list_anime.csv", encoding="ISO-8859-1")
    name     = reader["title"]
    score    = reader["scored_by"]
    audience = reader["members"]
    season   = reader["premiered"]
    tag      = reader["genre"]
    return name, score, audience, tag, season

def rank_analysis():
    """ Analyze the information from data_input """
    name, score, audience, tag, season = data_input()                    # INPUT: Recieve Info from database

    # ------------------------------- GET : Highest score for each Anime in database -----------------------
    score_dict = {}
    score_list = []
    score_total = 0
    for run in score:
        score_list.append(run)
    for number in range(len(name)):
        score_dict[name[number]] = score_list[number]
        score_total += score_list[number]
    top_score = max(score_list)

    # -------------------------------- GET : Highest audience for each Anime in database -------------------
    audience_dict = {}
    audience_list = []
    audience_total = 0
    for run in audience:
        audience_list.append(run)
    for number in range(len(name)):
        audience_dict[name[number]] = audience_list[number]
        audience_total += audience_list[number]
    top_audience = max(audience_list)

    # ----------------------------------- Analyzed : Top score anime's name --------------------------------
    for title in name:
        if top_score == score_dict[title]:
            top_score_name = title

    # ----------------------------------- Analyzed : Top audience anime's name------------------------------
    for title in name:
        if top_audience == audience_dict[title]:
            top_audience_name = title

    # ---------------------------- SORTING : Rearrange and Filter some Data --------------------------------

    score_tuples = sorted(score_dict.items() , reverse=True, key=lambda x: x[1])
    audience_tuples = sorted(audience_dict.items() , reverse=True, key=lambda x: x[1])

    # ------------------------------- OUTPUT : Overall Score Ranking Chart ---------------------------------

    score_ranking_chart = pg.Pie()
    score_ranking_chart.title = 'Overall Score Ranking Chart'
    score_ranking_chart.add(top_score_name, top_score)
    score_ranking_chart.add('Other Anime Total Score', (score_total-top_score))
    score_ranking_chart.render_to_file('score_ranking_chart.svg')

    # -------------------------------- OUTPUT : Top 5 Score Ranking Chart ----------------------------------

    top5_score_chart = pg.Pie()
    top5_score_chart.title = 'Top 5 Score Ranking Chart'
    for element in score_tuples[0:6]:
        top5_score_chart.add(element[0], element[1])
    top5_score_chart.render_to_file('top5_score_chart.svg')

    # ------------------------------- OUTPUT : Overall Audience Ranking Chart ------------------------------

    audience_ranking_chart = pg.Pie()
    audience_ranking_chart.title = 'Overall Audience Ranking Chart'
    audience_ranking_chart.add(top_audience_name, top_audience)
    audience_ranking_chart.add('Other Anime Total Audience', (audience_total-top_audience))
    audience_ranking_chart.render_to_file('audience_ranking_chart.svg')

    # ------------------------------ OUTPUT : Top 5 Audience Ranking Chart ---------------------------------

    top5_audience_chart = pg.Pie()
    top5_audience_chart.title = 'Top 5 Audience Ranking Chart'
    for element in audience_tuples[0:6]:
        top5_audience_chart.add(element[0], element[1])
    top5_audience_chart.render_to_file('top5_audience_chart.svg')

rank_analysis()
