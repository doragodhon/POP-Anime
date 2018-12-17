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

def season_2017_analysis():
    """ Analyze the information from data_input """
    name, score, audience, tag, season = data_input()                       # INPUT: Recieve Info from database

    # -------------------------------- BUILD : Create list for each season ----------------------------------
    spring_2017 = []
    summer_2017 = []
    fall_2017   = []
    winter_2017 = []

    # ------------------------------- GET : Number of audience from database --------------------------------
    audience_dict = {}
    audience_list = []
    for run in audience:
        audience_list.append(run)
    for number in range(len(name)):
        audience_dict[name[number]] = audience_list[number]

    # ----------------------------- GET: Tag list for each Anime from database ------------------------------
    tag_dict = {}
    tag_list = []
    for run in tag:
        tag_list.append(run)
    for number in range(len(name)):
        tag_dict[name[number]] = tag_list[number]

    # --------------------------- GET: Season list for each Anime from database -----------------------------
    season_dict = {}
    season_list = []
    for run in season:
        season_list.append(run)
    for number in range(len(name)):
        season_dict[name[number]] = season_list[number]

    # ------------------------------- PUT : Anime from each season into list --------------------------------
    for run in season_dict:
        if season_dict[run] == 'Spring 2017':
            spring_2017.append(run)
        elif season_dict[run] == 'Summer 2017':
            summer_2017.append(run)
        elif season_dict[run] == 'Fall 2017':
            fall_2017.append(run)
        elif season_dict[run] == 'Winter 2017':
            winter_2017.append(run)                                   

    # ---------------------------- Analyzed : Which Anime in Spring is most popular -------------------------

    spring_dict = {}
    spring_list = []
    for run in spring_2017:
        spring_list.append(audience_dict[run])
    spring_score = max(spring_list)
    for run in spring_2017:
        spring_dict[run] = audience_dict[run]
        if spring_dict[run] == spring_score:
            top_spring = run
    top_spring = '%s : %s' %(top_spring, tag_dict[top_spring])

    # ---------------------------- Analyzed : Which Anime in Summer is most popular -------------------------

    summer_dict = {}
    summer_list = []
    for run in summer_2017:
        summer_list.append(audience_dict[run])
    summer_score = max(summer_list)
    for run in summer_2017:
        summer_dict[run] = audience_dict[run]
        if summer_dict[run] == summer_score:
            top_summer = run
    top_summer = '%s : %s' %(top_summer, tag_dict[top_summer])

    # ---------------------------- Analyzed : Which Anime in Fall is most popular ---------------------------

    fall_dict = {}
    fall_list = []
    for run in fall_2017:
        fall_list.append(audience_dict[run])
    fall_score = max(fall_list)
    for run in fall_2017:
        fall_dict[run] = audience_dict[run]
        if fall_dict[run] == fall_score:
            top_fall = run
    top_fall = '%s : %s' %(top_fall, tag_dict[top_fall])

    # --------------------------- Analyzed : Which Anime in Winter is most popular --------------------------

    winter_dict = {}
    winter_list = []
    for run in winter_2017:
        winter_list.append(audience_dict[run])
    winter_score = max(winter_list)
    for run in winter_2017:
        winter_dict[run] = audience_dict[run]
        if winter_dict[run] == winter_score:
            top_winter = run
    top_winter = '%s : %s' %(top_winter, tag_dict[top_winter])

    # ---------------------------- SORTING : Rearrange and Filter some Data ---------------------------------

    spring_tuples = sorted(spring_dict.items() , reverse=True, key=lambda x: x[1])
    summer_tuples = sorted(summer_dict.items() , reverse=True, key=lambda x: x[1])
    fall_tuples   = sorted(fall_dict.items()   , reverse=True, key=lambda x: x[1])
    winter_tuples = sorted(winter_dict.items() , reverse=True, key=lambda x: x[1])

    # --------------------------- OUTPUT : Top 10 Spring 2017 Ranking Chart ---------------------------------

    spring_2017_chart = pg.Pie()
    spring_2017_chart.title = 'Top 10 Spring 2017 Ranking Chart'
    for element in spring_tuples[0:11]:
        spring_2017_chart.add(element[0], element[1])
    spring_2017_chart.render_to_file('spring_2017_chart.svg')

    # --------------------------- OUTPUT : Top 10 Summer 2017 Ranking Chart ---------------------------------

    summer_2017_chart = pg.Pie()
    summer_2017_chart.title = 'Top 10 Summer 2017 Ranking Chart'
    for element in summer_tuples[0:11]:
        summer_2017_chart.add(element[0], element[1])
    summer_2017_chart.render_to_file('summer_2017_chart.svg')

    # -------------------------------- OUTPUT : Fall 2017 Ranking Chart -------------------------------------

    fall_2017_chart = pg.Pie()
    fall_2017_chart.title = 'Top 10 Fall 2017 Ranking Chart'
    for element in fall_tuples[0:11]:
        fall_2017_chart.add(element[0], element[1])
    fall_2017_chart.render_to_file('fall_2017_chart.svg')

    # ------------------------------- OUTPUT : Winter 2017 Ranking Chart ------------------------------------

    winter_2017_chart = pg.Pie()
    winter_2017_chart.title = 'Top 10 Winter 2017 Ranking Chart'
    for element in winter_tuples[0:11]:
        winter_2017_chart.add(element[0], element[1])
    winter_2017_chart.render_to_file('winter_2017_chart.svg')


season_2017_analysis()
