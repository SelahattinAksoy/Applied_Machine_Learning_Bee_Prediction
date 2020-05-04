from builtins import enumerate

from pydub import AudioSegment #for soare the audio file
from pathlib import Path  #Path lib for looking file in a path


def FindFileNamesByPath(path,typeofFile):

    File_List = [path.name for path in Path(path).rglob('*.'+typeofFile)]
    return File_List



def ReadLabFile(list_of_sound_file_name):

    timeList_lab_all = []
    for j in list_of_sound_file_name:

        labFile = open("Data\\" + j[:-4] + ".lab", "r")

        labFile.readline()
        line = labFile.readline()
        timeList = []
        while line:

            line = line.split('	')
            if line[0] == '.\n':
                break

            startTime = float(line.pop(0))
            line.insert(0, startTime)
            finishTime = float(line.pop(1))
            line.insert(1, finishTime)
            # line.pop(-1)#to get rid of bee nobee
            timeList.append(line)
            line = labFile.readline()
        timeList_lab_all.append(timeList)
    return timeList_lab_all


list_of_sound_file_name = FindFileNamesByPath("Data", "wav")
split_timeList = ReadLabFile(list_of_sound_file_name)

def Clean_Wav_File(timeList):
    Vaw_obj_list = ["CF003 - Active - Day - (214).wav", "CF003 - Active - Day - (215).wav", "CF003 - Active - Day - (216).wav"]

    for counter, i in enumerate(Vaw_obj_list):

        newAudio = AudioSegment.from_wav("Data\\" + i)

        for num, a in enumerate(timeList[counter]):
            newAu = newAudio[a[0] * 1000:a[1] * 1000]
            newAu.export("Cleaned Data\\Cleaned_Voice\\" + i + "--" + (a[2])[:-1] + "--" + str(num) + ".wav", format="wav")



Clean_Wav_File(split_timeList)

print(len(list_of_sound_file_name))
print(len(split_timeList[0])+len(split_timeList[1])+len(split_timeList[2]))