import pandas as pd
import numpy as np

TopFrame_DataFrame = pd.read_csv("SNICKRS-main\TopFrame.txt")
BottomFrame_DataFrame = pd.read_csv("SNICKRS-main\Bottom_Frame.txt")


# Function to autofill the months
def autofill_months(data):
    months = [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec",
    ]
    last_month = None

    try:
        for i in range(len(data)):
            if i % 2 == 0:  # we're on a month entry
                if data[i]:  # if the entry is not an empty string
                    last_month = data[i]
                else:
                    next_month_index = (months.index(last_month) + 1) % 12
                    data[i] = months[next_month_index]
                    last_month = months[next_month_index]
        return data
    except:
        return data


def find_cow(cow):
    
    data = list((TopFrame_DataFrame.query(f"(Number == {cow})").iloc[0]))
    data.append(list((BottomFrame_DataFrame.query(f"(Number == {cow})").iloc[0])))

    data[-1][11:55] = autofill_months(data[-1][11:55])
    data[-1][65:109] = autofill_months(data[-1][65:109])
    data[-1][119:163] = autofill_months(data[-1][119:163])
    data[-1][173:217] = autofill_months(data[-1][173:217])
    data[-1][227:271] = autofill_months(data[-1][227:271])
    data[-1][281:325] = autofill_months(data[-1][281:325])
    data[-1][335:379] = autofill_months(data[-1][335:379])
    data[-1][389:433] = autofill_months(data[-1][389:433])
    data[-1][443:487] = autofill_months(data[-1][443:487])
    data[-1][497:541] = autofill_months(data[-1][497:541])
    data[-1][551:595] = autofill_months(data[-1][551:595])

    return data


def save_data(data):
    data_values = [item.cget("text") for item in data]

    top_frame = data_values[:19]
    bottom_frame = data_values[19:]

    clean_top_frame = [str(i).split("\n")[-1] for i in top_frame]
    clean_top_frame.append(top_frame[-1])
    
    
    bottom_frame.insert(0, clean_top_frame[0])

    clean_bottom_frame = [[str(i).split("\n")[-1]] for i in bottom_frame[1:11]]
    clean_bottom_frame += [float(str(i).split("\n")) for i in bottom_frame[11:33]]
    clean_bottom_frame += [[str(i).split("\n")[-1]] for i in bottom_frame[33:43]]
    clean_bottom_frame += [str(i).split("\n") for i in bottom_frame[43:65]]
    clean_bottom_frame += [[str(i).split("\n")[-1]] for i in bottom_frame[65:75]]
    clean_bottom_frame += [str(i).split("\n") for i in bottom_frame[75:97]]
    clean_bottom_frame += [[str(i).split("\n")[-1]] for i in bottom_frame[97:107]]
    clean_bottom_frame += [str(i).split("\n") for i in bottom_frame[107:129]]
    clean_bottom_frame += [[str(i).split("\n")[-1]] for i in bottom_frame[129:139]]
    clean_bottom_frame += [str(i).split("\n") for i in bottom_frame[139:161]]
    clean_bottom_frame += [[str(i).split("\n")[-1]] for i in bottom_frame[161:171]]
    clean_bottom_frame += [str(i).split("\n") for i in bottom_frame[171:193]]
    clean_bottom_frame += [[str(i).split("\n")[-1]] for i in bottom_frame[193:203]]
    clean_bottom_frame += [str(i).split("\n") for i in bottom_frame[203:225]]
    clean_bottom_frame += [[str(i).split("\n")[-1]] for i in bottom_frame[225:235]]
    clean_bottom_frame += [str(i).split("\n") for i in bottom_frame[235:257]]
    clean_bottom_frame += [[str(i).split("\n")[-1]] for i in bottom_frame[257:267]]
    clean_bottom_frame += [str(i).split("\n") for i in bottom_frame[267:289]]
    clean_bottom_frame += [[str(i).split("\n")[-1]] for i in bottom_frame[289:299]]
    clean_bottom_frame += [str(i).split("\n") for i in bottom_frame[299:321]]
    clean_bottom_frame += [[str(i).split("\n")[-1]] for i in bottom_frame[321:331]]
    clean_bottom_frame += [str(i).split("\n") for i in bottom_frame[331:353]]

    clean_bottom_frame = [item for sublist in clean_bottom_frame for item in sublist]
    clean_bottom_frame.insert(0, clean_top_frame[0])
    

    BottomFrame_DataFrame.loc[
        BottomFrame_DataFrame["Number"] == int(clean_top_frame[0]), :
    ] = clean_bottom_frame
        
    TopFrame_DataFrame.loc[
        TopFrame_DataFrame["Number"] == int(clean_top_frame[0]), :
    ] = clean_top_frame
    
    TopFrame_DataFrame.to_csv("SNICKRS-main\TopFrame.txt", index=False)
    BottomFrame_DataFrame.to_csv("SNICKRS-main\Bottom_Frame.txt", index=False)
    

def add_cow(calf_num, mama_num, dob):
    calf_num = int(calf_num)
    mama_num = int(mama_num)
    mama_breeding_data = mama_breeding_list(mama_num)[9::10]
    mama_breeding_data = [str(i) for i in mama_breeding_data]
    index = mama_breeding_data.index("")
    mama_breeding_data[index] = dob
    mama_breeding_data = list(
        zip(BottomFrame_DataFrame.columns[10::54], mama_breeding_data)
    )
    column_to_change = mama_breeding_data[index]

    BottomFrame_DataFrame.loc[
        BottomFrame_DataFrame["Number"] == mama_num, column_to_change[0]
    ] = column_to_change[1]

    column_to_change_before = BottomFrame_DataFrame.columns[
        BottomFrame_DataFrame.columns.get_loc(column_to_change[0]) - 1
    ]
    column_to_change_before = list(zip([column_to_change_before], [calf_num]))[0]

    BottomFrame_DataFrame.loc[
        BottomFrame_DataFrame["Number"] == mama_num, column_to_change_before[0]
    ] = calf_num

    if mama_num in list(TopFrame_DataFrame["Number"]):
        mama_data = list((TopFrame_DataFrame.query(f"(Number == {mama_num})").iloc[0]))[
            7:10
        ]
        mama_data.append(
            list((TopFrame_DataFrame.query(f"(Number == {mama_num})").iloc[0]))[11:14]
        )
        calf_empty = [
            calf_num,
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
        ]

        calf_dict = dict(zip(list(TopFrame_DataFrame.columns), calf_empty))
        calf_top_dataframe = pd.DataFrame([calf_dict])
        calf_top_dataframe["GrGrGrDam"] = mama_data[0]
        calf_top_dataframe["GrGrDam"] = mama_data[1]
        calf_top_dataframe["GrDam"] = mama_data[2]
        calf_top_dataframe["Dam"] = mama_num
        calf_top_dataframe["GrGrGrSire"] = mama_data[-1][0]
        calf_top_dataframe["GrGrSire"] = mama_data[-1][1]
        calf_top_dataframe["GrSire"] = mama_data[-1][2]
        calf_top_dataframe["Sire"] = find_dad(mama_num, dob)
        calf_top_dataframe["bday"] = dob

        calf_bottom_frame = [calf_num]
        while len(calf_bottom_frame) < 595:
            calf_bottom_frame.append("")

        calf_bottom_frame_dict = dict(
            zip(list(BottomFrame_DataFrame.columns), calf_bottom_frame)
        )
        calf_bottom_dataframe = pd.DataFrame([calf_bottom_frame_dict])

        TopFrame_DataFrame.loc[len(TopFrame_DataFrame)] = calf_top_dataframe.iloc[0]
        BottomFrame_DataFrame.loc[
            len(BottomFrame_DataFrame)
        ] = calf_bottom_dataframe.iloc[0]


def find_dad(mama_num, dob):
    mama_num = int(mama_num)
    dob = str(dob)
    mama_data = mama_breeding_list(mama_num)
    index_of_dob = mama_data.index(dob)
    if mama_data[index_of_dob - 5] != "":
        return mama_data[index_of_dob - 5]
    elif mama_data[index_of_dob - 7] != "":
        return mama_data[index_of_dob - 7]
    else:
        return mama_data[index_of_dob - 9]


def mama_breeding_list(mama_num):
    mama_data = []
    mama_data = list((BottomFrame_DataFrame.query(f"(Number == {mama_num})").iloc[0]))[
        1:11
    ]
    mama_data += list((BottomFrame_DataFrame.query(f"(Number == {mama_num})").iloc[0]))[
        55:65
    ]
    mama_data += list((BottomFrame_DataFrame.query(f"(Number == {mama_num})").iloc[0]))[
        109:119
    ]
    mama_data += list((BottomFrame_DataFrame.query(f"(Number == {mama_num})").iloc[0]))[
        163:173
    ]
    mama_data += list((BottomFrame_DataFrame.query(f"(Number == {mama_num})").iloc[0]))[
        217:227
    ]
    mama_data += list((BottomFrame_DataFrame.query(f"(Number == {mama_num})").iloc[0]))[
        271:281
    ]
    mama_data += list((BottomFrame_DataFrame.query(f"(Number == {mama_num})").iloc[0]))[
        325:335
    ]
    mama_data += list((BottomFrame_DataFrame.query(f"(Number == {mama_num})").iloc[0]))[
        379:389
    ]
    mama_data += list((BottomFrame_DataFrame.query(f"(Number == {mama_num})").iloc[0]))[
        433:443
    ]
    mama_data += list((BottomFrame_DataFrame.query(f"(Number == {mama_num})").iloc[0]))[
        487:497
    ]
    mama_data += list((BottomFrame_DataFrame.query(f"(Number == {mama_num})").iloc[0]))[
        541:551
    ]
    mama_data = [str(i) for i in mama_data]
    return mama_data


find_cow(619)
